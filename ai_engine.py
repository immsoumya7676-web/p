from ocr import extract_information
from detector import analyze_image
from report import generate_report
from database import insert_record


class PackSecureAI:

    def __init__(self):
        pass

    def inspect(self, image, product_name="Unknown Product"):

        # OCR
        ocr_data = extract_information(image)

        # Computer Vision
        analysis = analyze_image(image)

        result = {}

        result.update(ocr_data)
        result.update(analysis)

        result["product"] = product_name

        # Generate Report
        pdf = generate_report(result)

        result["report"] = pdf

        # Save History
        insert_record(result)

        return result
