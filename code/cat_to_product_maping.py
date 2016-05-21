# This will create a mapping from third category to products

import csv
import sys
from itertools import product
import operator
from sets import Set

readfile=csv.reader(open('./../dataset/category.csv','rt'))
writer=csv.writer(open('../dataset/category_to_product_map.csv','wb'))
category_to_product_map={}
for row in readfile:
	th_cat=row[3].strip()
	f_cat=row[0].strip()
	if th_cat in category_to_product_map:
		if len(category_to_product_map[th_cat])<10000:
			category_to_product_map[th_cat].append(f_cat)
	else:
		category_to_product_map[th_cat]=[f_cat]

print "writing..."
for x in category_to_product_map:
	writer.writerow([x,",".join(category_to_product_map[x])])