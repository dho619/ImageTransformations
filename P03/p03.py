'''
Translação - Mudança de posição da imagem
'''

import cv2
import numpy as np

img = cv2.imread('senko.jpeg', 0)
rows, cols = img.shape

M = np.float32([[1,0,200],[0,1,500]])
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imwrite('senko_Translacao.png', dst)
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
print('..|imagem salva com sucesso')
