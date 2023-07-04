import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread(r"C:\Users\User\Desktop\vjeverica.jpg")
cv2.imshow('Original', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sobel
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
combined_sobel = cv2.bitwise_or(sobelx, sobely)
cv2.imshow('Sobelx', sobelx)
cv2.imshow('Sobely', sobely)
cv2.imshow('Combined Sobel', combined_sobel)
cv2.waitKey(0)
