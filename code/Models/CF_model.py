import csv
import math
from sets import Set
import operator
data_reader=csv.reader(open('../dataset/test/preprocess_data_new.csv','rt'))
market_basket={}   #masket basket will store the user to its product mapping
row_count=0
for row in data_reader:
	if row_count==500:
		break
	market_basket[row[0]]=[row[1].split(',')+row[2].split(','),row[3].split(',')]
	row_count+=1
#print market_basket['161517']
#exit()
rating_reader=csv.reader(open('../dataset/test/trimed_rating_1000.csv','rt'))
rating={}   #rating dict will store the (user+product) to rating mapping
count=0

for row in rating_reader:
	rating[row[0]+' '+row[1]]=float(row[2])
	#print row[0],row[1]
#	count+=1
	#if count==10:
	#	break
#exit()
#this function will be used to calculate the cosine similarity bitween two customers
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

def top_rating_CF(u1):     #this will return the sorted similarty of customers
	similarity={}
	for user in market_basket:
		if user==u1:
			continue
		similarity[user]=cosine_similarity(u1,user)
	sorted_similarity=sorted(similarity.items(),key=operator.itemgetter(1),reverse=True)
	return sorted_similarity

print "Calulating.."
true_count=0  #true count will store total number of time products are successfully predicted
total=0   #total number of attempts for prediction
for userID in market_basket:  
	items=top_rating_CF(userID)
	count=0
	top_users={} #stores top 10 similar customer and their similarities
	for x,y in items:
		if count==10:
			break
		top_users[x]=y
		count+=1

	print "Top Users Find"

	users_item=[] #this will store the items of top similar customers
	for x in top_users:
		users_item.extend(market_basket[x][0])
	current_user_items=market_basket[userID][0]
	users_item=list(Set(users_item)-Set(current_user_items))  #remove the own product from list

	product_rating={} #this will store rating of each product from candidate set
	S=0
	for item in users_item:
		temp=0.0
		count=0
		for user in top_users:
			try:
				temp_rating=rating[user+' '+item]
				count+=1
			except KeyError:
				continue
			temp+=float(temp_rating)*float(top_users[user])
		try:	
			product_rating[item]=temp/count
		except ZeroDivisionError:
			continue
	count=0
	section_C=market_basket[userID][1]
	#sorted the products rating and return top n products
	product_rating=sorted(product_rating.items(),key=operator.itemgetter(1),reverse=True)
	for x,y in product_rating:
		if count==10:
			break
		if x in section_C:
			true_count+=1
			break
		count+=1
	total+=1

#this will print the accuracy of model
print "accuracy: ",float(true_count)/total
