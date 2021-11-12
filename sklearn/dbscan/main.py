import reader as rd
import numpy as np
from preprocessing import normalize, reduction, shuffle
from sklearn.cluster import DBSCAN
from sklearn.metrics.cluster import pair_confusion_matrix


if __name__ == "__main__":
    x, y = rd.read("../../data/reducted.csv", "../../data/tissue.csv")

    clustering = DBSCAN(eps=3, min_samples=2).fit(x)
    print("# Clusters:", len(set(clustering.labels_)))

    labels = clustering.fit_predict(x)

    clusters = {}
    n = 0
    for item in labels:
        if item in clusters:
            clusters[item].append(y[n])
        else:
            clusters[item] = [y[n]]
        n += 1

    for item in clusters:
        print("Cluster ", item)
        for i in clusters[item]:
            print(i, end=" ")
        print()
        print()

    print("Confusion matrix:", pair_confusion_matrix(clustering.labels_, labels))
