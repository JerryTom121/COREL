#this preprocess the data and divide them into 3 sections Section_A,section_B,section_C
import csv
import time
rating_reader=csv.reader(open('./../dataset/rating.csv','rt'))
writer=csv.writer(open('./../dataset/rating_52000.csv','wb'))
section_A={}
section_B={}
section_C={}

t1="2012-06-30"
t2="2012-07-31"
for row in rating_reader:
	t=row[4].split(' ')[0].strip()
	#print t
	userID=row[2].strip()
	pid=row[1].strip()
	writer.writerow([userID,pid,row[3].strip()])
	if t<=t1:
		if userID in section_A:
			section_A[userID].append(pid)
		else:
			section_A[userID]=[pid]
	elif t<=t2 and t>t1:
		if userID in section_B:
			section_B[userID].append(pid)
		else:
			section_B[userID]=[pid]
	else:
		if userID in section_C:
			section_C[userID].append(pid)
		else:
			section_C[userID]=[pid]

count=0
writer=csv.writer(open('./../dataset/preprocess_data_new.csv','wb'))
for userID in section_A:
	if (userID in section_A) and (len(section_A[userID])>=30) and (userID in section_B) and (userID in section_C):
		count+=1
		writer.writerow([userID,",".join(section_A[userID]),",".join(section_B[userID]),",".join(section_C[userID])])

print count