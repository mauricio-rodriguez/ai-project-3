from sklearn.neighbors import KDTree


class Dbscan:
    def __init__(self, x, y, radius, minPts):
        self.x = x
        self.y = y
        self.radius = radius
        self.minPts = minPts
        self.labels = [-1] * len(x)
        self.kd = KDTree(x, leaf_size=2)

        # print(self.x)
        self.neighbors = [self.kd.query_radius(
            self.x[i: i + 1], radius) for i in range(len(x))]
        print(self.neighbors)

    def fit(self):
        for idx, point in enumerate(self.x):
            if labels[idx] == -1:
                continue
