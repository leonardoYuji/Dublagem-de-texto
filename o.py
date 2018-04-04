import cv2

# Load an color image in grayscale
img = cv2.imread('gintoki.png',0)


cv2.imshow('gintoki',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
