import csv
import sys
from itertools import product
import operator
from sets import Set

readfile=csv.reader(open('./../dataset/preprocess_data_new.csv','rt'))

true_count=0 #no of time successfuly predicted
total_count=0 #total number of prediction made
n=int(input("Enter N: "))
def frequency(products,item): #this will caculate the frequency of item in products list
	count=0
	for x in products:
		if x==item:
			count+=1
	return count
for row in readfile:
	total_count+=1
	section_A=row[1].split(',')  #section A products of any user
	section_B=row[2].split(',')	 #section B products of any user
	section_C=Set([])			 #set of section C products of any user
	for x in row[3].split(','):
		try:
			section_C.add(x)
		except KeyError:
			continue
	
	products=section_A+section_B
	pi=section_B[0]    #item purchased by user
	#pi_count=frequency(products,pi)
	item_counter={}
#	print pi

	#this section calculates the frequency of each item in products list
	for item in products:
		try:
			if item in item_counter:
				item_counter[item]+=1
				
			else:
				item_counter[item]=1
		except KeyError:
			continue

	#this will sort the items according to their frequency
	item_counter=sorted(item_counter.items(),key=operator.itemgetter(1),reverse=True)
#	print item_counter

	#this will create a set of top n products
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
	#this will check whether pridicted output is correct or not
	if len(section_C.intersection(top_item))>0:
		true_count+=1
	#print true_count

print float(true_count)/total_count