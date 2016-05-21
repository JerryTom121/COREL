

import csv
import time
import operator
from sets import Set
#user_id=str(input("Enter Your User Id: "))
#product_id=str(input("Enter Product: "))
n=int(input("enter N: ")) #take input for top-n values
 

#read market basket
market_basket=csv.reader(open('./../dataset/preprocess_data_new.csv','rt'))
basket={}  #training basket 
testing={}	#testing basket
for user in market_basket:
	basket[user[0]]=user[1]
	testing[user[0]]=user[3].split(',')

#read popularity
product_popularity=csv.reader(open('./../dataset/output/update_pop.csv'))
popularity={}  #stores popularity of each product
for pro in product_popularity:
	popularity[pro[0]]=pro[1]

def accuracy(user_id):   #it will calculate the accuracy for each userID
	#word counting 
	try:
		user_items=basket[user_id].split(',')
	except KeyError:
		return -1
	

	testing_set=Set(testing[user_id])

	score={}
	count=0
	for x in user_items:
		try:
			score[x]=float(popularity[x])
		except KeyError:
			continue
	result=[]
	sorted_score=sorted(score.items(),key=operator.itemgetter(1),reverse=True)
	for p,s in sorted_score:
		if count==n:
			break
		result.append(p)
		count+=1
	result_set=Set(result)
	#print result_set
	#print testing_set
	#print "Correct Predicted Items: ",result_set & testing_set
	if len(result_set & testing_set)>0:
		return 1
	return 0

#print accuracy('1228324','1005190980')
def calculate():   #calculate function will calculate the accuracy for each user
	total=0
	pridicted=0
	#print "hello",market_basket
	market_basket=csv.reader(open('./../dataset/preprocess_data_new.csv','rt'))
	for row in market_basket:
		uid=row[0]
		items=row[2].split(',')
		#print len(items)
		
		x=accuracy(uid)
		if x==-1:
			continue
		pridicted+=x 
		total+=1
	print "accuracy: ",float(pridicted)/total
	return

calculate()
'''pop_product=csv.reader(open('./../dataset/output/sorted_pop.csv','rt'))
#if items purchaged are less than 3
if count<10:
	for x in pop_product:
		if count==10:
			break
		print x[0],x[1]
		count+=1
'''