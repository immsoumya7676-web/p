import cv2
import numpy as np
from vision import locate_date_region

def advanced_analysis(image):

    crop = locate_date_region(image)

    img = np.array(crop)

    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    # Local Contrast

    contrast = np.std(gray)

    # Sharpness

    sharp = cv2.Laplacian(
        gray,
        cv2.CV_64F
    ).var()

    # Ink Density

    ink = np.mean(gray)

    # Edge Detection

    edge = cv2.Canny(gray,80,180)

    edge_density = np.sum(edge>0)/edge.size

    # Threshold

    _,th = cv2.threshold(
        gray,
        190,
        255,
        cv2.THRESH_BINARY
    )

    white = np.sum(th==255)/th.size

    risk = 15

    reasons=[]

    if contrast<28:
        risk+=20
        reasons.append("Low Print Contrast")

    if sharp<60:
        risk+=20
        reasons.append("Blurred Characters")

    if white>0.35:
        risk+=20
        reasons.append("Possible Erased Surface")

    if edge_density>0.18:
        risk+=20
        reasons.append("Irregular Print Edges")

    if ink>205:
        risk+=15
        reasons.append("Uneven Ink")

    risk=min(risk,100)

    if risk>70:
        status="HIGH RISK"

    elif risk>40:
        status="MEDIUM RISK"

    else:
        status="SAFE"

    return{

        "risk":risk,

        "status":status,

        "reason":",".join(reasons),

        "cropped_image":crop
    }
