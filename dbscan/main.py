from dbscan import *

avr = np.array([[0,0],[1,0],[1,1],[2,2],[3,1],[3,0],[0,1],[3,2],[6,3]])

labelPoints = dbscan(avr, 1, 3)

print(labelPoints)