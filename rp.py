import cv2
import numpy as np

img = cv2.imread('img.jpg')
img2 = cv2.imread('imgo.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

diferenca = cv2.subtract(gray, gray2)
diferenca[diferenca > 0] = 255
kernel = np.ones((4,4), np.uint8)
erode = cv2.erode(diferenca, kernel, iterations = 2)

cv2.imshow('deteccao',erode)
cv2.waitKey(0)
