import numpy as np
import matplotlib.pyplot as plt
import cv2

path = os.path.join('..', os.getcwd(), 'images', 'squirrel.jpg')
img = cv.imread(path)
cv.imshow('Original', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sobel
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
combined_sobel = cv2.bitwise_or(sobelx, sobely)
cv2.imshow('Sobelx', sobelx)
cv2.imshow('Sobely', sobely)
cv2.imshow('Combined Sobel', combined_sobel)
cv2.waitKey(0)
