import numpy as np
import math
import matplotlib.pyplot as plt


class KMEANS:
    def __init__(self, data, k=3, iterations=100):
        self.data = data
        self.iterations = iterations
        self.k = k
        self.rows, self.dimensions = self.data.shape
        self.clusters = [[] for i in range(self.k)]

        self.centroids = []

    def distance(self, first, second):
        distance = np.sqrt(sum(pow(a - b, 2) for a, b in zip(first, second)))

        return distance

    def initialize_centroids(self):
        random_points = np.random.choice(self.rows, self.k, replace=False)
        centroids = [self.data[index] for index in random_points]
        return centroids

    def kmeans(self):
        self.centroids = self.initialize_centroids()
        for i in range(self.iterations):
            self.clusters = self._create_clusters()
            past_centroids = self.centroids
            self.centroids = self._update_centroids()
            if self._is_converged(past_centroids):
                print("converged", i)
                break

        return self.clusters

    def _create_clusters(self):
        clusters = [[] for i in range(self.k)]
        for index, row in enumerate(self.data):
            centroid_index = self._get_closest_centroid(row)
            clusters[centroid_index].append(index)
        return clusters

    def _get_closest_centroid(self, row):
        distances = [self.distance(row, centroid)
                     for centroid in self.centroids]
        closest = np.argmin(distances)
        return closest

    def _update_centroids(self):
        centroids = np.zeros((self.k, self.dimensions))
        for index, cluster in enumerate(self.clusters):
            mean = np.zeros(self.dimensions)
            for idx in cluster:
                mean += self.data[idx]
            mean = mean / float(len(cluster))
            centroids[index] = mean
        return centroids

    def _is_converged(self, past_centroids):
        distances = [self.distance(
            past_centroids[i], self.centroids[i]) for i in range(self.k)]
        return sum(distances) == 0
