from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np

image_file = '../kata_data/gears.PNG'
input_image = imread(image_file)
[nx, ny, nz] = np.shape(input_image)

r_img, g_img, b_img = input_image[:, :, 0], input_image[:, :, 1], input_image[:, :, 2]

gamma = 1.400  # a parameter
r_const, g_const, b_const = 0.2126, 0.7152, 0.0722  # weights for the RGB components respectively
grayscale_image = r_const * r_img ** gamma + g_const * g_img ** gamma + b_const * b_img ** gamma

plt.imshow(grayscale_image, cmap=plt.get_cmap('gray'))
plt.show()