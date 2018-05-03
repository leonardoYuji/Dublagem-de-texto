import cv2
import numpy as np

img = cv2.imread("cap.png")
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
for thresh in [cv2.THRESH_BINARY]:
	(_, bw) = cv2.threshold(gray, 127, 255, thresh | cv2.THRESH_OTSU) 
cv2.imshow('ola',bw)
cv2.waitKey(0)
