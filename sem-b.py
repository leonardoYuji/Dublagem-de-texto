import cv2
import numpy as np

image = cv2.imread('oi.jpg')

r = image.copy()
r[:, :, 0] = 0


cv2.imshow('oi', r)

cv2.waitKey(0)



