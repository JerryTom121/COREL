import csv
import sys
readfile=open('./../dataset/english/rating.csv','rt')
writefile=open('./../dataset/output/market_basket.csv','wb')
try:
	reader=csv.reader(readfile)
	writer=csv.writer(writefile,dialect='excel')
	store_map={}
	for row in reader:
		key,value=row[2].strip(),row[1].strip()
		if key in store_map:
			store_map[key].append(value)
		else:
			store_map[key]=[value]
	'''key_list=store_map.keys()
	key_list.sort()'''
	print "dictionary length : ",len(store_map)
	print "writing market basket to csv file......."
	for row in store_map:
			writer.writerow([row,",".join(store_map[row])])
	
finally:
	readfile.close()
	writefile.close()