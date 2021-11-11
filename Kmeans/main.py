# import preprocessing as p
# from general_functions import helpers, preprocessing
# from kmeans import KMEANS

# if __name__ == "__main__":
#     data = p.get_data("../dataset_tissue.txt")
#     data = p.normalize(data)
#     data = p.components_analysis(data)
#     print(data.shape)
#     print(data)
#     # test = KMEANS(data,3)
#     # test.kmeans()
    
from general_functions import helpers, preprocessing
from data import reducted

if __name__ == "__main__":
    
    