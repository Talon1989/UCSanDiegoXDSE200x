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


def filterIntesity(photo):
    print("Shape of photo_data:", photo.shape)
    lowValueFilter = photo < 200  # returns True for each value of rbg of each pixel if it's less than 200
    print("Shape of low_value_filter:", lowValueFilter.shape)
    print(photo[1000,1000])
    plt.figure(figsize=(10,10))
    plt.imshow(photo)
    plt.show()
    photo[lowValueFilter] = 0  # set the low value pixel to black
    plt.figure(figsize=(10,10))
    plt.imshow(photo)
    plt.show()


def broadcastGrid():
    arr1 = np.array([[0], [1], [2]])  # rows, [0], [1], [2]
    arr2 = np.array([1, 2, 3])  # columns [1, 2, 3]
    print(arr1 + arr2)


def maskingImage(photo):
    assert isinstance(photo, imageio.core.util.Image)
    rows, cols, layers = photo.shape
    X, Y = np.ogrid[:rows, :cols]
    # print("X.shape = ", X.shape, " and Y.shape = ", Y.shape)
    # print('X=',X)
    # print('Y=',Y)
    centerRow, centerCol = rows / 2, cols / 2
    # print('centerRow=', centerRow)
    # print('centerCol=', centerCol)
    dist_from_center = (X - centerRow) ** 2 + (Y - centerCol) ** 2
    # print('dist_from_center=', dist_from_center)  # [3725 by 4797]
    radius = (rows / 2) ** 2
    # print("Radius = ", radius)
    circular_mask = (dist_from_center > radius)
    # print(circular_mask)
    # print(circular_mask[1500:1700, 2000:2200])
    photo[circular_mask] = 0

    halfUpper = X < centerRow
    half_upper_mask = np.logical_and(halfUpper, circular_mask)
    photo[half_upper_mask] = 200

    plt.figure(figsize=(15,15))
    plt.imshow(photo)
    plt.show()


def highLightReds(photo):
    assert isinstance(photo, imageio.core.util.Image)
    red_mask = photo[:, :, 0] < 150  # True for all r values in photo, lower than 150
    photo[red_mask] = 0
    plt.figure(figsize=(15,15))
    plt.imshow(photo)
    plt.show()


def rgbMask(photo):
    assert isinstance(photo, imageio.core.util.Image)
    red_mask = photo[:, :, 0] < 150
    green_mask = photo[:, :, 1] > 100
    blue_mask = photo[:, :, 2] < 100
    final_mask = np.logical_and(red_mask, green_mask, blue_mask)
    photo[final_mask] = 0
    plt.figure(figsize=(15,15))
    plt.imshow(photo)
    plt.show()




photo_data = imageio.imread('img/sd-3layers.jpg')
rgbMask(photo_data)





