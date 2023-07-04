import numpy as np
import matplotlib.pyplot as plt
import cv2

path = os.path.join('..', os.getcwd(), 'images', 'lamp.jpg')
img = cv.imread(path)
cv2.imshow('Original', img)

# Rotacija
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)
    rotMat = cv2.getRotationMatrix2D (rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv2.warpAffine (img, rotMat, dimensions)

rotated = rotate(img, 45)
cv2.imshow('Rotated', rotated)
cv2.waitKey(0)
