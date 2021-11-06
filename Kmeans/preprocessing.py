import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA


def normalize(data):
    scaler = MinMaxScaler()
    normalizeData = scaler.fit_transform(data)

    return normalizeData

def components_analysis(data):
    pca = PCA(.95)
    principal_components = pca.fit_transform(data)
    return principal_components

def get_data(fileName):
    matrix = []
    with open(fileName,'r') as file:
        for row in file:
            line = row
            line = line.replace('"','')
            line = line.replace('\n','')
            line = line.split(',')
            matrix.append(line)
            
    #obtengo y elimino los nombres de filas y columnas
    #realizo una transpuesta, cada antigua columna es una fila
    column_names = matrix[0]
    matrix = np.delete(matrix,0,0)
    matrix = np.transpose(matrix)
    row_names = matrix[0]
    matrix = np.delete(matrix,0,0)
    matrix = matrix.astype(np.float)
    return matrix



        
