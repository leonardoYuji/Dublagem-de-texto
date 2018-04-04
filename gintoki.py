import cv2

img = cv2.imread('gintoki.png')
recorte = cv2.imread('recorte.jpg')
img[100:320,100:316] = recorte

cv2.imshow('modificada',img)
cv2.imwrite('gintoki2.png',img)
cv2.waitKey(0)
