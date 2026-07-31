import easyocr
import numpy as np
from PIL import Image

reader = easyocr.Reader(['en'], gpu=False)

def locate_date_region(image):

    img = np.array(image)

    results = reader.readtext(img)

    for r in results:

        box = r[0]

        text = r[1].upper()

        if "MFG" in text or "EXP" in text or "PKD" in text:

            x = int(min(p[0] for p in box))
            y = int(min(p[1] for p in box))

            w = int(max(p[0] for p in box))
            h = int(max(p[1] for p in box))

            pad = 30

            crop = img[
                max(0,y-pad):h+pad,
                max(0,x-pad):w+pad
            ]

            return Image.fromarray(crop)

    return image
