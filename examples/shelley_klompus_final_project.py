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

df_RF.reset_index (level =0, inplace = True)
func_dict = {}
for i in range(len(df_RF)):
    oligo = df_RF.iloc[i]['antigen_num']
    func= df_RF.iloc[i]['uniref_func']
    func = str(func).split(" n=")[0]
    func_dict.update({oligo:func})

df_func = pd.DataFrame.from_dict(func_dict, orient='index')
df_func.columns = ['parsed_func']

df_RF.set_index('antigen_num', inplace = True)
df_RF=pd.concat([df_RF,df_func],axis=1)

# step 3- select the 2 groups: fllagella agtigens and negative controls
df_negative= df_RF.loc[df_RF["full name"].str.contains("random")]
df_negative["type_of_antigen"] = "negative control"


df_flag = df_RF.loc[(df_RF["parsed_func"].str.contains("flagell",na=False)) | (df_RF["full name"].str.contains("flagell",na=False))]
df_flag["type_of_antigen"] = "flagella"

#step 4- create the datafram for the output files: boxplot and basic statistics

df_toplot =pd.concat([df_flag,df_negative ],axis=0)

boxplot = df_toplot.boxplot(by = "type_of_antigen", column=["perc_passed"], grid=False)
plt.ylabel("% of reactivity")
plt.xlabel("type of antigen")
plt.title("reactivity against bacterial flagella antigens")
plt.suptitle("")
#plt.show()
fig_file_name = 'reactivity against bacterial flagella antigens.png'
stat_file_name = 'reactivity against bacterial flagella antigens statistics.csv'
plt.savefig(os.path.join(path_of_dir,fig_file_name))

stat = df_toplot.groupby('type_of_antigen').describe().unstack(1)
stat.to_csv(os.path.join(path_of_dir,stat_file_name))

print("project is done")

