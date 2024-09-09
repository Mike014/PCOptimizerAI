from transformers import AutoModelForQuestionAnswering, AutoTokenizer

model_name = "distilbert-base-cased-distilled-squad"
save_directory = "PCOptimizerAI/modules/models/distilbert-base-cased-distilled-squad"

model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

model.save_pretrained(save_directory)
tokenizer.save_pretrained(save_directory)

print(f"Modello scaricato e salvato in {save_directory}")
