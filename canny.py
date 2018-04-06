import cv2
import numpy
from matplotlib import pyplot as plt

img = cv2.imread('imgo.jpg',0)
canny = cv2.Canny(img,200,100)
laplaciano = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1,0, ksize = 5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0,1, ksize = 5)

sobelxy = cv2.add(sobelx,sobely)
sobelxy[sobelxy < 255 ] = 0

plt.subplot(121),plt.imshow(img,cmap = 'gray') 
plt.subplot(122),plt.imshow(sobelxy,cmap = 'gray'), plt.savefig('novo.png')
plt.show()
