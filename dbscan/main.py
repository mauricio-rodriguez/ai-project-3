from dbscan import *
import reader as rd

x, y = rd.read("../data/reducted.csv", "../data/tissue.csv")

print(x[:3,:])

#db = DBScan(avr,1,3)
#res = db.fit()
#print(res)