import cv2
import numpy as np
# read sample images
img1 = cv2.imread("img.jpg")
img2 = cv2.imread("imgo.jpg")
img3 = cv2.imread("mask.jpg")
 
# convert the images for gray scale
imgray1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
imgray2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
imgray3 = cv2.cvtColor(img3, cv2.COLOR_RGB2GRAY)
 
# kernel to use for erode imagem
kernel = np.ones((2, 2), np.uint8)
 
#find the diference betwen img1 and img2
diference = cv2.subtract(imgray1, imgray2)
 
erode = cv2.erode(diference, kernel, iterations=2)
erode1 = cv2.erode(imgray3, kernel, iterations=2)
 
#read the counter sample to compare
im1, cont1, hier1 = cv2.findContours(erode1, cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_NONE)
 
#find contours
im2, cont, hier = cv2.findContours(erode, cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_NONE)
 
cv2.imshow('DETECCAO', erode)
cv2.waitKey(0)
