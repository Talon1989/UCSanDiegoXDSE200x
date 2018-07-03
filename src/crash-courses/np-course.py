import numpy as np



def arrays():

    arr = np.array([1,2,3])
    # print(arr)

    matrix = np.array( [ [1,2,3], [4,5,6], [7,8,9] ] )
    # print(matrix)

    arranged = np.arange(0, 10, dtype=float)
    # print(arranged)
    arranged_stepsOf2 = np.arange(0, 10, 2, dtype=float)
    print(arranged_stepsOf2)

    np.zeros( (5,3) )  # fill with zeroes, 5 rows 3 cols
    np.ones( (5,3) )  # fill with ones, 5 rows 3 cols

    lspace = np.linspace(0, 5, 10)  # 10 evenly spaced points from 0 to 5
    print(lspace)

    idMatrix = np.eye(4)  # identity matrix of 4x4
    # print(idMatrix)

    np.random.rand()
    randMatrix = np.random.rand(3,2)  # a,b size, populate with random values from 0 to 1
    # print(randMatrix)

    np.random.randn()  # same as above but with normal/gaussian distrib instead of uniform

    rarr = np.random.randint(1, 10, (3,3))  # 3x3 matrix of rand integers from 1 to 9

    arrangedArr = np.arange(0, 25)  # [0 1 2 ... 24]
    arrMatrix = arrangedArr.reshape(5,5)  # turns the array into a 5x5 matrix with the same values
    print(arrMatrix)

    print(rarr.max())  # max value of the random matrix rarr
    rarr.argmax()  # index of the max value

    rarr.shape  # (3, 3)

    rarr.dtype  # 'int32'


def arraysIndexing():

    arr = np.arange(0,11)
    arr[8]  # returns value at index 8
    arr[5:8]  # returns an array from index 5 to 8
    arr[:6]  # [0 1 2 3 4 5]
    arr[6:]  # [6 7 8 9 10]
    sliceArr = arr[0:6]
    arr[:] = 100  # also changes the slice, it's a copy, changing slice changes main
    print(arr)
    print(sliceArr)
    arr = np.arange(0,11)
    sliceArrCopy = arr.copy()[0:6]
    arr[:] = 100
    print(arr)
    print(sliceArrCopy)
    print()

    arr_2d = np.array([ [5,10,15], [20,25,30], [35,40,45] ])
    print(arr_2d)
    # double bracket format
    print( arr_2d[0][1] )  # row 0, col 1 = 10
    # single bracket format
    print( arr_2d[0,1] )  # 10
    arr_2d[0]  # all 0 row
    print( arr_2d[:, 0] )  # all 0 column = 5, 20, 35
    print( arr_2d[:2,1:] )
    print( arr_2d[1:] )
    print()

    arr = np.arange(1, 11)
    print(arr)
    bool_arr = arr > 5
    print(bool_arr)
    print(arr[bool_arr])
    arr_2d = np.arange(50).reshape(5,10)
    print(arr_2d)
    print('print 13,14, 23,24')
    print(
        arr_2d[1:3, 3:5]
    )


def operation():
    arr = np.arange(0, 10)
    print(arr)
    print(arr - arr)
    print(arr + 2)  # adds 2 to all values inside the array
    print(np.sqrt(arr))






operation()







