#!/usr/bin/python3
# -*-coding:utf-8 -*
import random  
import sys 
# numpy.random.uniform() method
sim_N=0
for line in sys.stdin:
	line=line.strip()
	numbers=line.split()
	sim_N=int(numbers[0])

#print(sim_N)
ans_dict={}	
min_n=0
for i in range(sim_N):
	n=1
	sum1=0.0
	while True:
		number=random.uniform(0,1)
		sum1+=number
		
		#print(sum1)
		if sum1>1.0:
			if n in ans_dict:
				ans_dict[n]+=1
			else:
				ans_dict[n]=1
			#min_n+=n
			break
		n+=1

for key in ans_dict:
	print(key,end='\t')
	print(ans_dict[key])
#print(float(min_n)/float(sim_N))

