'''
Rotação de 90 graus em relação ao centro, sem redimensionamento.
'''
import cv2

img = cv2.imread('senko.jpeg',0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),180,1)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imwrite('senko_Rotacao.png', dst)
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
print('..|imagem salva com sucesso')
