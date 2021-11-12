import reader as rd
import numpy as np
from preprocessing import normalize, reduction, shuffle
from sklearn.cluster import KMeans


if __name__ == "__main__":
    x, y = rd.read("../data/reducted.csv", "../data/tissue.csv")
    kmeans = KMeans(n_clusters=len(np.unique(y)), random_state=0).fit(x)
    print(kmeans.labels_)
