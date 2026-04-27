from transformers import pipeline
from PIL import Image

class ImageCaptioner:
    """
    A class that leverages a pre-trained Vision-Transformer model
    to generate natural language captions for input images.
    """
    def __init__(self):
        print("Loading AI Model (Salesforce/blip-image-captioning-base)...")
        # BLIP uses a Vision Transformer (ViT) architecture combined with a text decoder
        self.captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
        print("AI Model successfully loaded!")

    def generate_caption(self, image_stream):
        """
        Takes a file stream (or path), processes it via Pillow,
        and returns the AI-generated caption.
        """
        try:
            # Convert raw bytes to a PIL object which the transformer pipeline requires
            image = Image.open(image_stream)
            
            # If the image has an alpha channel (like PNGs), convert to RGB so the model doesn't crash
            if image.mode != "RGB":
                image = image.convert(mode="RGB")
                
            # Perform inference
            result = self.captioner(image)
            
            # The pipeline outputs a list: [{'generated_text': 'caption'}]
            return result[0]['generated_text'].capitalize() + "."
        except Exception as e:
            return f"Error: Could not process image. ({str(e)})"
