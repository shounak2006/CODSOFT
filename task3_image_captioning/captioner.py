from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

class ImageCaptioner:
    """
    A class that leverages a pre-trained Vision-Transformer model
    to generate natural language captions for input images.
    """
    def __init__(self):
        print("Loading AI Model (Salesforce/blip-image-captioning-base)...")
        # Initialize the BLIP processor and model explicitly instead of via pipeline
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        print("AI Model successfully loaded!")

    def generate_caption(self, image_stream):
        """
        Takes a file stream (or path), processes it via Pillow,
        and returns the AI-generated caption.
        """
        try:
            # Convert raw bytes to a PIL object which the transformer requires
            image = Image.open(image_stream)
            
            # If the image has an alpha channel (like PNGs), convert to RGB so the model doesn't crash
            if image.mode != "RGB":
                image = image.convert(mode="RGB")
                
            # Perform inference
            inputs = self.processor(image, return_tensors="pt")
            out = self.model.generate(**inputs)
            caption = self.processor.decode(out[0], skip_special_tokens=True)
            
            return caption.capitalize() + "."
        except Exception as e:
            return f"Error: Could not process image. ({str(e)})"
