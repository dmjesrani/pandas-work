# 4. which sources reported more "junk" than "noise"?

import pandas as pd
import numpy as np

from datetime import datetime
startTime = datetime.now()

source1 = pd.read_csv("~/Downloads/source1.csv")
source2 = pd.read_csv("~/Downloads/source2.csv")

#more_junk_than_noise=pd.DataFrame()

# grab just the actions json string column from source 2 dataset

actions=source2.iloc[:,4]

# get row count to set up counter

row_count=actions.shape[0]

# set up dataframe for conversion of json data

list=pd.DataFrame()

# iterate list of actions, appending each json string to the new dataframe

print('\nImporting json data: ')
for i in range(row_count):
	json_str=actions[i]
	data=pd.read_json(json_str)
	list=pd.concat([list,data])
	print('\rProcessing row ' + str(i),end='')
		
# make new dataframes, one for reports on junk, one for reports on noise

junk=list[list["action"].str.contains('junk')]
noise=list[list["action"].str.contains('noise')]

# init list of sources

sources=['A','B','C','D','E','F','G','H','J','K']

# iterate list of sources, testing each for junk vs. noise 

print('\n')
for source in sources:
	Ajunk=int(junk[source].sum())
	Anoise=int(noise[source].sum())
	if Ajunk > Anoise:
		print('Source ' + source + ' reported more junk than noise.')
		
print('\nCurrent time is ' + str(datetime.now()) + '  Elapsed time ' + str(datetime.now() - startTime))
	




