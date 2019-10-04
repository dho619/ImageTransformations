'''
Transformação de perspectiva
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('senko.jpeg')
rows,cols,ch = img.shape

pts1 = np.float32([[306,665],[618,652],[278,987],[639,990]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(300,300))
cv2.imwrite('senko_TransformacaoDePerspectiva.png', dst)

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
print('..|imagem salva com sucesso')
