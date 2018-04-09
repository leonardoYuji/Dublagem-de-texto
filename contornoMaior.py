import cv2
import numpy as np

img  = cv2.imread('square.png',0)
ret, thresh = cv2.threshold(img, 127, 255, 0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]
m = cv2.moments(cnt)
cx = int(m['m10']/m['m00'])
cy = int(m['m01']/m['m00'])
area = cv2.contourArea(cnt)
perinetro = cv2.arcLength(cnt, True)


cv2.imshow("t",thresh)
cv2.waitKey(0)
