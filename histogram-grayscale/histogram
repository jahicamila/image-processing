import numpy as np
import matplotlib.pyplot as plt
import cv2

path = os.path.join('..', os.getcwd(), 'images', 'flowers.jpg')
img = cv.imread(path)
cv.imshow('Original', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', gray)

histr = cv2.calcHist([gray], [0], None, [256], [0,256])
plt.figure()
plt.xlabel('Bins')
plt.ylabel('Nummber of pixels')
plt.plot(histr)
plt.show()

cv2.waitKey(0)
