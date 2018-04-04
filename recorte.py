import cv2
import numpy as np
img  =  cv2.imread('gintoki.png')
recorte = cv2.imread('recorte.jpg')

img[0:220,0:216] = recorte

cv2.imshow('o',img)

cv2.waitKey(0)
