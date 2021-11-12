import reader as rd
import numpy as np
from preprocessing import normalize, reduction, shuffle
from sklearn.metrics.cluster import pair_confusion_matrix
from sklearn.mixture import GaussianMixture


if __name__ == "__main__":
    x, y = rd.read("../../data/reducted.csv", "../../data/tissue.csv")

    clustering = GaussianMixture(n_components=len(
        np.unique(y)), random_state=0).fit(x)
    print(clustering.means_)

    print(clustering.predict(x))
    print(clustering.score(x))
