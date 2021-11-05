import numpy as np

class KMEANS:
    def __init__(self, data,k = 3, iterations = 100):
        self.data = data
        self.iterations = iterations
        self.k = k
        self.rows, self.dimensions = self.data.shape
        #indices pertenecientes a cada cluster
        self.clusters = [[] for i in range(self.k)]
        
        self.centroids = []
        
    def euclidean_distance(self,first,second):
        sum = 0
        for i in range(first.size):
            sum += (first[i] - second[i])**2
        return np.sqrt(sum)
    
    def initialize_centroids(self):
        random_points = np.random.choice(self.rows, self.k, replace = False)
        self.centroids = [self.data[index]  for index in random_points]
    
    def kmeans(self):
        self.initialize_centroids()
        for i in range(self.iterations):
            self._create_clusters()
            past_centroids = self.centroids
            self._update_centroids()
            if self._is_converged(past_centroids):
                break
    
    def _create_clusters(self):
        for index, row in enumerate(self.data):
            centroid_index = self._get_closest_centroid(row)
            self.clusters[centroid_index].append(index)
    
    def _get_closest_centroid(self,row):
        distances = [self.euclidean_distance(row, centroid) for centroid in self.centroids ]
        closest = np.argmin(distances)
        return closest
    
    def _update_centroids(self):
        for index, cluster in enumerate(self.clusters):
            mean =  [0] * self.dimensions
            for idx in cluster:
                mean += self.data[idx]
            mean = mean / float(len(cluster))
            self.centroids[index] = mean
    
    def _is_converged(self,past_centroids):
        distances = [self.euclidean_distance(past_centroids[i],self.centroids[i]) for i in range (self.k)]
        return round(sum(distances)) == 0   