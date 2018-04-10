import cv2
import numpy as np

img = cv2.imread('square.png',0)
matris = np.zeros((img.shape[0]+1,img.shape[1]+1))
outro = np.zeros((img.shape[0]+1,img.shape[1]+1))
#for i in range(img.shape[0]):
#	for o in range(img.shape[1]):
#		outro[i,o] = img[i,o]
#		if img[i,o] == outro[i+1,o]:
#			matris[i,o] = 255
#		if img[i,o] != outro[i,o+1]:
o = 0
i = 0
for i in range(img.shape[0]):
	for o in range(img.shape[1]):
		outro[i,o] = img[i,o]
		
cv2.imshow('legal',matris)
cv2.waitKey(0)
