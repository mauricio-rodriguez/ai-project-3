from dbscan import *
import reader as rd

x, y = rd.read("../data/reducted.csv", "../data/tissue.csv")

db = DBScan(x,5,2)
res = db.fit()

