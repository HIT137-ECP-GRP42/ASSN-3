from transformers import pipeline

class BaseModel:
   
    def __init__(self, model_name: str, task: str):
        self.model_name = model_name
        self.task = task
        self.model = pipeline(task, model=model_name)

    def run(self, input_data):
        
        raise NotImplementedError("Subclass must override run()")

class TextClassificationModel(BaseModel):
  
    def run(self, input_data):
        return self.model(input_data)

class ImageClassificationModel(BaseModel):
  
    def run(self, input_data):
        return self.model(images=input_data)

TEXT_MODEL_NAME = "nateraw/bert-tiny-sst2"  
text_model = TextClassificationModel(
    TEXT_MODEL_NAME,
    "text-classification"
)


IMAGE_MODEL_NAME = "apple/mobilevit-xx-small"

image_model = ImageClassificationModel(
    IMAGE_MODEL_NAME,
    "image-classification"
)