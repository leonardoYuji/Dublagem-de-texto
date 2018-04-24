# -*- coding: utf-8 -*-


import pytesseract as ocr
import time 
import numpy as np
import cv2
from PIL import Image
import os
################## 
DELAY = 0.02 
USE_CAM = 1 
IS_FOUND = 0 
 
MORPH = 7 
CANNY = 250 
################## 
# 420x600 oranı 105mmx150mm gerçek boyuttaki kağıt için 
_width  = 600.0 
_height = 420.0 
_margin = 0.0 
################## 
if USE_CAM: video_capture = cv2.VideoCapture(0) 
 
corners = np.array( 
  [ 
    [[      _margin, _margin       ]], 
    [[       _margin, _height + _margin  ]], 
    [[ _width + _margin, _height + _margin  ]], 
    [[ _width + _margin, _margin       ]], 
  ] 
) 
 
pts_dst = np.array( corners, np.float32 ) 
while(True):
   if USE_CAM : 
    ret, rgb = video_capture.read() 
   else : 
    ret = 1 
    rgb = cv2.imread( "opencv.jpg", 0 ) 
 
   if  ret:

	    gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
	    blur = cv2.blur(gray,(1,1))
	    sobelx64 = cv2.Sobel(blur,cv2.CV_64F,1,0,ksize=1)
	    sobely64 = cv2.Sobel(blur,cv2.CV_64F,0,1,ksize=1)
	
	    sobelx = np.uint8(np.absolute(sobelx64))
	    sobely = np.uint8(np.absolute(sobely64))
	    add = cv2.add(sobelx,sobely)
	    kernel = cv2.getStructuringElement( cv2.MORPH_RECT, ( MORPH, MORPH ) )
	    closed = cv2.morphologyEx( add, cv2.MORPH_CLOSE, kernel )
	    contours,hierarchy = cv2.findContours(closed, 1, 2)	
	    for cont in contours:
		if cv2.contourArea( cont ) > 5000 :

		    arc_len = cv2.arcLength( cont, True )
		    approx = cv2.approxPolyDP(cont,0.01*cv2.arcLength(cont,True),True)
		    if len(approx) == 4:
			print "oi"

cap.release()
cv2.destroyAllWindows()


