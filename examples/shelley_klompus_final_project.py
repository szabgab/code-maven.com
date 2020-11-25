# in this project I would like to merge 2 csv files as pandas dataframes, one has information on the reactivity of\
# antigen in our assay and the other one has the information on the biological identity of the antigen
# I will keep only 2 types of antigens: positive controls - bacterial fllagella and negative controls- random peptides\
# I will compare the reactivity of the two groups and create 2 output files: boxplot, and basic statistics of the 2 groups

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
import io
import sys
import time

startTime = time.time()

def parse_column(row):
    return str(row['uniref_func']).split(" n=")[0]

def antigen_type(row):
    if "random" in row["full name"]:
        return "negative control"
    elif "flagell" in row["parsed_func"]:
        return "flagella"
    elif "flagell" in row["full name"]:
        return "flagella"
    else:
        return ""

if len(sys.argv) < 2:
    exit("Save the two input files under the names: library_prec_passed.csv and library_uniref_funk.csv\
     and provide only the path to the directory")

#path_of_dir = '/net/mraid08/export/genie/Lab/Personal/shelley/courses/python_bootcamp/final_project'
path_of_dir = sys.argv[1]
file_input_1= 'library_prec_passed.csv'
file_input_2= 'library_uniref_funk.csv'

file_input_1_path = os.path.join(path_of_dir,file_input_1)
file_input_2_path = os.path.join(path_of_dir,file_input_2)
if not(os.path.exists(file_input_1_path or file_input_2_path)):
    exit("Save the two input files under the names: library_prec_passed.csv and library_uniref_funk.csv\
     and provide only the path to the directory")

# step 1- load the data and merge the dataframes and fill the NA with 0

df_reac = pd.read_csv(file_input_1_path,index_col="antigen_num")
df_func = pd.read_csv(file_input_2_path,index_col="antigen_num")

df_RF=pd.concat([df_reac,df_func ],axis=1)
df_RF['perc_passed'] = df_RF['perc_passed'].fillna(0)

# step 2- create a dictionary to parse the uniref_func column and merge it back to the main dataframe

df_RF['parsed_func'] = df_RF.apply(parse_column, axis=1)

# step 3- select the 2 groups: fllagella agtigens and negative controls
#df_RF.reset_index (level =0, inplace = True)
df_RF['type_of_antigen'] = df_RF.apply(antigen_type, axis=1)

#step 4- create the datafram for the output files: boxplot and basic statistics

df_toplot =df_RF.loc[df_RF["type_of_antigen"] != ""]

boxplot = df_toplot.boxplot(by = "type_of_antigen", column=["perc_passed"], grid=False)
plt.ylabel("% of reactivity")
plt.xlabel("type of antigen")
plt.title("reactivity against bacterial flagella antigens")
plt.suptitle("")
#plt.show()
fig_file_name = 'reactivity against bacterial flagella antigens.png'
stat_file_name = 'reactivity against bacterial flagella antigens statistics.csv'
df_file_name = 'flagella and random oligos df.csv'
plt.savefig(os.path.join(path_of_dir,fig_file_name))

stat = df_toplot.groupby('type_of_antigen').describe().unstack(1)
#print(stat)
stat.to_csv(os.path.join(path_of_dir,stat_file_name))
df_toplot.to_csv(os.path.join(path_of_dir,df_file_name))

executionTime = (time.time() - startTime)
print("Project is done,execution time in seconds: " + str(executionTime))