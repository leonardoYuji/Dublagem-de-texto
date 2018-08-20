import numpy as np
import cv2
img = cv2.imread("a.png")
sub = np.zeros((img.shape[0], img.shape[1]))
dois = np.zeros((img.shape[0], img.shape[1]))
vetx = np.zeros((img.shape[0], img.shape[1]))
vety = np.zeros((img.shape[0], img.shape[1]))
z = 0
imgg = 0
for i in range(img.shape[0]):
        for o in range(img.shape[1]):
                if i != 1:
                        if o != 1:
                                imgi = img[i-1,o,0] + 0
                                imgo = img[i,o,0] + 0
                                media = imgo - imgi + 0
				
				if media <= 20:
					sub[i,o] = 0
				if media > 20:
					sub[i,o] = 255 
for a in range(img.shape[0]):
        for b in range(img.shape[1]):
                if a != 1 and b!= 1:
                        
                        imga = img[a,b-1,0] + 0
                        imgb = img[a,b,0] + 0
                        m = imga - imgb
                        if m < 20:
                                dois[a,b] = 0   
                        if m > 20:
                                dois[a,b] = 255 
				dois[a,b-1] = 255                                
sobelxy = cv2.add(dois, sub)
							
for kkk  in range(sobelxy.shape[0]):
	for uia in range(sobelxy.shape[1]):
		imgg = sobelxy[kkk, uia] + 0
		if imgg == 0:
			
cv2.imshow("img.jpg",img)
cv2.waitKey(0)
