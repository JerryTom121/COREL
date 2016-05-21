#this program will generate data for linear model (will calculate constants beta_0,beta_1,beta_2....) 
import csv
import sys
from datetime import datetime
reader=csv.reader(open('./../dataset/output/croudsourcing_data.csv','rt'))
parameter_reader=csv.reader(open('./../dataset/output/popularity_parameter.csv','rt'))
writer=csv.writer(open('./../dataset/output/linear_model_data.csv','wb'))
df="%Y-%m-%d"
def date_diff(d1,d2):
	diff=datetime.strptime(d1,df)-datetime.strptime(d2,df)
	return diff.days
def diff(p1,p2):
	return float(p1)-float(p2)
print "##creating dataset for linear model......"
rating_count={}
avrg_rating={}
on_shelf={}
letest_date={}
for row in parameter_reader:
	pid=row[0]
	rating_count[pid]=row[1]
	avrg_rating[pid]=row[2]
	on_shelf[pid]=row[3]
	letest_date[pid]=row[4].split(' ')[0].strip()

print "writting file...."
for row in reader:
	pro1=row[0]
	pro2=row[1]
	better=row[2]
	not_better=pro1
	if better == pro1:
		not_better=pro2
	else:
		not_better=pro1
	writer.writerow([diff(rating_count[better],rating_count[not_better]),diff(avrg_rating[better],avrg_rating[not_better]),date_diff(on_shelf[better],on_shelf[not_better]),date_diff(letest_date[better],letest_date[not_better]),"1"])
	writer.writerow([-1*diff(rating_count[better],rating_count[not_better]),-1*diff(avrg_rating[better],avrg_rating[not_better]),-1*date_diff(on_shelf[better],on_shelf[not_better]),-1*date_diff(letest_date[better],letest_date[not_better]),"-1"])
