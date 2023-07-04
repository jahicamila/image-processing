import numpy as np
import cv2 as cv
import os

  path = os.path.join('..', os.getcwd(), 'images', 'rocket.jpg')
  img = cv.imread(path)
  cv.imshow('Original', img)

    # Gaussian filter
    gaussian = cv.GaussianBlur(img, (5,5), 0)
    cv.imshow('Gaussian blur', gaussian)

    # Median filter
    median = cv.medianBlur(img, 3)
    cv.imshow('Median', median)
  
    # Avergaing filter
    average = cv.blur(img, (3,3))
    cv.imshow('Average blur', average)

    cv.waitKey(0)
