import pytesseract as ocr
import numpy as np
import cv2
from PIL import Image


imagem = Image.open('print.png').convert('RGB')


npimagem = np.asarray(imagem).astype(np.uint8)  



im = cv2.cvtColor(npimagem, cv2.COLOR_RGB2GRAY) 


ret, thresh = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) 


binimagem = Image.fromarray(thresh) 


phrase = ocr.image_to_string(binimagem, lang='eng')

print(phrase) 
cv2.imshow('img',thresh)
cv2.waitKey(0)
