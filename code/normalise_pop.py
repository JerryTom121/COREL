#this code normalize the popularity score of products 
import csv
import operator
read=csv.reader(open('./../dataset/output/popularity_1.csv','rt'))
write=csv.writer(open('./../dataset/output/update_pop.csv','wb'))
for x in read:
	write.writerow([x[0],(float(x[1])+10)/20.0])