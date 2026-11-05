import torch

from transformers import AutoTokenizer, AutoModelForCausalLM

from peft import PeftModel

model_name = "Qwen/Qwen2.5-0.5B-Instruct"
adapter_path = "./GenAI/FineTuned_model_cpu"

device=torch.device("cpu")

# load tokenizer
tokenizer = AutoTokenizer.from_pretrained(adapter_path)

# load base model to cpu
base_model = AutoModelForCausalLM.from_pretrained(
    model_name,
    dtype = torch.float32,
)

base_model.to(device)

#Load trained LoRA adapter
model = PeftModel.from_pretrained(base_model, adapter_path)

model.eval()

#============================================================================

messages = [
    {
        "role":"user",
        "content":"what is dynamically typed language ?"
    }
]

inputs = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_tensors = "pt"
)

# print(inputs)
# print(inputs["input_ids"])

input_ids = inputs["input_ids"]

input_ids = input_ids.to(device)

# print("Input shape::", input_ids.shape)

# Generate Response : 

with torch.no_grad():
    outputs = model.generate(
        input_ids=input_ids,
        max_new_tokens=100,
        do_sample=False,
        pad_token_id=tokenizer.eos_token_id
    )

# print(outputs)
# print('###'*10)

generate_tokens = outputs[0][input_ids.shape[-1]:]

response = tokenizer.decode(
    generate_tokens,
    skip_special_tokens=True
)

print("Generated Response :\n", response)