#!/usr/bin/env python

from subprocess import PIPE
import sys
import subprocess

jarAddress = sys.argv[1]                #Hadoop-stream jar file address, 
inputFile = sys.argv[2]                 #input file address (local one), 
hdfsInputDir = sys.argv[3]              #input directory address(where to copy local input files in HDFS), 
hdfsOutputDir = sys.argv[4]             #output directory address(where to store the output files in HDFS),
mapperReducerDirAddress = sys.argv[5]   #address of the directory where all mappers and reducersare located.

m=0
n=0
p=0

file1 = open(inputFile, 'r')
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
		
file1=open(inputFile,'r')
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
file1.close()

inputFile='pfile.txt'
				
					

cmd = """
hdfs dfs -rm -r -f {hdfsOutputDir}
hdfs dfs -rm -r -f {hdfsInputDir}
hdfs dfs -mkdir {hdfsInputDir}
hdfs dfs -copyFromLocal {inputFile} {hdfsInputDir}
chmod 777 {mapperReducerDirAddress}/mapper.py
chmod 777 {mapperReducerDirAddress}/reducer.py

hadoop jar {jarAddress} \
-input {hdfsInputDir} \
-output {hdfsOutputDir} \
-file {mapperReducerDirAddress}/mapper.py \
-file {mapperReducerDirAddress}/reducer.py \
-mapper "python3 mapper.py" \
-reducer "python3 reducer.py"

hdfs dfs -cat {hdfsOutputDir}/part*
""".format(
    jarAddress = jarAddress,
    hdfsInputDir = hdfsInputDir,
    hdfsOutputDir = hdfsOutputDir,
    inputFile = inputFile,
    mapperReducerDirAddress = mapperReducerDirAddress
)

resp = subprocess.run(cmd, shell=True, stdout=PIPE)
print(resp.stdout.decode())
