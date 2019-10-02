'''
Na transformação afim, todas as linhas paralelas na imagem original ainda serão 
paralelas na imagem de saída. Para encontrar a matriz de transformação, precisamos 
de três pontos da imagem de entrada e seus locais correspondentes na imagem de saída. 
Então cv2.getAffineTransform criará uma matriz 2x3 que será passada para cv2.warpAffine.
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lenna.png')
rows,cols,ch = img.shape

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()