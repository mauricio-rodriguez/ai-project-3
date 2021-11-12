import numpy as np
# from sklearn.datasets.samples_generator import make_blobs
from sklearn.datasets import make_blobs


class GMM:
    def __init__(self, x, y, clusters, epoch):
        self.x = x
        self.y = y
        self.clusters = clusters
        self.epoch = epoch
        self.dimensions = x.shape[1]

        self.pi = np.ones((x.shape[0], self.clusters)) / self.clusters
        self.mu = np.random.randint(min(x[:, 0]), max(x[:, 0]),
                                    size=(x.shape[0], self.clusters))
        self.sigma = np.random.randint(1, 5, size=(x.shape[0], self.clusters))

    def train(self):
        pass
