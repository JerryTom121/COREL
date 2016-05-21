
import csv
import sys
from itertools import product
import operator
from sets import Set

readfile=csv.reader(open('./../dataset/preprocess_data_new.csv','rt'))

product_popularity=csv.reader(open('./../dataset/output/update_pop.csv'))
popularity={}  #stores the popularity of each product
for pro in product_popularity:
	popularity[pro[0]]=pro[1]


true_count=0
total_count=0
n=int(input("Enter N: "))
def frequency(products,item): #this will calculate the frequency of item in products set
	count=0
	for x in products:
		if x==item:
			count+=1
	return count
for row in readfile:
	total_count+=1
	section_A=row[1].split(',') #section A items
	section_B=row[2].split(',') #section B items
	section_C=Set([])  #set of section C items
	for x in row[3].split(','):
		try:
			section_C.add(x)
		except KeyError:
			continue
	
	products=section_A+section_B  #product set
	pi=section_B[0] #randomly selected any product
	#pi_count=frequency(products,pi)
	item_counter={}  #this will store the P(Pj|Pi) score
#	print pi
	for item in products:
		try:
			if item in item_counter:
				item_counter[item]+=1
				
			else:
				item_counter[item]=1
		except KeyError:
			continue
	for item in item_counter:  #here we multiplied each products pi_pj score with Pj popularity
		item_counter[item]*=float(popularity[item])
	item_counter=sorted(item_counter.items(),key=operator.itemgetter(1),reverse=True)
#	print item_counter
	counter=0
	top_item=Set([])
	for item,value in item_counter:
		if counter==n:
			break
		if item!=pi:
			top_item.add(item)
			counter+=1
	
	#print section_C
	#print 'hello2'
	if len(section_C.intersection(top_item))>0:
		true_count+=1
	#print true_count

print float(true_count)/total_count