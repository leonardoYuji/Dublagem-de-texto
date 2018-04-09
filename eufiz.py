import cv2 
import numpy as np

img = cv2.imread('square.png',cv2.IMREAD_GRAYSCALE)
sub = np.zeros((img.shape[0], img.shape[1]))
dois = np.zeros((img.shape[0], img.shape[1]))
for i in range(img.shape[0]):
        for o in range(img.shape[1]):
                if i != 1:
                        if o != 1:
                                imgi = img[i-1,o] + 0
                                imgo = img[i,o] + 0
                                media = imgo - imgi
                                if media <= 20:
                                        sub[i,o] = 0 			
                                if media > 20:
                                        sub[i,o] = 255
					sub[i-1,o] = 255	
for a in range(img.shape[0]):
        for b in range(img.shape[1]):
                if a != 1 and b!= 1:
                        
                        imga = img[a,b-1] + 0
                        imgb = img[a,b] + 0
                        m = imga - imgb
                        if m < 20:
                                dois[a,b] = 0   
                        if m > 20:
                                dois[a,b] = 255 
				dois[a,b-1] = 255                                
sobelxy = cv2.add(dois, sub)

im_floodfill = sobelxy.astype(np.uint8)


h, w = im_floodfill.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
cv2.floodFill(im_floodfill, mask, (0,0), 255);
                                        

cv2.imshow('ba',im_floodfill)
cv2.waitKey(0)
