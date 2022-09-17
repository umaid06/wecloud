import os
import os.path
import glob
import pandas as pd

cur_dir = os.getcwd()

#print(cur_dir)

joined_list = []

for name in glob.glob(cur_dir+'/*.csv'):
	if "all_years.csv" not in name:
		#print(name)
		joined_list.append(name)

#joined_list = glob.glob(cur_dir+'/*.csv')

#print(joined_list)

df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
#print(df)

df.to_csv(cur_dir+'/all_years.csv', index=False)