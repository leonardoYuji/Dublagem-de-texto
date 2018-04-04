import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.png')
nImage = np.zeros((img.shape[0],img.shape[1]))
result = np.zeros((img.shape[0]-1,img.shape[1]-1))
print img.shape
for i in range(img.shape[0]-1):
	for o in range(img.shape[1]-1):

		blue = img.item(i,o,0)
		green = img.item(i,o,1)
		red = img.item(i,o,2)
		media = (blue + green + red)/3
		nImage[i,o] = media
		fltMedia = (nImage[i-1,o-1] + nImage[i,o-1] + nImage[i+1,o-1] + nImage[i-1,o] + nImage[i,o] + nImage[i+1,o] + nImage[i-1,o+1] + nImage[i,o+1] + nImage[i+1,o+1] + nImage[i-1,o]) /9	
		result[i,o] = fltMedia 	

cv2.imshow('original',img)
cv2.waitKey(0)
plt.imshow(result,'gray')
plt.title('media')
plt.show()
