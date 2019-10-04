'''
conversao de imagem para tons de cinza
'''

import cv2

im = cv2.imread('senko.jpeg')
img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imwrite('senko_gray.png', img)
cv2.imshow('imagem', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print('..|imagem salva com sucesso')
