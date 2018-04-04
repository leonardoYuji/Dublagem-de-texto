import cv2

imagem = cv2.imread('lena.png')

k = imagem.shape[0]
kk = k / 2 - 0

vermelho = [255,0,255]
(X, Y) = (imagem.shape[1] //2-25, imagem.shape[0] //2-50)
for raio in range(0, 16, 15):
    cv2.circle(imagem, (X, Y), raio, vermelho, 7)
cv2.rectangle(imagem,( kk,0) , (imagem.shape[0]//2, imagem.shape[1]//4), vermelho, 7)
(z, w) = (imagem.shape[1] //2+25, imagem.shape[0] //2-50)
for raio in range(0, 16, 15):
    cv2.circle(imagem, (z, w), raio, vermelho, 7)
    
fonte = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagem,'My penis',(0,imagem.shape[0]//2), fonte,1.8,(255,255,255),2,cv2.CV_AA)
    
cv2.imshow("Desenhando sobre a imagem", imagem)
cv2.waitKey(0)
