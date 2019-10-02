'''
Imagem Redimensionada
'''
import cv2
import numpy as np

img = cv2.imread('senko.jpeg')

height, width = img.shape[:2]
res = cv2.resize(img, (width//2, height//4), interpolation=cv2.INTER_CUBIC)
cv2.imwrite('sekko_Redimensionado.png', res)
cv2.imshow('imagem', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
