from matplotlib.image import imread
import cv2
import matplotlib.pyplot as plt
import numpy as np

input = cv2.imread('/home/allen/data/gears.PNG')
rows, cols, channels = input.shape
img = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
Gx = np.array([[1.0, 0.0, -1.0], [2.0, 0.0, -2.0], [1.0, 0.0, -1.0]])
Gy = np.array([[1.0, 2.0, 1.0], [0.0, 0.0, 0.0], [-1.0, -2.0, -1.0]])


out = np.zeros(shape=(rows,cols))
for r in range(rows-2):
    for c in range(cols-2):
        #pixel = []
        gx = np.sum(Gx @ img[r:r+3, c:c+3])
        gy = np.sum(Gy @ img[r:r+3, c:c+3])
        out[r+1, c+1] = np.sqrt(gx **2 + gy **2)

imgplot = plt.imshow(out, cmap=plt.get_cmap('gray'))
plt.show()