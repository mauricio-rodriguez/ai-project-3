def shuffle(x, y):
    p = np.random.permutation(len(x))
    return x[p], y[p]

def percentage(length, fraction):
    return int(length * fraction / 100)


def splitData(dataset, train, val, test):
    rowsAmount = len(dataset)
    dTrain = dataset[:percentage(rowsAmount, train)]
    dVal = dataset[percentage(rowsAmount, train):percentage(rowsAmount, train + val)]
    dTest = dataset[percentage(rowsAmount, 100 - test):]

    return dTrain, dVal, dTest


def getAccuracy(confusionMatrix):
    return (confusionMatrix[0][0] + confusionMatrix[1][1]) / (confusionMatrix[0][0] + confusionMatrix[0][1] + confusionMatrix[1][0] + confusionMatrix[1][1]) * 100


def getError(confusionMatrix):
    return (confusionMatrix[1][0] + confusionMatrix[0][1]) / (confusionMatrix[0][0] + confusionMatrix[0][1] + confusionMatrix[1][0] + confusionMatrix[1][1]) * 100

