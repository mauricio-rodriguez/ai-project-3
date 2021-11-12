import reader as rd
import numpy as np
from preprocessing import normalize, reduction, shuffle
from gmm import GMM

if __name__ == "__main__":
    # rd.toCSV("../dataset_tissue.txt", "../clase.txt")

    x, y = rd.read("../data/dataset.csv", "../data/tissue.csv")
    x[:, :] = normalize(x)
    print(x)

    # reduction(x, 20)
    """
    """

    # x, y = rd.read("../data/reducted.csv", "../data/tissue.csv")

    # np.random.seed(0)
    # shuffleX, shuffleY = shuffle(x, y)

    # clusters = 10
    # epoch = 10

    # e1 = GMM(shuffleX, shuffleY, clusters, epoch)

    # los pi se dividen entre k al inicio
    # media y varianza aleatoria
