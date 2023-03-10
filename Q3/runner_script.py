#!/usr/bin/env python

from subprocess import PIPE
import sys
import subprocess

jarAddress = sys.argv[1]                 
inputFile = sys.argv[2]                 
hdfsInputDir = sys.argv[3]               
hdfsOutputDir = sys.argv[4]             
mapperReducerDirAddress = sys.argv[5]   

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
