
import cv2
import numpy
# Load an color image in grayscale
imagem = cv2.imread('oi.jpg')
for i in range(imagem.shape[0]):
	for o in range(imagem.shape[1]):
		print imagem[i,o]



