import numpy as np
import pylab
import random

rattlesnake = np.array([1,1,1,1,0])
boaConstrictor = np.array([0,1,0,1,0])
fartFrog = np.array([1,0,1,0,4])


def plotSamples(samples, marker):
    xVals, yVals = [], []
    for s in samples:
        x = s.getFeatures()[0]
        y = s.getFeatures()[1]
        pylab.annotate(s.getName(), xy=(x, y), xytext=(x+0.13, y-0.07), fontsize='x-large')
        xVals.append(x)
        yVals.append(y)
    pylab.plot(xVals, yVals, marker)
    pylab.show()


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
        return computeDistance(
            np.array(self.features), np.array(other.getFeatures()), 2)

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


def kMeans(examples, exampleType, k, verbose):
    """Assumes examples is a list of examples of type exampleType,
    k is a positive int, verbose is a Boolean
    Returns a list containing k clusters. If verbose is
    True it prints result of each iteration of k-means"""

    # get k randomly chosen initial centroids
    initialCentroids = random.sample(examples, k)

    # create a singleton cluster for each centroid
    clusters = []
    for e in initialCentroids:
        clusters.append(Cluster([e], exampleType))

    # iterate until centroids do not change
    converged = False
    counter = 0
    while not converged:
        counter += 1
        newCluster = []
        for _ in range(k):
            newCluster.append([])
        for e in examples:
            smallestDistance = e.distance(clusters[0].getCentroid())
            index = 0
            for i in range(1, k):
                distance = e.distance(clusters[i].getCentroid())
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = i
            newCluster[index].append(e)

        # update each cluster, check if a centroid has changed
        converged = True
        for i in range(len(clusters)):
            if clusters[i].update(newCluster[i]) > 0.0:
                converged = False
            if verbose:
                print('Iteration #' + str(counter))
                for c in clusters:
                    print(c)
                print('\n')
    return clusters


def dissimilarity(clusters):
    totDist = 0.0
    for c in clusters:
        totDist += c.variance()
    return totDist


def tryKmeans(examples, exampleType, numClusters, numTrials, verbose=False):
    """
    Calls kmeans numTrials times and returns the result with the lowest dissimilarity
    """
    best = kMeans(examples, exampleType, numClusters, verbose)
    minDissimilarity = dissimilarity(best)
    for numTrials in range(1, numTrials):
        clusters = kMeans(examples, exampleType, numClusters, verbose)
        currDissimilarity = dissimilarity(clusters)
        if currDissimilarity < minDissimilarity:
            best = clusters
            minDissimilarity = currDissimilarity
    return best


def genDistribution(xMean, xSD, yMean, ySD, n, namePrefix):
    samples = []
    for s in range(n):
        x = random.gauss(xMean, xSD)
        y = random.gauss(yMean, ySD)
        samples.append(Example(namePrefix+str(s), [x, y]))
    return samples


def contrivedTest(numTrials, k, verbose=True):
    random.seed(0)
    xMean, xSD, yMean, ySD = 3, 1, 5, 1
    n = 10
    d1Samples = genDistribution(xMean, xSD, yMean, ySD, n, '1.')
    plotSamples(d1Samples, 'b^')
    d2Samples = genDistribution(xMean+3, xSD, yMean+1, ySD, n, '2.')
    plotSamples(d2Samples, 'ro')
    clusters = tryKmeans(d1Samples + d2Samples, Example, k, numTrials, verbose)
    print('Final result.')
    for c in clusters:
        print('', c)


contrivedTest(40,2, True)


# my_animals = [Animal('rattlesnake', [1,1,1,1,0]), Animal('boa\nconstrictor', [0,1,0,1,0])
#               , Animal('dart frog', [1,0,1,0,1])]
# alligator = Animal('alligator', [1,1,0,1,1])
# my_animals.append(alligator)
# compareAnimals(my_animals)


