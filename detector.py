import cv2
import numpy as np
from PIL import Image

def analyze_image(image):

    # Convert PIL image to OpenCV format
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # ---------- Image Quality ----------
    brightness = np.mean(gray)

    contrast = np.std(gray)

    # ---------- Edge Detection ----------
    edges = cv2.Canny(gray, 100, 200)

    edge_density = np.sum(edges > 0) / edges.size

    # ---------- Noise Estimation ----------
    laplacian = cv2.Laplacian(gray, cv2.CV_64F).var()

    # ---------- Scratch / Tamper Estimation ----------
    _, thresh = cv2.threshold(gray, 210, 255, cv2.THRESH_BINARY)

    white_ratio = np.sum(thresh == 255) / thresh.size

    # ---------- Risk Score ----------
    risk = 20

    reasons = []

    if brightness > 220:
        risk += 15
        reasons.append("Over-bright print")

    if contrast < 30:
        risk += 15
        reasons.append("Low contrast")

    if edge_density > 0.18:
        risk += 20
        reasons.append("Irregular edge pattern")

    if laplacian < 80:
        risk += 20
        reasons.append("Blurred printing")

    if white_ratio > 0.25:
        risk += 20
        reasons.append("Possible erased region")

    risk = min(risk, 100)

    # ---------- Final Status ----------
    if risk >= 75:
        status = "HIGH RISK"

    elif risk >= 45:
        status = "MEDIUM RISK"

    else:
        status = "LOW RISK"

    if len(reasons) == 0:
        reasons.append("No major anomaly detected")

    return {

        "risk": risk,

        "status": status,

        "reason": ", ".join(reasons),

        "brightness": round(brightness,2),

        "contrast": round(contrast,2),

        "edge_density": round(edge_density,3),

        "sharpness": round(laplacian,2),

        "surface_damage": round(white_ratio,3)

    }
