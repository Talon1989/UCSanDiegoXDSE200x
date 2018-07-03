import random
import numpy as np
import pylab

from Example import Example


# random.seed(0)
# units = []
# for i in range(10):
#     x, y = random.choice([0,1,2,3]), random.choice([0,1,2,3])
#     units.append(Example(str(i), [x,y]))
#
#
# print(Example.distance(units[0], units[1]))


def plot2Samples(samples1, samples2, marker1, marker2):
    xVals, yVals = [], []
    for s in samples1:
        x = s.getFeatures()[0]
        y = s.getFeatures()[1]
        pylab.annotate(s.getName(), xy=(x, y), xytext=(x + 0.13, y - 0.07), fontsize='x-large')
        xVals.append(x)
        yVals.append(y)
    pylab.plot(xVals, yVals, marker1)
    xVals, yVals = [], []
    for s in samples2:
        x = s.getFeatures()[0]
        y = s.getFeatures()[1]
        pylab.annotate(s.getName(), xy=(x, y), xytext=(x + 0.13, y - 0.07), fontsize='x-large')
        xVals.append(x)
        yVals.append(y)
    pylab.plot(xVals, yVals, marker2)
    pylab.show()


class Cluster:

    def __init__(self, examples, ExampleType):
        """
        :param examples: array of example
        :param ExampleType: class type of example
        """
        self.examples = examples
        self.ExampleType = ExampleType
        self.centroid = self.computeCentroid()

    def computeCentroid(self):
        dimensions = self.examples[0].dimensionality()
        centroid = np.array( [0.0] * dimensions )
        for e in self.examples:
            centroid += e.getFeatures()
        return self.ExampleType( 'centroid', centroid / len(self.examples) )

    def update(self, newExamples):
        if len(newExamples) < 1:
            return 0.0
        else:
            oldCentroid = self.centroid
            self.examples = newExamples
            self.centroid = self.computeCentroid()
            return oldCentroid.distance(self.centroid)

    def variance(self):
        counter = 0.0
        for e in self.examples:
            counter += (e.distance(self.centroid)) ** 2
        return counter ** 0.5

    def size(self):
        return len(self.examples)

    def getCentroid(self):
        return self.centroid

    def __str__(self):
        return 'cluster of '+str(self.size())+' examples. Centroid: '+str(self.getCentroid())


def kMeans(examples, ExampleType, k):
    initialExamples = random.sample(examples, k)
    clusters = []
    for e in initialExamples:
        clusters.append(Cluster([e], ExampleType))
    flag = False
    while not flag:
        centroids = []
        for cl in clusters:
            centroids.append(cl.getCentroid())
        newClusters = [ [] for _ in range(k) ]
        for e in examples:
            closestDistance = e.distance(centroids[0])
            index = 0
            for i in range(1, k):
                distance = e.distance(centroids[i])
                if distance < closestDistance:
                    closestDistance = distance
                    index = i
            newClusters[index].append(e)
        flag = True
        for i in range(len(clusters)):
            if clusters[i].update(newClusters[i]) > 0.0:
                flag = False
    return clusters


def dissimilarity(clusters):
    """
    :param clusters: array of Cluster
    :return: dissimilarity
    """
    counter = 0.0
    for c in clusters:
        counter += c.variance()
    return counter


def tryK(examples, ExampleType, k, numTrials):
    bestCluster = kMeans(examples, ExampleType, k)
    minDissimilarity = dissimilarity(bestCluster)
    for _ in range(numTrials):
        cluster = kMeans(examples, ExampleType, k)
        currentDissimilarity = dissimilarity(cluster)
        if currentDissimilarity < minDissimilarity:
            bestCluster = cluster
            minDissimilarity = currentDissimilarity
    return bestCluster


def contrivedTest(numTrials, k):
    def generateSamples(xM, xsd, yM, ysd, nn):
        samples = []
        for s in range(nn):
            x = random.gauss(xM, xsd)
            y = random.gauss(yM, ysd)
            samples.append(Example(str(s), [x, y]))
        return samples
    random.seed(0)
    xMean, xSD, yMean, ySD = 3, 1, 5, 1
    n = 10
    samples1 = generateSamples(xMean, xSD, yMean, ySD, n)
    samples2 = generateSamples(xMean+3, xSD, yMean+1, ySD, n)
    plot2Samples(samples1, samples2, 'b^', 'rx')
    cluster = tryK(samples1 + samples2, Example, k, numTrials)
    print(cluster)


contrivedTest(10, 2)


















