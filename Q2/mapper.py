#!/usr/bin/python3
# -*-coding:utf-8 -*

import sys

for line in sys.stdin:
	line=line.strip()
	mat_row=line.split(',')
	dict_name=mat_row[0]
	row=int(mat_row[1])
	col=int(mat_row[2])
	val=int(mat_row[3])
	m=int(mat_row[4])
	n=int(mat_row[5])
	p=int(mat_row[7])
	if dict_name=='A':
		for k in range(1,p+1):
			print(row,end=',')
			print(k,end=',')
			print(dict_name,end=',')
			print(col,end=',')
			print(val)
			
	if dict_name=='B':
		for k in range(1,m+1):
			print(k,end=',')
			print(col,end=',')
			print(dict_name,end=',')
			print(row,end=',')
			print(val)
			
			
		
	
	
	#print(key,end='\t')
	#print(value)
	
	
