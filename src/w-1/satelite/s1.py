import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
import imageio
from skimage import data


def testing():
    photo_data = misc.imread('img/sd-3layers.jpg')
    # photo_data = imageio.imread('img/sd-3layers.jpg')
    print(type(photo_data))
    # plt.figure(figsize=(15,15))
    # plt.imshow(photo_data)
    # plt.show()

    print(photo_data.shape)  # y, x, layers(rgb = 3)
    print(photo_data.min(), photo_data.max())
    print('at pixel 150,250  3 color values:', photo_data[150, 250])  # 17, 35, 255  this has a lot of blue
    print('rgb b value of above:', photo_data[150, 250, 2])
    photo_data[150, 250] = 0  # set the pixel to 0,0,0 = black
    photo_data[1500] = 255, 255, 255  # set the line at y=1500 to white
    photo_data[200:800, :, 1] = 255  # set all linea between 200 and 800px to g (rgb) value of 255 = max
    photo_data[:, 1900:1950] = 0  # set all columns betw 1900 to 1950 to black
    plt.figure(figsize=(10, 10))
    plt.imshow(photo_data)
    plt.show()


def makeWhiteDiagonal(photo):
    rowsRange = np.arange(len(photo))
    colsRange = rowsRange
    photo[rowsRange, colsRange] = 255
    # photo[:,:] = 255  # to make it all white
    plt.figure(figsize=(10, 10))
    plt.imshow(photo)
    plt.show()


photo_data = imageio.imread('img/sd-3layers.jpg')
print("Shape of photo_data:", photo_data.shape)
lowValueFilter = photo_data < 200  # returns True for each value of rbg of each pixel if it's less than 200
print("Shape of low_value_filter:", lowValueFilter.shape)
print(photo_data[1000,1000])
# plt.figure(figsize=(10,10))
# plt.imshow(photo_data)
# plt.show()
# photo_data[lowValueFilter] = 0  # set the low value pixel to black
# plt.figure(figsize=(10,10))
# plt.imshow(photo_data)
# plt.show()
makeWhiteDiagonal(photo_data)






