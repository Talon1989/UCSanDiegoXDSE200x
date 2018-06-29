import random
import pylab


class Location:

    def __init__(self, x, y):
        """
        :param x: float
        :param y: float
        """
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        assert isinstance(other, Location)
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist ** 2 + yDist ** 2) ** 0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'


# --------------------------------------------------------------


class Field:

    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('drunk not in the dictionary')
        currentLoc = self.drunks[drunk]
        xDist, yDist = drunk.takeStep()
        self.drunks[drunk] = currentLoc.move(xDist, yDist)

    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('drunk not in the dictionary')
        return self.drunks[drunk]


# --------------------------------------------------------------


class Drunk:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Abstract Drunk'


class UsualDrunk(Drunk):

    def takeStep(self):
        return random.choice( [(0.0,1.0), (0.0,-1.0), (1.0,0.0), (-1.0,0.0)] )


class NorthEastDrunk(Drunk):

    def takeStep(self):
        return random.choice( [(0.0,2.0), (0.0,-1.0), (2.0,0.0), (-1.0,0.0)] )


tries = 200
xResults = []
yResults = []
for _ in range(tries):
    field = Field()
    ivan = NorthEastDrunk('ivan')
    field.addDrunk(ivan, Location(0.,0.))
    start = field.getLoc(ivan)
    for _ in range(100):
        field.moveDrunk(ivan)
    xResults.append(field.getLoc(ivan).getX())
    yResults.append(field.getLoc(ivan).getY())
pylab.plot(xResults, yResults, 'r+')
pylab.ylabel('y axis')
pylab.xlabel('x axis')
pylab.ylim(-100,+100)
pylab.xlim(-100,+100)
pylab.legend()
pylab.show()


