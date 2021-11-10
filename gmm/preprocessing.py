import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler


def reduction(data):
    pca = PCA(n_components=20)
    principalComponents = pca.fit_transform(data)
    df = pd.DataFrame(data=principalComponents)
    df.to_csv("reducted.csv", index=False)


def normalize(data):
    scaler = MinMaxScaler()
    normalizeData = scaler.fit_transform(data)

    return normalizeData


def shuffle(x, y):
    p = np.random.permutation(len(x))
    return x[p], y[p]
