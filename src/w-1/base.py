import numpy
import pylab


def meanStd(data):
    """
    :param data: numpy list of numbers
    :return: mean and std of numbers in list
    """
    mean = sum(data) / len(data)
    std = (sum(((data - mean) ** 2)) / len(data)) ** 0.5
    return mean, std


def coefficientOfDetermination(y1, y2):
    """
    :param y1: matlab array
    :param y2: matlab array
    :return: R^2
    """
    mean = sum(y1) / len(y1)
    estimatedError = sum((y1 - y2) ** 2)
    estimatedDVariability = sum((y1 - mean) ** 2)
    return 1 - estimatedError / estimatedDVariability


def plottingStuff():
    linear = []
    quadratic = []
    cubic = []
    exponential = []
    tetrated = []
    for i in range(0, 20):
        linear.append(i)
        quadratic.append(i**2)
        cubic.append(i**3)
        exponential.append(2**i)
        tetrated.append((2**i)*i)
    pylab.plot(linear, label='linear')
    pylab.plot(quadratic, label='quadratic')
    pylab.plot(cubic, label='cubic')
    pylab.plot(exponential, label='exponential')
    pylab.plot(tetrated, label='tetracted')
    pylab.ylim(0, 50)
    pylab.legend()
    pylab.show()


def reverseWord(word, position=0, finalword=''):
    if position < len(word)-1:
        finalword = reverseWord(word, position+1, finalword)
    finalword += word[position]
    return finalword


# d = [2,2,5,6,4,5,2,3,2,5,4,2,3,3,3,3]
# print(numpy.std(d))
# d = numpy.array(d)
# print(meanStd(d))

plottingStuff()


# a = (lambda x: x*2)
# print(a(4))
# print(reverseWord('we are the world'))

