result_dict={}
result_dict[(1,2)]=1
result_dict[(1,1)]=2
result_dict[(2,1)]=3
result_dict[(2,2)]=4
myKeys = list(result_dict.keys())
myKeys.sort()
print(result_dict)
result_dict = {i: result_dict[i] for i in myKeys}
print(result_dict)

for (i,k) in result_dict:
	print(i,end=',')
	print(k,end=',')
	print(result_dict[(i,k)])
