#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys 

min_n=0
total_sim=0

'''
for line in sys.stdin:
	line = line.strip()
	numbers=line.split()
	min_n+=int(numbers[0])
	count+=1
	
print(float(min_n)/float(count))

'''
for line in sys.stdin:
	line=line.strip()
	n,count=line.split('\t',1)
	n=int(n)
	count=int(count)
	min_n+=n*count
	total_sim+=count
	
print(float(min_n)/float(total_sim))
	
	

