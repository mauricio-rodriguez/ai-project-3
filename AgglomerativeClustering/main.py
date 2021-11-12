import reader as rd
import numpy as np
from preprocessing import normalize, reduction, shuffle
from sklearn.metrics.cluster import pair_confusion_matrix
from sklearn.cluster import AgglomerativeClustering


if __name__ == "__main__":
    x, y = rd.read("../data/reducted.csv", "../data/tissue.csv")

    clustering = AgglomerativeClustering(n_clusters=len(np.unique(y))).fit(x)
    print(clustering.labels_)

    print("Clusters:", len(set(clustering.labels_)))
    print("Y's:", len(np.unique(y)))

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

    print("Confusion Matrix:", pair_confusion_matrix(clustering.labels_, labels))
