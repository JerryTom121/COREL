#this extracts the product features(no_of_reviews,avg_rating,on_shelf,latest_review) and store them in one file

import csv
import time
try:
	rating_reader=csv.reader(open('./../dataset/english/rating.csv','rt'))
	product_reader=csv.reader(open('./../dataset/english/product_new.csv','rt'))
	parameter_writer=csv.writer(open('./../dataset/output/popularity_parameter.csv','wb'))
	on_shelf_date={}
	avrg_rating={}
	total_review={}
	latest_review={}
	for row in product_reader:
		#print row
		on_shelf_date[row[0].strip()]=row[1].strip()
	
	for row in rating_reader:
		pid,prating,rating_date=row[1].strip(),row[3].strip(),row[4].strip()
		if pid in avrg_rating:
			avrg_rating[pid]+=float(prating)
			total_review[pid]+=1
			if rating_date>latest_review[pid]:
				latest_review[pid]=rating_date
		else:
			avrg_rating[pid]=float(prating)
			total_review[pid]=1
			latest_review[pid]=rating_date
		

	for pid in avrg_rating:
		avrg_rating[pid]=float(avrg_rating[pid])/float(total_review[pid])
		try:
			on_shelf=on_shelf_date[pid];
		except KeyError:
			on_shelf="2010-09-20".strip()
		finally:
			parameter_writer.writerow([pid,total_review[pid],avrg_rating[pid],on_shelf,latest_review[pid]])

	
finally:
	print "complete...."