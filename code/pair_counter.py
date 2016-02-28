import sys
import csv
try:
	reader=csv.reader(open('./../dataset/output/pair_item_third.csv','rt'))
	writer=csv.writer(open('./../dataset/output/pair_counter.csv','wb'))
	pair_counter={}
	print "counting started...."
	print "buiding dictionary...."
	for row in reader:
		pair=row[0]+' '+row[1]
		if pair in pair_counter:
			pair_counter[pair]+=1
		else
			pair_counter[pair]=1
	print "dictionary complete..."
	print "writing frquency..."
	for key in pair_counter:
		writer.writerow([key,pair_counter[key]])
finally:
	print "complete ...."