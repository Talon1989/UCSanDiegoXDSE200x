import numpy as np


matrix = np.array([ [1,2,3], [11,22,33], [111,222,333] ], dtype=float)
print(matrix)
print(matrix[1,2])  # second row, third value = 33
print()

zeros = np.zeros( (3,3) )  # 3x3 array of zeros
print(zeros)

valueArray = np.full( (4,2), 9.0)  # 4x2 array of 9.0
print(valueArray)

print(valueArray.shape)  # returns the shape of the matrix
print()

sliceOfMatrix = matrix[:2, 1:3]  # slice of matrix, first and second rows, from 2 to 3 column
sliceOfMatrix2 = np.copy(matrix[:2, 1:3])  # same as above but a copy, so if modified doesn't change the original
sliceOfMatrix2[0,0] = 99
print(sliceOfMatrix2)
print(matrix)
print(matrix[:2, :])  # first 2 rows, all columns
print()

an_array = np.array([[11,12,13], [21,22,23], [31,32,33], [41,42,43]])
print(an_array)
rowIndices = np.arange(4)  # arrange values in a vector from 0 to n-1
colIndices = np.array([0,1,0,2])
for r,c in zip(rowIndices, colIndices):
    print('position:', r, ',', c, ' = ', an_array[r,c])
print('filt = ( (an_array > 20) & (an_array < 30)')
filt = ( (an_array > 20) & (an_array < 30) )
print(filt)
print(an_array[filt])
print()

print('above array an_array.dtype : ', an_array.dtype)
np.random.seed(0)
randM = np.random.randn(2, 5)  # generate a matrix 2 by 5 populated with random values
print(randM)
print('mean:', randM.mean())
print('mean of the first row based on columns:', randM.mean(axis=0))
print('std:', randM.std())
print('sorted, it sorts each rows independently:')
randM.sort()
print(randM)
print()




