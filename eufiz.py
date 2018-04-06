import cv2 
import numpy as np

img = cv2.imread('oi.jpg',0)
sub = np.zeros((img.shape[0], img.shape[1]))
for i in range(img.shape[0]):
	for o in range(img.shape[1]):
		if i != 1:
			if o != 1:
				imgi = img[i-1,o] + 0
				imgo = img[i,o] + 0
				media = imgo - imgi
				if media < 20:
					sub[i,o] = 0	
				if media > 20:
					sub[i,o] = 255

					
cv2.imshow('eba',sub)
cv2.waitKey(0)
