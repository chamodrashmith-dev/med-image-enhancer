import cv2
import numpy as np

def load_image(uploaded_file):
    """Load uploaded image as grayscale"""
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)
    return image
