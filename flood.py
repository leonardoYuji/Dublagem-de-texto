import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('square.png',0)

#copy = cv2.threshold(img, 60, 255, cv2.THRESH_BINARY)[1]
copy = img.copy()

cnts = cv2.findContours(copy, cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)



cnts = cnts[0]

for c in cnts:
	# compute the center of the contour
	M = cv2.moments(c)
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])
 	print cX, cY
	# draw the contour and center of the shape on the image
	cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
	cv2.putText(img, "square quadrado", (2*cX/3, 3*cY/5),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
 


# show the image
cv2.imshow("Image", img)
cv2.waitKey(0)
