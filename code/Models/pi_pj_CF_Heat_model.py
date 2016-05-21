


import csv
import sys
from itertools import product
import operator
from sets import Set
import math

readfile=csv.reader(open('./../dataset/preprocess_data_500.csv','rt'))

third_category={} #this will store the third category of product
category_reader=csv.reader(open('./../dataset/english/category.csv','rt'))
for row in category_reader:
	key,value=row[0].strip(),row[3].strip()
	third_category[key]=value







market_basket={} #customers market basket

for row in readfile:
	market_basket[row[0]]=[row[1].split(',')+row[2].split(','),row[3].split(',')]
#print market_basket['161517']
#exit()
rating_reader=csv.reader(open('../dataset/test/trimed_rating_1000.csv','rt'))
rating={} #this will store the rating of each product
count=0
for row in rating_reader:
	rating[row[0]+' '+row[1]]=float(row[2])
	#print row[0],row[1]
#	count+=1
	#if count==10:
	#	break
#exit()
#this function will calculate the cosine similarity between two customers
def cosine_similarity(u1,u2):
	user1=list(Set(market_basket[u1][0]))
	user2=list(Set(market_basket[u2][0]))
	user1=sorted(user1)
	user2=sorted(user2)
	rating_sum=0
	i,j=0,0
	mod1=0
	mod2=0
	while i<len(user1) and j<len(user2):

		pid1=user1[i]
		'''if u1=='100401' and pid1=='1266857':
			print "heeellerlere"'''
		pid2=user2[j]
		try:
			mod1+=rating[u1+' '+pid1]**2
			#print "HEllo"
		except KeyError:
			i+=1
			continue
		try:
			mod2+=rating[u2+' '+pid2]**2
			#print "HEllo2"
		except KeyError:
			j+=1
			continue
		if pid1==pid2:
			rating_sum+=rating[u1+' '+pid1]*rating[u2+' '+pid2]
			i+=1
			j+=1
		elif pid1>pid2:
			j+=1
		else:
			i+=1
	try:
		return float(rating_sum)/(math.sqrt(mod1)*math.sqrt(mod2))
	except ZeroDivisionError:
		return 0



#this will return top 10 similar users
def top_rating_CF(u1):
	similarity={}
	for user in market_basket:
		if user==u1:
			continue
		similarity[user]=cosine_similarity(u1,user)
	sorted_similarity=sorted(similarity.items(),key=operator.itemgetter(1),reverse=True)
	top_9_users={}
	top_9_users[u1]=1.0
	count_user=0
	for x,y in sorted_similarity:
		if count_user==9:
			break
		top_9_users[x]=y
		count_user+=1
	return top_9_users

#this will calculate the frequency of item in producs
def frequency(products,item):
	count=0
	for x in products:
		if x==item:
			count+=1
	return count
#this will return the top 10 third category products
def top_10_category(row):
	section_A=row[1].split(',')
	section_B=row[2].split(',')
	
	products=section_A+section_B
	#pi_count=frequency(products,pi)
	flag=False
	for i in range(0,len(section_B)):
		try:
			pi=third_category[section_B[0]]
			flag=True
			break
		except KeyError:
			continue
	if flag==False:
		return list([])
	item_counter={}
#	print pi
	for item in products:
		try:
			if third_category[item] in item_counter:
				item_counter[third_category[item]]+=1
				
			else:
				item_counter[third_category[item]]=1
		except KeyError:
			continue
	item_counter=sorted(item_counter.items(),key=operator.itemgetter(1),reverse=True)
#	print item_counter
	counter=0
	top_item=Set([])
	for item,value in item_counter:
		if counter==10:
			break
		if item!=pi:
			top_item.add(item)
			counter+=1
	
	return list(top_item)


#this will create the candidate product set from top 10 third category products
def candidate_product_set(top_category):
	readfile=csv.reader(open('./../dataset/category_to_product_map.csv','rt'))
	items=[]
	for x in readfile:
		if x[0] in top_category:
			items=items+x[1].split(',')
	return list(Set(items))

product_popularity=csv.reader(open('./../dataset/output/update_pop.csv'))
popularity={}
for pro in product_popularity:
	popularity[pro[0]]=pro[1]
def sorted_cf_score_products(candidate_products,top_users):
	product_rating={}
	for item in candidate_products:
		temp=0.0
		count=0
		for user in top_users:
			try:
				temp_rating=rating[user+' '+item]
				count+=1
			except KeyError:
				continue
			temp+=float(temp_rating)*float(top_users[user])
		if count==0:
			product_rating[item] = 0.0
		else:
			try:
				product_rating[item]=temp/count*float(popularity[item])
			except KeyError:
				product_rating[item]=0.0
	return product_rating

true_count=0
total_count=0
n=input("Enter N: ")
readfile=csv.reader(open('./../dataset/preprocess_data_500.csv','rt'))
for row in readfile:
	top_category=top_10_category(row)
	top_users=top_rating_CF(row[0].strip())
	candidate_products=candidate_product_set(top_category)
	scsp=sorted_cf_score_products(candidate_products,top_users)
	scsp = sorted(scsp.items(),key=operator.itemgetter(1),reverse=True)
	suggested_products=[]
	count=0
	for x,y in scsp:
		if count==n:
			break
		suggested_products.append(x)
		count+=1
	Section_C=row[3].split(',')
	if len(Set(suggested_products).intersection(Set(Section_C)))>0:
		true_count+=1
	total_count+=1
	print total_count

print "accuracy",float(true_count)/total_count