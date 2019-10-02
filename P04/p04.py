'''
A rotação de uma imagem para um ângulo theta é obtida pela matriz de transformação da forma

M = | cos theta     -sin theta  |
    | sin theta      cos theta  |

Mas o OpenCV fornece rotação em escala com centro de rotação ajustável 
para que você possa girar em qualquer local que você preferir. 
A matriz de transformação modificada é dada por


M = |  alpha     beta    (1- \ alpha) . center.x - beta . center.y  |
    | -beta      alpha   beta . center.x + (1 - alpha) . center.y   |

Onde:
    alpha = scale . cos theta
    beta  = scale . sin theta

Para encontrar essa matriz de transformação, o OpenCV fornece uma função, 
cv2.getRotationMatrix2D. Veja abaixo o exemplo que gira a imagem em 90 graus em 
relação ao centro, sem redimensionamento.
'''
import cv2

img = cv2.imread('lenna.png',0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),180,1)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()