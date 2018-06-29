import numpy as np
import pylab

rattlesnake = np.array([1,1,1,1,0])
boaConstrictor = np.array([0,1,0,1,0])
fartFrog = np.array([1,0,1,0,4])


def computeDistance(data1, data2, p=2):
    """
    :param data1: np array
    :param data2: np array
    :param p: 2 for euclidian distance, 1 for minkowski
    :return:
    """
    return sum( (data1-data2) ** p ) ** (1/p)


class Animal:

    def __init__(self, name, features):
        """
        :param name: string
        :param features: list of size 5 corresponding to todo
        """
        self.name = name
        self.features = features

    def getName(self):
        return self.name

    def getFeatures(self):
        return self.features

    def distance(self, other):
        """
        :param other: another Animal obj
        :return: distance in default euclidian
        """
        return computeDistance(np.array(self.features), np.array(other.getFeatures()))


def compareAnimals(animals):
    """Assumes animals is a list of animals, precision an int >= 0
    Builds a table of Euclidean distance between each animal"""
    # Get labels for columns and rows
    columnLabels = []
    for a in animals:
        columnLabels.append(a.getName())
    rowLabels = columnLabels[:]
    tableVals = []
    # Get distances between pairs of animals
    # For each row
    for a1 in animals:
        row = []
        # For each column
        for a2 in animals:
            if a1 == a2:
                row.append('--')
            else:
                distance = a1.distance(a2)
                row.append(str(round(distance, 3)))
        print(row)
        tableVals.append(row)
    # Produce table
    table = pylab.table(rowLabels=rowLabels, colLabels=columnLabels, cellText=tableVals,
        cellLoc='center', loc='center', colWidths=[0.2]*len(animals))
    table.scale(1, 2.5)
    pylab.axis('off')  # Don't display x and y-axes
    pylab.savefig('distances')
    pylab.show()


# def my_variance(data):
#     """
#     :param data: np array
#     :return: variance
#     """
#     mean = sum(data) / len(data)
#     return ( sum( computeDistance(mean, data) ** 2 ) ) ** 0.5

class Example:

    def __init__(self, name, features, label=None):
        self.name = name
        self.features = features
        self.label = label

    def dimensionality(self):
        return len(self.features)

    def getFeatures(self):
        return self.features[:]

    def getLabel(self):
        return self.label

    def getName(self):
        return self.name

    def distance(self, other):
        return computeDistance(self.features, other.getFeatures(), 2)

    def __str__(self):
        return self.name + ':' + str(self.features) + ':' + str(self.label)


class Cluster:

    def __init__(self, examples, exampleType):
        """
        :param examples: a list of type exampleType
        :param exampleType: type
        """
        assert isinstance(examples[0], Example)
        self.examples = examples
        self.exampleType = exampleType
        self.centroid = self.computeCentroid()

    def computeCentroid(self):
        dim = self.examples[0].dimensionality()
        totVals = np.array([0.0] * dim)
        for e in self.examples:
            totVals += e.getFeatures()
        centroid = self.exampleType('centroid', totVals / float(len(self.examples)))
        return centroid

    def update(self, examples):
        oldCentroid = self.centroid
        self.examples = examples
        if len(examples) > 0:
            self.centroid = self.computeCentroid()
            return oldCentroid.distance(self.centroid)
        else:
            return 0.0

    def members(self):
        for e in self.examples:
            yield e

    def size(self):
        return len(self.examples)

    def getCentroid(self):
        return self.centroid

    def variance(self):
        totDist = 0.0
        for e in self.examples:
            totDist += (e.distance(self.centroid)) ** 2
        return totDist ** 0.5

    def __str__(self):
        names = []
        for e in self.examples:
            names.append(e.getName())
        names.sort()
        result = 'Cluster with centroid' + str(self.centroid.getFeatures()) + '' \
              'contains:\n  '
        for e in names:
            result = result + e + ', '
        return result[:-2]

# print('data distance:', computeDistance(fartFrog, boaConstrictor))

# rattlesnake = Animal('rattlesnake', [1,1,1,1,0])
# boa = Animal('boa\nconstrictor', [0,1,0,1,0])
# dartFrog = Animal('dart frog', [1,0,1,0,4])
#
# print(Animal.distance(boa, rattlesnake))


my_animals = [Animal('rattlesnake', [1,1,1,1,0]), Animal('boa\nconstrictor', [0,1,0,1,0])
              , Animal('dart frog', [1,0,1,0,1])]
alligator = Animal('alligator', [1,1,0,1,1])
my_animals.append(alligator)
compareAnimals(my_animals)


