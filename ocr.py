import easyocr
import numpy as np
from PIL import Image

# Load the OCR model only once
reader = easyocr.Reader(['en'], gpu=False)

def extract_text(image):
    """
    Extract text from a PIL Image using EasyOCR.
    Returns a formatted string.
    """

    # Convert PIL image to NumPy array
    img = np.array(image)

    # Perform OCR
    results = reader.readtext(img)

    if len(results) == 0:
        return "No text detected."

    text = []

    for result in results:
        detected_text = result[1]
        confidence = result[2]

        text.append(
            f"{detected_text}   (Confidence: {confidence:.2f})"
        )

    return "\n".join(text)
