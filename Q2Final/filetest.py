m=0
n=0
p=0

file1 = open('inputtest.txt', 'r')
line_no=1
for line in file1.readlines():
	line=line.strip()
	values=line.split()
	if line_no==1:
		m=int(values[0])
		n=int(values[1])
		
	if line_no==m+2:
		p=int(values[1])
	line_no+=1
	
file1.close()
		
print(m)
print(n)
print(p)

file1=open('inputtest.txt','r')
file2=open('pfile.txt','w')

line_no=1

mat_name='A'
i=1
j=1
for line in file1.readlines():
	line=line.strip()
	values=line.split()
	if line_no==1:
		mat_name='A'
	
	elif line_no==m+2:
		mat_name='B'
		i=1
		j=1
		
		
		
	
	else:
		while j<=len(values):
			file2.write("{},{},{},{},{},{},{},{}".format(mat_name,i,j,values[j-1],m,n,n,p))
			file2.write('\n')
			j+=1
		j=1
		#file2.write('\n')	
		i+=1
	line_no+=1
	
		
file2.close()
		
		
		
	
	



