# -*- coding: utf-8 -*-


import pytesseract as ocr
import numpy as np
import cv2
from PIL import Image
import os
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.blur(gray,(1,1))
    sobelx64 = cv2.Sobel(blur,cv2.CV_64F,1,0,ksize=1)
    sobely64 = cv2.Sobel(blur,cv2.CV_64F,0,1,ksize=1)
	
    sobelx = np.uint8(np.absolute(sobelx64))
    sobely = np.uint8(np.absolute(sobely64))

    add = cv2.add(sobelx,sobely)
    # Display the resulting frame
    cv2.imshow('frame',add)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
