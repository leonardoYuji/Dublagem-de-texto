import cv2
import numpy
from matplotlib import pyplot as plt

img = cv2.imread('oi.jpg',0)
canny = cv2.Canny(img,200,100)
laplaciano = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1,0, ksize = 5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0,1, ksize = 5)

plt.subplot(321),plt.imshow(img,cmap = 'gray')
plt.subplot(322),plt.imshow(canny,cmap = 'gray')
plt.subplot(323),plt.imshow(laplaciano,cmap = 'gray')
plt.subplot(324),plt.imshow(sobelx,cmap = 'gray')
plt.subplot(325),plt.imshow(sobely,cmap = 'gray')
plt.show()
