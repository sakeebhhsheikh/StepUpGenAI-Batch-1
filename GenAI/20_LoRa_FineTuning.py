import torch
print(torch.cuda.is_available())

device = torch.device("cpu")

print("Training Device :::", device)

from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForCausalLM
from trl import SFTTrainer, SFTConfig

# from peft import LoraConfig
from peft import LoraConfig, TaskType

#Configurations : 

DEVICE = "cpu"
model_name = "Qwen/Qwen2.5-0.5B-Instruct"
output_dir = "./GenAI/FineTuned_model_cpu"

torch.set_num_threads(4)

training_data = [
    {
        "instruction":"What is Python, and what are its key characteristics?",
        "response":"Python is a high-level, interpreted, and dynamically-typed programming language. Its key characteristics include a clean, highly readable syntax, support for multiple programming paradigms (Object-Oriented, Functional, and Procedural), and a vast standard library."
    },
    {
        "instruction":"Is Python code compiled or interpreted?",
        "response":"Python is both compiled and interpreted. When you run a script, the source code (.py) is first compiled into an intermediate low-level form called bytecode (.pyc). This bytecode is then executed line-by-line by the Python Virtual Machine (PVM) interpreter"
    },
    {
        "instruction":"What does it mean that Python is dynamically typed?",
        "response":"In Python, you do not need to declare a variable's data type before using it. The data type is automatically determined at runtime based on the value assigned to the variable. You can change a variable's type later simply by assigning a different value type"
    },
    {
        "instruction":"What is the difference between mutable and immutable objects?",
        "response":"Mutable objects can be changed after they are created (e.g., lists, dictionaries, sets). Immutable objects cannot be modified once they are defined (e.g., strings, tuples, integers, floats). Any operation that modifies them creates a new object in memory."
    },
    {
        "instruction":"What is BeautifulSoup?",
        "response":"BeautifulSoup is a python library used to parse HTML and XML data."
    },
]


dataset = Dataset.from_list(training_data)
print(dataset)


#Tokenization : 

tokenizer = AutoTokenizer.from_pretrained(model_name)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token


#Load Model : 

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    dtype = torch.float32,
    low_cpu_mem_usage = True
)

model.to(DEVICE)

model.config.use_cache = False

def format_input_data(input_data):
    messages = [
        {
            "role":"system",
            "content":"You are a python language expert."
        },
        {
            "role":"user",
            "content":input_data['instruction']
        },
         {
            "role":"assistant",
            "content":input_data['response']
        },
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=False
    )

    #print(text)

    return {"text":text}

dataset = dataset.map(format_input_data)


peft_config = LoraConfig(
    r=4, 
    lora_alpha=8, 
    lora_dropout=0.05, 
    task_type="CAUSAL_LM",
    target_modules=["q_proj", "v_proj"]
    )


#Training Configuration : 

training_args = SFTConfig(
    output_dir = output_dir,
    num_train_epochs=1,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=4,
    learning_rate=1e-4,
    max_length=128,
    logging_steps=1,
    save_strategy="no",
    report_to="none",
    fp16=False,
    bf16=False,
    gradient_checkpointing=False,
    dataloader_num_workers=0,
    use_cpu=True
)


# 8. Trainer erstellen
trainer = SFTTrainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    processing_class=tokenizer,
    peft_config=peft_config,
)


# 10. Training starten
print("Start CPU Fine-Tuning ...")

trainer.train()


print("Fine Tuning Completed.")


trainer.save_model(output_dir)
tokenizer.save_pretrained(output_dir)

print("Model saved to :", output_dir)

# https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst