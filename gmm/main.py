import reader as rd
import numpy as np
from preprocessing import normalize, reduction, shuffle

if __name__ == "__main__":
    # rd.toCSV("../dataset_tissue.txt", "../clase.txt")

    """
    x, y = rd.read("./dataset.csv", "./tissue.csv")
    x[:, :] = normalize(x)

    reduction(x, 20)
    """

    x, y = rd.read("./reducted.csv", "./tissue.csv")

    np.random.seed(0)
    shuffleX, shuffleY = shuffle(x, y)

    # los pi se dividen entre k al inicio
    # media y varianza aleatoria
