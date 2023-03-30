#!/usr/bin/python3
# -*-coding:utf-8 -*

import sys

A_dict={}
B_dict={}
result_dict={}
for line in sys.stdin:
	line=line.strip()
	mat_row=line.split(',')
	i=int(mat_row[0])
	k=int(mat_row[1])
	mat_name=mat_row[2]
	j=int(mat_row[3])
	val=int(mat_row[4])
	if mat_name == 'A':
		if (i,k) in A_dict:
			A_dict[(i,k)].append((j,val))
		
		if (i,k) not in A_dict:
			A_dict[(i,k)]=[(j,val)]
			
					
	if mat_name=='B':
		if (i,k) in B_dict:
			B_dict[(i,k)].append((j,val))
		
		if (i,k) not in B_dict:
			B_dict[(i,k)]=[(j,val)]
			
			
#print(A_dict)
#print(B_dict)	
for (i,k) in A_dict:		
	A_dict[(i,k)]=sorted(A_dict[(i,k)],key=lambda a:a[0])
	
for (i,k) in B_dict:
	B_dict[(i,k)]=sorted(B_dict[(i,k)],key=lambda b:b[0])
	
#print(A_dict)
#print(B_dict)

for (i,k) in A_dict:
	j=0
	total=len(A_dict[(i,k)])
	while j<total:
		if (i,k) in result_dict:
			result_dict[(i,k)]+=(A_dict[(i,k)][j][1])*(B_dict[(i,k)][j][1])
	
		if (i,k) not in result_dict:
			result_dict[(i,k)]=(A_dict[(i,k)][j][1])*(B_dict[(i,k)][j][1])
		j+=1
		

#myKeys = list(result_dict.keys())
#myKeys.sort()
#final_dict = {i: result_dict[i] for i in myKeys}

num_rows=sorted(result_dict.keys())[-1][0]
#print(sorted(result_dict.keys()))
num_cols=sorted(result_dict.keys())[-1][1]
#print(num_rows)
#print(num_cols)
final_ans=[]
for i in range(num_rows):
	temp_list=[]
	for j in range(num_cols):
		temp_list.append(0)
	final_ans.append(temp_list)

#print(len(final_ans))
for (i,k) in sorted(result_dict.keys()):
	#print(i,end=',')
	#print(k,end=',')
	#print(result_dict[(i,k)])
	#row_list=[]
	#row_list.append(result_dict[(i,k)])
	#print(i-1)
	#print(k-1)
	final_ans[i-1][k-1]=result_dict[(i,k)]
	
	#print(val)

for i in final_ans:
	for j in i:
		print(j,end=" ")
	print()
	
	








		
		
		
	
