## This takes outfile from aai.rb with the -T option and creates an AII matrix ##
# for i in *gz; do for j in *gz; do aai.rb -1 $i -2 $j -T ${i%%.*}-${j%%.*}.out ;done; done

import csv
import pandas as pd
from os import listdir
from os.path import isfile, join

#open file, obtain first value (ANI) from file

#Initialize empty dict and df
data={}
#Get a list of the 96 MAGs. Can be a text file that I import or extract that list somehow.
MAGs = ["cow9_15", "pig8_7"]
df_matrix = pd.DataFrame(data, columns = MAGs, index = MAGs)


#make a list of all files
mypath = '.'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) if ".out" in f]

#TODO I would like to obtain my path from the argument in the CLI  

# make a matrix directly:
for filename in onlyfiles:
  #obtain arg1 and arg2 from fileName
  filename_rm_out = filename.split(".", 1)[0]
  MAG_names = filename_rm_out.split("-")
  with open(filename) as tsv: 
     for line in csv.reader(tsv, dialect="excel-tab"):
       value= line
       df_matrix[MAG_names[0]][MAG_names[1]]=value[0]
       
       
#write arg1, arg2, and value to dataframe
df_matrix.to_csv("Fecal_MAGs_AAI_matrix.txt", index=True, sep='\t')