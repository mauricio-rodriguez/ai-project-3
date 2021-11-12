import numpy as np
import queue

undefined = 0

class DBScan:
    def __init__(self, data, eps=1, minPts=3):
        self.data = data
        self.eps = eps
        self.minPts = minPts

        self.pointCount = []
        self.moreMinPoints = []
        self.notMatchPoints = []
        self.labelPoints = []

    def rangeQuery(self, point):
        points = []
        for i in range(len(self.data)):
            d = np.linalg.norm(self.data[i] - self.data[point],2)
            if d <= self.eps:
                points.append(i)
        return points

    def fit(self):
        for i in range(len(self.data)):
            self.labelPoints.append(undefined)

        for i in range(len(self.data)):
            self.pointCount.append(self.rangeQuery(i))

        for i in range(len(self.pointCount)):
            if (len(self.pointCount[i]) >= self.minPts):
                self.labelPoints[i] = -1
                self.moreMinPoints.append(i)
            else:
                self.notMatchPoints.append(i)

        for i in self.notMatchPoints:
            for j in self.pointCount[i]:
                if j in self.moreMinPoints:
                    self.labelPoints[i] = -2
                    break

        C = 1
        for i in range(len(self.labelPoints)):
            neigNeigs = queue.Queue()
            if (self.labelPoints[i] == -1):
                self.labelPoints[i] = C
                for x in self.pointCount[i]:
                    if (self.labelPoints[x] == -1):
                        neigNeigs.put(x)
                        self.labelPoints[x] = C
                    elif (self.labelPoints[x] == -2):
                        self.labelPoints[x] = C

                while not neigNeigs.empty():
                    neighbors = self.pointCount[q.get()]
                    for y in neighbors:
                        if (self.labelPoints[y] == -1):
                            self.labelPoints[y] = C
                            neigNeigs.put(y)
                        if (self.labelPoints[y] == -2):
                            self.labelPoints[y] = C
                C += 1

        return self.labelPoints
