import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('0001.png',0)
w, l = img.shape
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations = 1)
plt.imshow(erosion, cmap = 'gray', interpolation = 'bicubic')
plt.show()
