import csv
import sys
import time
from sets import Set
from itertools import product
import time
try:
	print "stage 1 started..."
	third_category={}
	category_reader=csv.reader(open('./../dataset/english/category.csv','rt'))
	for row in category_reader:
		key,value=row[0].strip(),row[3].strip()
		third_category[key]=value

####stage 2########################################################
	print "stage 2 started..."
	market_basket_reader=csv.reader(open('./../dataset/output/market_basket.csv','rt'))
	pair_writer=csv.writer(open('./../dataset/output/pair_item_third.csv','wb'))
	i,x=0,10
	pair_counter={}
	for row in market_basket_reader:
		basket=row[1].split(',')
		for x,y in product(basket,basket):
			try:
				if x != y:
					pair=third_category[x]+' '+third_category[y]
					if pair in pair_counter:
						pair_counter[pair]+=1
					else:
						pair_counter[pair]=1
			except KeyError:
				continue

	print "writing..."
	writer=csv.writer(open('./../dataset/output/pair_counter.csv','wb'))
	for key in pair_counter:
		writer.writerow([key,pair_counter[key]])

finally:
	print "Completed!!"