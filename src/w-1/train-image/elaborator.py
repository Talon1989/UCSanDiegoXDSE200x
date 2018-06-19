import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
import imageio
from skimage import data


class ImageElaborator:

    def __init__(self, photo_data):
        assert isinstance(photo_data, imageio.core.util.Image)
        self.photo_data = photo_data

    def print_image(self):
        plt.figure(figsize=(15, 15))
        plt.imshow(self.photo_data)
        plt.show()

    def negative(self):
        photo = self.photo_data[:]
        photo = 255 - photo
        plt.figure(figsize=(15, 15))
        plt.imshow(photo)
        plt.show()

    def circle(self):
        photo = self.photo_data[:]
        rows, cols, layers = photo.shape
        center_row, center_col = rows / 2, cols / 2
        radius = center_row ** 2
        X_grid, Y_grid = np.ogrid[:rows, :cols]
        # print(X_grid.shape)
        # print(Y_grid.shape)
        # print(X_grid)
        distance_from_radius = (X_grid - center_row) ** 2 + (Y_grid - center_col) ** 2
        photo[distance_from_radius > radius] = 0
        plt.figure(figsize=(15,15))
        plt.imshow(photo)
        plt.show()

    def diagonal_line(self):
        photo = self.photo_data[:]
        pic_range = np.arange(photo.shape[0])
        for n in range(10):
            try:
                photo[pic_range, pic_range+n] = 255
                photo[pic_range, pic_range-n] = 255
            except IndexError:
                pass
        plt.figure(figsize=(10,10))
        plt.imshow(photo)
        plt.show()





elaboration = ImageElaborator(imageio.imread('mathias-zamecki.jpg'))
elaboration.circle()
elaboration.diagonal_line()

