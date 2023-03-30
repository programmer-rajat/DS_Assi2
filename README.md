# Distributed-Systems-A2

# Q2

## Description of solution

### Input Preprocessing
1) Since each mapper will get only a chunk of input file. There is a need of input preprocessing to make sure that each mapper receives the information it needs - code for input preprocessing is written in runner script.
2) The input needs to be converted to below form. For each matrix element of both matrices : 
Matrix_name,row_index,col_index,value,total rows in matrix1, total columns in matrix1,total rows in matrix2, total columns in matrix2.

### Mapper
1) Mapper takes the pre-processed input and prints key value pairs as below : 
Here  
m=no of rows in mat 1  
n=no of columns in mat1 and no of rows in mat2  
p=no of rows in mat2  

For mat1   
for k in (0,p):  
(key,value)=((row_num,k),(Matrix_name,col_num,value))

For mat2   
for k in (0,m):  
(key,value)=((k,col_num),(Matrix_name,row_num,value))

### Reducer
1) Reducer makes two dictionaries for mat1 and mat2 based on mapper output, then sorts them on the basis of indices in value.
2) Then resultant matrix is created as per below : 
For each (i,k) key :   
    Values at same indices are multiplied and summed up.  
    This creates the final result matrix.
3) Reducer then prints the output accordingly.


### Execution instructions
1) First copy the following 4 files into namenode:  
runner_script.py,mapper.py,reducer.py,input.txt  
Example : docker cp LOCAL_PATH/mapper.py namenode:mapper.py  

2) Enter into bash using docker exec -it namenode bash.  
3) Then execute below command :  
python3 runner_script.py [command line arguments]  
Provide 5 command line arguments as given in assignment pdf.

### Results
1) We can see that the results are accurate and fast.


# Q3
## Description of solution
### Mapper 
1) Our mapper takes no of simulations as input, finds Euler's constant as per Monte Carlo method and then prints key value pairs as below : 
(key,value)=(n,no of times simulation stops at n as per Monte Carlo method)

### Reducer
1) Reducer takes mapper's output and then takes mean of n across all simulations to calculate Euler's constant.

### Results
1) Results mostly came around 2.7.
2) We ran the code for iterations [10, 100, 1000, 10000, 100000, 1000000] and got following values as Euler's constant :  
[2.4,2.71,2.735,2.7124,2.71655,2.719061]  

3) For 10 simulations(too less), the value is not that accurate.  
4) Euler's constant value vs no of simulations graph    
 ![alt text](https://github.com/programmer-rajat/testrepo/blob/main/imag2.PNG?raw=true)  
5) Scatter plot of Euler's constant value wrt number of simulations  
![alt text](https://github.com/programmer-rajat/testrepo/blob/main/imag1.png?raw=true)  









### Execution instructions
1) First copy the following 4 files into namenode:  
runner_script.py,mapper.py,reducer.py,input.txt  
Example : docker cp LOCAL_PATH/mapper.py namenode:mapper.py  
2) Enter into bash using docker exec -it namenode bash.
3) Then execute below command :  
python3 runner_script.py [command line arguments]  
Provide 5 command line arguments as given in assignment pdf.
