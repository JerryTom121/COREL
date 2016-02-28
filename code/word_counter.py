import csv
import sys
try:
	reader=csv.reader(open('./../dataset/output/market_basket.csv','rt'))
	writer=csv.writer(open('./../dataset/output/word_counter.csv','wb'))
	
	print "stage 1 started..."
	third_category={}
	category_reader=csv.reader(open('./../dataset/english/category.csv','rt'))
	for row in category_reader:
		key,value=row[0].strip(),row[3].strip()
		third_category[key]=value


	word_counter={}
	print "word counter started..."
	print "building dictionay...."
	for row in reader:
		for item in row[1].split(','):
			try:
				temp=third_category[item]
				if temp in word_counter:
					word_counter[temp]+=1
				else:
					word_counter[temp]=1
			except KeyError:
				continue

	print "dictionary complete...."
	print "writing...."
	for key in word_counter:
		writer.writerow([key,word_counter[key]])
finally:
	print "complete...."