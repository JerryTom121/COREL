#this program is written to do crowdsourcing of products 
#decide the more popular product between two products

import csv
import sys
from itertools import product
from datetime import datetime
reader=csv.reader(open('./../dataset/output/popularity_parameter.csv','rt'))
items=[]
rating_count={}
avrg_rating={}
on_self_date={}
limit=1000
counter=0
for row in reader:
	items.append(row[0])
	rating_count[row[0]]=row[1]
	avrg_rating[row[0]]=row[2]
	on_self_date[row[0]]=row[3]
	counter+=1
	if counter>limit:
		break
def calculate(pid):
	n=float(rating_count[pid])
	r=float(avrg_rating[pid])
	df="%Y-%m-%d"
	diff=datetime.strptime(datetime.today().strftime("%Y-%m-%d"),df)-datetime.strptime(on_self_date[pid],df)
	return float(n*r*3000)/float(diff.days)

writer=csv.writer(open('./../dataset/output/croudsourcing_data.csv','wb'))
pair=product(items,items)
for x,y in pair:
	if x!=y:
		pro1=calculate(x)
		pro2=calculate(y)
		if pro1>pro2:
			writer.writerow([x,y,x])
		else:
			writer.writerow([x,y,y])