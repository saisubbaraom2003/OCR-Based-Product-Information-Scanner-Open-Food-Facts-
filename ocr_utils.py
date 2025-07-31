import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np

def extract_text_from_image(image: Image.Image) -> str:
    # Convert to grayscale
    gray = image.convert("L")
    
    # Optional preprocessing for better OCR
    gray = gray.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(gray)
    gray = enhancer.enhance(2)

    # Run OCR
    text = pytesseract.image_to_string(gray)

    # Debug: print extracted text in terminal
    print("Extracted Text:", repr(text))

    # Check if any meaningful text was found
    if not text.strip():
        return "No readable text found. Please try another image."

    return text.strip()
