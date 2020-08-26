#!/usr/local/pacerepov1/python/3.6/bin/python
## This takes outfile from aai.rb with the -T option and creates an AII matrix ##
# for i in *gz; do for j in *gz; do aai.rb -1 $i -2 $j -T ${i%%.*}-${j%%.*}.out ;done; done

### Takes as input a list of the MAG names obtained from echo ${i%%.*} ####
### don't forget to change the names of the MAGs file and the output Matrix as needed ###

import csv
import pandas as pd
from os import listdir
from os.path import isfile, join

#open file, obtain first value (ANI) from file

#Initialize empty dict and df
data={}
#Import text file that has list of all the MAGs.
MAGs = []
with open('MAGs_for_python.txt') as MAGfile:
   for line in csv.reader(MAGfile, dialect="excel-tab"):
      MAGs.append(line[0])
#print(MAGs)
df_matrix = pd.DataFrame(data, columns = MAGs, index = MAGs)
print(df_matrix.head())


#make a list of all files that end in ".out"
mypath = '.'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) if ".out" in f]

for filename in onlyfiles:
  #obtain arg1 and arg2 from fileName
  filename_rm_out = filename.split(".", 1)[0]
  MAG_names = filename_rm_out.split("-")
  #print(MAG_names)
#Make matrix directly
  with open(filename) as tsv:
     for line in csv.reader(tsv, dialect="excel-tab"):
       value = line
       df_matrix[MAG_names[0]][MAG_names[1]]=value[0]
print(df_matrix.head())

#write arg1, arg2, and value to dataframe
df_matrix.to_csv("Fecal_D7_MAGs_AAI_matrix.txt", index=True, sep='\t')
