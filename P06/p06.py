'''
Para transformação de perspectiva, você precisa de uma matriz de transformação 3x3. 
As linhas retas permanecerão retas, mesmo após a transformação. Para encontrar essa 
matriz de transformação, você precisa de 4 pontos na imagem de entrada e pontos 
correspondentes na imagem de saída. Entre esses 4 pontos, 3 deles não devem ser 
colineares. Em seguida, a matriz de transformação pode ser encontrada pela função 
cv2.getPerspectiveTransform. Em seguida, aplique cv2.warpPerspective com essa 
matriz de transformação 3x3.
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lenna.png')
rows,cols,ch = img.shape

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()