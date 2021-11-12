import reader as rd
import numpy as np
from preprocessing import normalize, reduction, shuffle
from sklearn.cluster import KMeans
from sklearn.metrics.cluster import pair_confusion_matrix


if __name__ == "__main__":
    x, y = rd.read("../../data/reducted.csv", "../../data/tissue.csv")
    kmeans = KMeans(n_clusters=len(np.unique(y)), random_state=0)
    kmeans = kmeans.fit(x)
    labels = kmeans.predict(x)

    print(labels)
    print()

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

    print(kmeans.labels_)
    print()
    print(pair_confusion_matrix(kmeans.labels_, labels))
