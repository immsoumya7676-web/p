from PIL import Image
import cv2
import numpy as np


def pil_to_cv(image):

    return cv2.cvtColor(
        np.array(image),
        cv2.COLOR_RGB2BGR
    )


def cv_to_pil(image):

    image = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2RGB
    )

    return Image.fromarray(image)


def resize_image(image,width=900):

    w,h=image.size

    ratio=width/w

    return image.resize(

        (width,int(h*ratio))

    )


def format_percentage(value):

    return f"{round(value,2)} %"
