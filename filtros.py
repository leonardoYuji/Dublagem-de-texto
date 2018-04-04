import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('oi.jpg')

median = cv2.medianBlur(img,5)
gaussian = cv2.GaussianBlur(img,(5,5),0)
bilateral = cv2.bilateralFilter(img,40,75,75)

cv2.imshow("mediana",median)
cv2.imshow('gaussiana',gaussian)
cv2.imshow("bilateral",bilateral)
cv2.imshow("img",img)
cv2.waitKey(0)
