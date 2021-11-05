import preprocessing as p
from Kmeans.kmeans import KMEANS

if __name__ == "__main__":
    data = p.get_data("dataset_tissue.txt")
    test = KMEANS(data,3)