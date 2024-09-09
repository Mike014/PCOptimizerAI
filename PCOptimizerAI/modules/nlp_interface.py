import os
from transformers import pipeline

os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

class NLPQuestionAnswering:
    def __init__(self, model_path="PCOptimizerAI/modules/models/distilbert-base-cased-distilled-squad"):
        """
        Initializes the NLPQuestionAnswering class by setting up the question-answering pipeline.
        
        Parameters:
        model_path (str): The local path to the model to be used for the question-answering pipeline.
        """
        self.qa_pipeline = pipeline("question-answering", model=model_path, tokenizer=model_path)

    def get_response(self, question, context):
        """
        Retrieves an answer to the given question based on the provided context.

        Parameters:
        question (str): The question to be answered.
        context (str): The context from which to extract the answer.

        Returns:
        str: The answer extracted from the context based on the question.
        """
        result = self.qa_pipeline(question=question, context=context, clean_up_tokenization_spaces=True)
        return result['answer']

# Example usage
if __name__ == "__main__":
    nlp_qa = NLPQuestionAnswering(model_path="PCOptimizerAI/modules/models/distilbert-base-cased-distilled-squad")
    question = "What is the capital of France?"
    context = "France's capital is Paris."
    print(nlp_qa.get_response(question, context))
