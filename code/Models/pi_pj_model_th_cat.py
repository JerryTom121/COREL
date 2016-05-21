import csv
import sys
from itertools import product
import operator
from sets import Set

readfile=csv.reader(open('./../dataset/test/preprocess_data_new.csv','rt'))

third_category={}
category_reader=csv.reader(open('./../dataset/english/category.csv','rt'))
for row in category_reader:
	key,value=row[0].strip(),row[3].strip()
	third_category[key]=value

true_count=0
total_count=0
n=int(input("Enter N: "))
def frequency(products,item):
	count=0
	for x in products:
		if x==item:
			count+=1
	return count
for row in readfile:
	total_count+=1
	section_A=row[1].split(',')
	section_B=row[2].split(',')
	section_C=Set([])
	for x in row[3].split(','):
		try:
			section_C.add(third_category[x])
		except KeyError:
			continue
	
	products=section_A+section_B
	try:
		pi=third_category[section_B[0]]
	except KeyError:
		continue
	#pi_count=frequency(products,pi)
	item_counter={}
#	print pi
	for item in products:
		try:
			if third_category[item] in item_counter:
				item_counter[third_category[item]]+=1
				
			else:
				item_counter[third_category[item]]=1
		except KeyError:
			continue
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

	#print pi,top_item
	if len(section_C.intersection(top_item))>0:
		true_count+=1
	#print true_count

print float(true_count)/total_count