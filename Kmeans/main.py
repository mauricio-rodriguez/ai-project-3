import helpers
import csv
import numpy as np
from kmeans import KMEANS
from helpers import splitData,shuffle

if __name__ == "__main__":
    x = []
    with open('../data/reducted.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            temp = []
            for i in range(20):
                temp.append(float(row[str(i)]))
            x.append(temp)

    x = np.array(x)
    
    y = []
    with open('../data/tissue.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            y.append(row["name"])
    y = np.array(y)
    #shuffle(x, y)
    
    
    n_uniques = len(np.unique(y))
    test = KMEANS(x,3)
    clusters = test.kmeans()
    labels = [[y[element] for element in cluster] for cluster in clusters]
    #print(labels)
    
    