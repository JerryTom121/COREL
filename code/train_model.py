#this will calculate the co-efficients of linear model using linear regression

import csv
import sys
from sklearn import linear_model
reader=csv.reader(open('./../dataset/output/linear_model_data.csv','rt'))
writer=csv.writer(open('./../dataset/output/coefficient.csv','wb'))
dataset=[]
lebles=[]
for row in reader:
	dataset.append([float(row[0]),float(row[1]),float(row[2]),float(row[3])])
	lebles.append(float(row[4]))

clf = linear_model.LinearRegression()
clf.fit (dataset,lebles)
print 
v=[]
v.append(clf.intercept_)
for x in clf.coef_:
	v.append(x)
print v

writer.writerow(v)