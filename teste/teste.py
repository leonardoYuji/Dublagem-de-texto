import numpy as np
import cv2 
img = cv2.imread('../imgo.jpg',0)
ret,thresh = cv2.threshold(img,127,255,0)
im2,contours,hierarchy = cv2.findContours(thresh, 1, 2)
print img2
print contours
print hierarchy
