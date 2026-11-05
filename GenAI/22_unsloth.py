# Unsloth : https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst

# pip install unsloth
# pip install transformers==4.57.6
# pip install --no-deps trl==0.22.2

# FastModel supports loading nearly any model now! This includes Vision and Text models!
from unsloth import FastModel
import torch
from unsloth.chat_templates import get_chat_template
from datasets import load_dataset
from trl import SFTTrainer, SFTConfig
from unsloth.chat_templates import train_on_responses_only

max_seq_length = 2048

model, tokenizer = FastModel.from_pretrained(
    model_name = "unsloth/gemma-3-270m-it",
    max_seq_length = max_seq_length, # Choose any for long context!
    load_in_4bit = False,  # 4 bit quantization to reduce memory
    load_in_8bit = False, # [NEW!] A bit more accurate, uses 2x memory
    full_finetuning = False, # [NEW!] We have full finetuning now!
    # token = "YOUR_HF_TOKEN", # HF Token for gated models
)

#add LoRA adapters so we only need to update a small amount of parameters!

model = FastModel.get_peft_model(
    model,
    r = 128, # Choose any number > 0 ! Suggested 8, 16, 32, 64, 128
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj",],
    lora_alpha = 128,
    lora_dropout = 0, # Supports any, but = 0 is optimized
    bias = "none",    # Supports any, but = "none" is optimized
    # [NEW] "unsloth" uses 30% less VRAM, fits 2x larger batch sizes!
    use_gradient_checkpointing = "unsloth", # True or "unsloth" for very long context
    random_state = 3407,
    use_rslora = False,  # We support rank stabilized LoRA
    loftq_config = None, # And LoftQ
)

# Data Prep
def convert_to_chatml(example):
    return {
        "conversations": [
            {"role": "system", "content": example["task"]},
            {"role": "user", "content": example["input"]},
            {"role": "assistant", "content": example["expected_output"]}
        ]
    }

def formatting_prompts_func(examples):
   convos = examples["conversations"]
   texts = [tokenizer.apply_chat_template(convo, tokenize = False, add_generation_prompt = False).removeprefix('<bos>') for convo in convos]
   return { "text" : texts, }

tokenizer = get_chat_template(
    tokenizer,
    chat_template = "gemma3",
)


dataset = load_dataset("Thytu/ChessInstruct", split = "train[:10000]")

dataset = dataset.map(
    convert_to_chatml
)

# print(dataset[100])


dataset = dataset.map(formatting_prompts_func, batched = True)

# print(dataset[100]['text'])

# Train the model

trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    eval_dataset = None, # Can set up evaluation!
    args = SFTConfig(
        dataset_text_field = "text",
        per_device_train_batch_size = 4,
        gradient_accumulation_steps = 1, # Use GA to mimic batch size!
        warmup_steps = 5,
        num_train_epochs = 1, # Set this for 1 full training run.
        max_steps = 100,
        learning_rate = 5e-5, # Reduce to 2e-5 for long training runs
        logging_steps = 1,
        optim = "adamw_8bit",
        weight_decay = 0.001,
        lr_scheduler_type = "linear",
        seed = 3407,
        output_dir = "outputs",
        report_to = "none", # Use TrackIO/WandB etc
    ),
)


trainer = train_on_responses_only(trainer)

tokenizer.decode(trainer.train_dataset[100]["input_ids"])
response = tokenizer.decode([tokenizer.pad_token_id if x == -100 else x for x in trainer.train_dataset[100]["labels"]]).replace(tokenizer.pad_token, " ")
print(response)

trainer_stats = trainer.train()

#======================================================================

#using model:

messages = [
    {'role': 'system','content':dataset['conversations'][10][0]['content']},
    {"role" : 'user', 'content' : dataset['conversations'][10][1]['content']}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize = False,
    add_generation_prompt = True, # Must add for generation
).removeprefix('<bos>')

from transformers import TextStreamer
_ = model.generate(
    **tokenizer(text, return_tensors = "pt").to("cuda"),
    max_new_tokens = 125,
    temperature = 1, top_p = 0.95, top_k = 64,
    streamer = TextStreamer(tokenizer, skip_prompt = True),
)
print(_)
#======================================================================

# Saving, loading finetuned models

model.save_pretrained("gemma_3_lora")  # Local saving
tokenizer.save_pretrained("gemma_3_lora")



#=========================================================

#Load Locally Stored model : 
"""
from unsloth import FastLanguageModel
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "gemma_3_lora", # YOUR MODEL YOU USED FOR TRAINING
    max_seq_length = 2048,
    load_in_4bit = False,
)
"""