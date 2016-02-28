import csv
import sys
reader=csv.reader(open("./../dataset/"+sys.argv[1],"rt"))
i,x=0,5
for row in reader:
	print row
	if i>x:
		break
	i=i+1
