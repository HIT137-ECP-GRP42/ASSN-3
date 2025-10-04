from transformers import pipeline
from PIL import Image


class BaseModel:
   
    def __init__(self, model_name: str, task: str):
        self.model_name = model_name
        self.task = task
        self.model = pipeline(task, model=model_name)  # auto-fetches on first use

    def run(self, input_data):
        
        raise NotImplementedError("Subclass must override run()")

class TextModel(BaseModel):
    def __init__(self, model_name: str):
        super().__init__(model_name, "text-generation")
    def run(self, prompt: str, max_new_tokens: int = 30):
        return self.model(prompt, max_new_tokens=max_new_tokens)




class ImageClassificationModel(BaseModel):
    def __init__(self, model_name: str):
        super().__init__(model_name, "image-classification")

    def run(self, pil_image: Image.Image, top_k: int = 5):
        return self.model(images=pil_image, top_k=top_k)

TEXT_MODEL_NAME = "sshleifer/tiny-gpt2"  
text_model = TextModel(TEXT_MODEL_NAME)


IMAGE_MODEL_NAME = "apple/mobilevit-xx-small"

image_model = ImageClassificationModel(
    IMAGE_MODEL_NAME
)