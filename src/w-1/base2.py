import numpy as np

an_array = np.array([1,2,3,4])
# print(an_array)

rank2 = np.array([[11,22,33], [21,22,23], [31,32,33], [41,42,43]])
print(rank2)
print('Shape is 4 rows, 3 columns:', rank2.shape)
print('Accessing element [0,2]:', rank2[0,2])


zeroes = np.zeros((2,2)) # 2 by 2 array of 0 values
print('zeroes:', zeroes)


print(np.array([[0,1,2], [10,11,12]]))


l = [1,2,3,4,5,6]
print([num for num in l if  num%2==0])
l2 = l[:]
l2.pop()
print(l)
print()
print()

row = [1,2,3,4]
col = [0,1,2,0]
for a,b in zip(row, col):
    print(a, b)


print()
print('BOOLEAN INDEXING')


an_array = np.array([[11.,12.], [21., 22.], [31., 32.]])
print(an_array.dtype)
even = an_array % 2 == 0
print(even)
print(an_array[even])


print(np.random.randn(2,5))

