import pandas as pd
import numpy as np


def toCSV(dataset, tissue):
    data = pd.read_csv(dataset)
    id = pd.DataFrame(
        np.array(data.columns.values[1:len(data.columns)]), columns=["id"])

    rows = data.values.transpose()
    cols = rows[0]
    rows = np.delete(rows, 0, 0)
    df = pd.DataFrame(rows, columns=cols)

    tissueData = pd.read_csv(tissue, usecols=["x"])
    tissueData.columns.values[0] = "name"

    tissueDf = pd.concat([id, tissueData], axis=1)

    df.to_csv("../data/dataset.csv", index=False)
    tissueDf.to_csv("./data/tissue.csv", index=False)


def read(dataset, tissue):
    x = []
    y = []

    datasetDf = pd.read_csv(dataset)
    tissueDf = pd.read_csv(tissue, usecols=["name"])

    return datasetDf.values, tissueDf.values
