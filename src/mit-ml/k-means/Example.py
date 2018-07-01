import numpy as np



def calculateDistance(data1, data2, n=2):
    """
    :param data1: np array of size x
    :param data2: np array of size x
    :param n: minkowski number
    :return:
    """
    assert isinstance(data1, np.ndarray)
    return sum( (data1 - data2) ** n ) ** (1/n)


class Example:

    def __init__(self, name, features):
        self.name = name
        self.features = features

    def distance(self, other):
        assert isinstance(other, Example)
        assert self.dimensionality() == other.dimensionality()
        return calculateDistance(
            np.array(self.features), np.array(other.getFeatures())
        )

    def dimensionality(self):
        return len(self.features)

    def getName(self):
        return self.name

    def getFeatures(self):
        return self.features



