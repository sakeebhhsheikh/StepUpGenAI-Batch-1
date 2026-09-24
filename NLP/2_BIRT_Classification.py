# pip install torch transformers datasets scikit-learn
# pip install 'accelerate>=1.1.0'
import torch
from datasets import Dataset
from transformers import (
    BertTokenizer,
    BertForSequenceClassification,
    Trainer,
    TrainingArguments
)
from sklearn.metrics import accuracy_score, precision_recall_fscore_support


# ============================================================
# 1. DUMMY DATA
# ============================================================

texts = [
    "I love this product",
    "This product is excellent",
    "The service was very good",
    "I am very happy with this",
    "This is an amazing experience",
    "The product works perfectly",
    "I hate this product",
    "This product is terrible",
    "The service was very bad",
    "I am very disappointed",
    "This is a horrible experience",
    "The product does not work"
]

# 1 = Positive
# 0 = Negative
labels = [
    1, 1, 1, 1, 1, 1,
    0, 0, 0, 0, 0, 0
]


# ============================================================
# 2. CREATE DATASET
# ============================================================

data = {
    "text": texts,
    "label": labels
}

dataset = Dataset.from_dict(data)

# Split into training and testing datasets
dataset = dataset.train_test_split(test_size=0.25, seed=42)

train_dataset = dataset["train"]
test_dataset = dataset["test"]

print("Training examples:", len(train_dataset))
print("Testing examples:", len(test_dataset))


# ============================================================
# 3. LOAD PRE-TRAINED BERT TOKENIZER
# ============================================================

model_name = "bert-base-uncased"

tokenizer = BertTokenizer.from_pretrained(model_name)


# ============================================================
# 4. TOKENIZE TEXT
# ============================================================

def tokenize_function(examples):
    return tokenizer(
        examples["text"],
        padding="max_length",
        truncation=True,
        max_length=64
    )


train_dataset = train_dataset.map(
    tokenize_function,
    batched=True
)

test_dataset = test_dataset.map(
    tokenize_function,
    batched=True
)


# Remove original text column
train_dataset = train_dataset.remove_columns(["text"])
test_dataset = test_dataset.remove_columns(["text"])

# Tell Hugging Face to return PyTorch tensors
train_dataset.set_format("torch")
test_dataset.set_format("torch")


# ============================================================
# 5. LOAD PRE-TRAINED BERT MODEL
# ============================================================

model = BertForSequenceClassification.from_pretrained(
    model_name,
    num_labels=2
)


# ============================================================
# 6. EVALUATION METRICS
# ============================================================

def compute_metrics(pred):

    predictions = pred.predictions.argmax(axis=-1)
    labels = pred.label_ids

    accuracy = accuracy_score(labels, predictions)

    precision, recall, f1, _ = precision_recall_fscore_support(
        labels,
        predictions,
        average="binary",
        zero_division=0
    )

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1
    }


# ============================================================
# 7. TRAINING CONFIGURATION
# ============================================================

training_args = TrainingArguments(
    output_dir="./bert_results",

    # Number of training epochs
    num_train_epochs=3,

    # Number of samples processed together
    per_device_train_batch_size=4,

    # Evaluation batch size
    per_device_eval_batch_size=4,

    # Learning rate
    learning_rate=2e-5,

    # Save model after training
    save_strategy="epoch",

    # Evaluate after each epoch
    eval_strategy="epoch",

    # Print training information
    logging_strategy="epoch",

    # Best model will be loaded after training
    load_best_model_at_end=True,

    # Do not use external logging
    report_to="none"
)


# ============================================================
# 8. TRAINER
# ============================================================

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    compute_metrics=compute_metrics
)


# ============================================================
# 9. TRAIN / FINE-TUNE BERT
# ============================================================

print("\nStarting BERT training...\n")

trainer.train()


# ============================================================
# 10. EVALUATE MODEL
# ============================================================

print("\nEvaluating model...\n")

results = trainer.evaluate()

print("Evaluation Results:")
print(results)


# ============================================================
# 11. SAVE MODEL AND TOKENIZER
# ============================================================

model.save_pretrained("./my_bert_model")
tokenizer.save_pretrained("./my_bert_model")

print("\nModel saved to ./my_bert_model")


# ============================================================
# 12. FUNCTION FOR QUERYING THE MODEL
# ============================================================

def predict(text):

    # Tokenize input
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=64
    )

    # Move input to same device as model
    device = model.device
    inputs = {key: value.to(device)
              for key, value in inputs.items()}

    # Disable gradient calculation
    with torch.no_grad():

        outputs = model(**inputs)

    # Convert logits to probabilities
    probabilities = torch.softmax(
        outputs.logits,
        dim=-1
    )

    # Get predicted class
    prediction = torch.argmax(probabilities, dim=-1).item()

    confidence = probabilities[0][prediction].item()

    if prediction == 1:
        label = "Positive"
    else:
        label = "Negative"

    return label, confidence


# ============================================================
# 13. QUERY THE MODEL
# ============================================================

print("\n===== MODEL QUERY =====")

queries = [
    "I really enjoyed this product",
    "This is the worst product",
    "The service was excellent",
    "I am not happy with this"
]

for query in queries:

    label, confidence = predict(query)

    print("\nText:", query)
    print("Prediction:", label)
    print("Confidence:", round(confidence, 4))


# ============================================================
# 14. INTERACTIVE QUERY
# ============================================================

while True:

    user_text = input(
        "\nEnter text (or type 'exit' to quit): "
    )

    if user_text.lower() == "exit":
        break

    label, confidence = predict(user_text)

    print("Prediction:", label)
    print("Confidence:", round(confidence, 4))