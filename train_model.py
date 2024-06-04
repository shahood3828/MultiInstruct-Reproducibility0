from transformers import OFAForConditionalGeneration, OFATokenizer, Trainer, TrainingArguments
from datasets import load_dataset

# Load tokenizer and model
tokenizer = OFATokenizer.from_pretrained("OFA")
model = OFAForConditionalGeneration.from_pretrained("OFA")

# Load dataset
dataset = load_dataset('path/to/multi_instruct')
train_dataset = dataset['train']
eval_dataset = dataset['eval']

# Define training arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
)

# Train the model
trainer.train()
from transformers import OFAForConditionalGeneration, OFATokenizer, Trainer, TrainingArguments
from datasets import load_dataset

# Load tokenizer and model
tokenizer = OFATokenizer.from_pretrained("OFA")
model = OFAForConditionalGeneration.from_pretrained("OFA")

# Load dataset
dataset = load_dataset('path/to/multi_instruct')
train_dataset = dataset['train']
eval_dataset = dataset['eval']

# Define training arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
)

# Train the model
trainer.train()
