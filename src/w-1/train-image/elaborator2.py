import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
import imageio
from skimage import data


pic = imageio.imread('mathias-zamecki.jpg')

# d = np.arange(pic.shape[0])
# pic[d, d] = 255
for n in range(pic.shape[0]):
    pic[n,n] = 255

plt.figure(figsize=(10,10))
plt.imshow(pic)
plt.show()


