#This program is used to calculate the popularity of products

import csv
from itertools import product
import sys
from math import exp
from datetime import datetime

writer=csv.writer(open('./../dataset/output/popularity_1.csv','wb'))
reader=csv.reader(open('./../dataset/output/popularity_parameter.csv','rt'))
coeff_reader=csv.reader(open('./../dataset/output/coefficient.csv','rt'))

for row in coeff_reader:
	coef=[float(row[0]),float(row[1]),float(row[2]),float(row[3]),float(row[4])]

def f(phi):
	pi_phi=coef[0]*phi[0]+coef[1]*phi[1]+coef[2]*phi[2]+coef[3]*phi[3]+coef[4]*phi[4]
	return float(exp(pi_phi))/float(1+exp(pi_phi))

df="%Y-%m-%d"

def date_diff(d1,d2):
	diff=datetime.strptime(d1,df)-datetime.strptime(d2,df)
	return diff.days

def diff(p1,p2):
	return float(p1)-float(p2)

def vect_diff(v1,v2):
	return [1,diff(v1[0],v2[0]),diff(v1[1],v2[1]),date_diff(v1[2],v2[2]),date_diff(v1[3],v2[3])]

V={}
pro=[]
for row in reader:
	pro.append(row[0])
	V[row[0]]=[row[1],row[2],row[3],row[4].split(' ')[0].strip()]
product_count=len(pro)
#print product_count
#exit()
pair=product(pro,pro)
Pd={}
grt=0
count=0
for a,b in pair:
	#print len(Pd)
	if len(Pd)==product_count:
		print count
		if count>20*product_count:
			print count
			break
		else:
			count=count+1
	if a!=b:
		phi=vect_diff(V[a],V[b])
		r=f(phi)
		if a in Pd:
			Pd[a]=Pd[a]+r-0.5
		else:
			Pd[a]=r-0.5
		if b in Pd:
			Pd[b]=Pd[b]+0.5-r
		else:
			Pd[b]=0.5-r

		if Pd[a]>grt:
			grt=Pd[a]
		if Pd[b]>grt:
			grt=Pd[b]

print "max value: ",grt
for key in Pd:
	writer.writerow([key,Pd[key]])