import cv2

def denoise_image(image, ksize=5):
    """Apply Gaussian Blur with adjustable kernel size"""
    if ksize % 2 == 0:
        ksize += 1
    return cv2.GaussianBlur(image, (ksize, ksize), 0)

def enhance_contrast(image):
    """Histogram equalization"""
    return cv2.equalizeHist(image)

def detect_edges(image, low_thresh=100, high_thresh=200):
    """Canny edge detection with adjustable thresholds"""
    return cv2.Canny(image, low_thresh, high_thresh)
