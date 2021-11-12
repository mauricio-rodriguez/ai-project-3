import numpy as np
import matplotlib.pyplot as plt
import queue
import csv

def rangeQuery(data, P, eps):
    points = []
    for i in range(len(data)):
        d = np.linalg.norm(data[i] - data[P],2)
        if d <= eps:
            points.append(i)
    return points

def dbscan(data, eps, minPts):
    
    pointCount = []
    moreMinPoints = []
    nonCore = []
    labelPoints = []
    for i in range(len(data)):
        labelPoints.append(0)

    for i in range(len(data)):
        pointCount.append(rangeQuery(data, i, eps))

    for i in range(len(pointCount)):
        if (len(pointCount[i]) >= minPts):
            labelPoints[i] = -1
            moreMinPoints.append(i)
        else:
            nonCore.append(i)

    for i in nonCore:
        for j in pointCount[i]:
            if j in moreMinPoints:
                labelPoints[i] = -2

                break

    C = 1
    for i in range(len(labelPoints)):
        q = queue.Queue()
        if (labelPoints[i] == -1):
            labelPoints[i] = C
            for x in pointCount[i]:
                if (labelPoints[x] == -1):
                    q.put(x)
                    labelPoints[x] = C
                elif (labelPoints[x] == -2):
                    labelPoints[x] = C

            while not q.empty():
                neighbors = pointCount[q.get()]
                for y in neighbors:
                    if (labelPoints[y] == -1):
                        labelPoints[y] = C
                        q.put(y)
                    if (labelPoints[y] == -2):
                        labelPoints[y] = C
            C += 1

    return labelPoints