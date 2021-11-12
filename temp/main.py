import reader as rd
import numpy as np
from preprocessing import normalize, reduction, shuffle
from dbscan import Dbscan
from sklearn.cluster import DBSCAN


if __name__ == "__main__":
    x, y = rd.read("../data/reducted.csv", "../data/tissue.csv")

    clustering = DBSCAN(eps=3, min_samples=2).fit(x)
    print(clustering.labels_)
    print(len(set(clustering.labels_)))

    print(len(np.unique(y)))
