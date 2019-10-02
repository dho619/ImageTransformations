'''
A translacao é a mudança da localização do objeto. 
Se você conhece a mudança na direção (x, y), seja (t_x, t_y), 
é possível criar a matriz de transformação M da seguinte maneira:

M = | 1  0  tx |
    | 0  1  ty |
    
Você pode transformá-lo em uma matriz Numpy do tipo np.float32 e passá-lo para 
a função cv2.warpAffine(). 

O terceiro argumento da função cv2.warpAffine () é o tamanho da imagem de saída, 
que deve estar na forma de (largura, altura). Lembre-se de largura = número de colunas 
e altura = número de linhas.
'''

import cv2
import numpy as np

img = cv2.imread('lenna.png', 0)
rows, cols = img.shape

M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()