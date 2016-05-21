import csv
import math
from sets import Set
import operator

data_reader=csv.reader(open('../dataset/test/preprocess_data_new.csv','rt'))
market_basket={}
for row in data_reader:
	market_basket[row[0]]=[row[1].split(',')+row[2].split(','),row[3].split(',')]
#print market_basket['161517']
#exit()
rating_reader=csv.reader(open('../dataset/test/trimed_rating_1000.csv','rt'))
rating={}
count=0
for row in rating_reader:
	rating[row[0]+' '+row[1]]=float(row[2])

def cosine_similarity(u1,u2):
	user1=list(Set(market_basket[u1][0]))
	user2=list(Set(market_basket[u2][0]))
	user1=sorted(user1)
	user2=sorted(user2)
	rating_sum=0
	i,j=0,0
	mod1=0
	mod2=0
	while i<len(user1) and j<len(user2):

		pid1=user1[i]
		'''if u1=='100401' and pid1=='1266857':
			print "heeellerlere"'''
		pid2=user2[j]
		try:
			mod1+=rating[u1+' '+pid1]**2
			#print "HEllo"
		except KeyError:
			i+=1
			continue
		try:
			mod2+=rating[u2+' '+pid2]**2
			#print "HEllo2"
		except KeyError:
			j+=1
			continue
		if pid1==pid2:
			rating_sum+=rating[u1+' '+pid1]*rating[u2+' '+pid2]
			i+=1
			j+=1
		elif pid1>pid2:
			j+=1
		else:
			i+=1
	try:
		return float(rating_sum)/(math.sqrt(mod1)*math.sqrt(mod2))
	except ZeroDivisionError:
		return 0

length=len(users)

for i in range(0,length):
	for j in range(i+1,length):

