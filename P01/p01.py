# conversao de imagem para tons de cinza

import cv2

im = cv2.imread('senko.jpeg')
img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imwrite('sekko_gray.png', img)
print('..|imagem salva com sucesso')
