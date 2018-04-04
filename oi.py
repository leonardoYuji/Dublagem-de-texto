import cv2

# Load an color image in grayscale
imagem = cv2.imread('oi.jpg')
i = 1
o = 1
while i != imagem.shape[0]:
    i = i + 1
    while o != imagem.shape[1]:
        o = o + 1
        print imagem



