import cv2 as cv
import numpy as np
import os 

path = os.path.join('..', os.getcwd(), 'images', 'squirrel.jpg')
img = cv.imread(path)
cv.imshow('Original', img)

# Convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv.GaussianBlur(gray, (3, 3), 0)

# Perform Canny edge detection
edges = cv.Canny(blurred, 150, 175)

# Create a mask of the edges
mask = cv.bitwise_and(img, img, mask=edges)
# Combine the mask with the original image to create a sharpened result
sharpened = cv.addWeighted(img, 1.5, mask, -0.5, 0)

# Display the sharpened images
cv.imshow('Sharpened', sharpened)
cv.waitKey(0)
cv.destroyAllWindows()
