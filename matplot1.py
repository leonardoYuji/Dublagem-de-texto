import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem = cv2.imread('lena.png')
largura = imagem.shape[0]
altura = imagem.shape[1]

nImage = np.zeros((altura, largura))



for i in range(largura):
    for o in range(altura):
        (b, g, r) = imagem[i, o]
        blue = b + 0
        green = g + 0
        red = r + 0
        media = (blue + green + red)/3
	imagem.itemset((i,o,0),media)
	imagem.itemset((i, o, 1),media)
	imagem.itemset((i, o, 2),media)
	if media<127:
            nImage[-i,-o] = 0
        else :
            nImagem[-i,-o] = 255
cv2.imshow('dpoisajd',imagem)
cv2.imwrite('imagem.png',imagem)
cv2.waitKey(0)

plt.imshow(nImage, 'gray'),plt.title ( 'ORIGINAL' )
plt.show()



