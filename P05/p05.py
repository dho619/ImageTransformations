'''
Transformação afim
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('senko.jpeg')
rows,cols,ch = img.shape

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imwrite('senko_TransformacaoDeAfim.png', dst)

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
print('..|imagem salva com sucesso')
