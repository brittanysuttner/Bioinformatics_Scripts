#This takes outfile from aai.rb with the -T option and adds the two MAGs being compared to the table
# for i in *gz; do for j in *gz; do aai.rb -1 $i -2 $j -T ${i%%.*}-${j%%.*}.out ;done; done

import csv
import pandas as pd
from os import listdir
from os.path import isfile, join

#Initialize empty dictionary and df
data={}
df = pd.DataFrame (data, columns = ['MAG1','MAG2','ANI','std_dev','proteins_used','#prots_smallest_genome'])

#make a list of all files
#open files
#obtain values from file
#append MAG1, MAG2, and values to df	
#print df to csv

#make a list of all files that have "out" in the name
mypath = '.'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) if ".out" in f]
#TODO I would like to obtain my path from the argument in the CLI (e.g. give directory to where the .out files are located)  
	
#open all the files
for filename in onlyfiles:
  #obtain arg1 and arg2 from fileName
  filename_rm_out = filename.split(".", 1)[0]
  MAG_names = filename_rm_out.split("-")
  
  with open(filename) as tsv: 
     for line in csv.reader(tsv, dialect="excel-tab"):
       value=line
       new_row = {'MAG1': MAG_names[0],'MAG2': MAG_names[1],'ANI': value[0],'std_dev': value[1],'proteins_used':value[2],'#prots_smallest_genome':value[3]}
       #append row to the dataframe
       df = df.append(new_row, ignore_index=True)
     	
# Write table to CSV file
df.to_csv("Fecal_MAGs_AAI_table.txt", index=False, sep='\t')



#data = {'MAG1': [MAG_names[0]],
#        'MAG2': [MAG_names[1]],
#        'ANI': [value[0]]
#        'std_dev': [value[1]]
#        'proteins_used':[value[2]]
#        'prots_smallest_genome':[value[3]]
#        }

## Other way to create the dataframe and write MAG_names and values AT THE END!
#data = {'MAG1': [MAG_names[0]],'MAG2': [MAG_names[1]],'ANI': [value[0]],'std_dev': [value[1]],'proteins_used':[value[2]],'prots_smallest_genome':[value[3]]}
#df = pd.DataFrame (data, columns = ['MAG1','MAG2','ANI','std_dev','proteins_used','prots_smallest_genomes'])
