import numpy as np

an_array = np.array([1,2,3,4])
# print(an_array)

rank2 = np.array([[11,22,33], [21,22,23], [31,32,33], [41,42,43]])
print(rank2)
print('Shape is 4 rows, 3 columns:', rank2.shape)
print('Accessing element [0,2]:', rank2[0,2])


zeroes = np.zeros((2,2)) # 2 by 2 array of 0 values
print('zeroes:', zeroes)