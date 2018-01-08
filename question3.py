# 3. how many times did source H report on clicks?

import pandas as pd
import numpy as np

from datetime import datetime
startTime = datetime.now()

source1 = pd.read_csv("~/Downloads/source1.csv")
source2 = pd.read_csv("~/Downloads/source2.csv")

# grab just the actions json string column from source 2 dataset
# and set up a counter to iterate the list of actions

actions=source2.iloc[:,4]
row_count=actions.shape[0]

# set up dataframe to store data converted from json strings into pandas 

list=pd.DataFrame()

# iterate list of actions and assign each to json_str, convert each json string into a
# dataframe and add it to the main list

print('\nBuilding table of sources & actions.')

for i in range(row_count):
	print('\rProcessing row ' + str(i),end='')
	json_str=actions[i]
	data=pd.read_json(json_str)
	list=pd.concat([list,data])
	
# grab a dataframe of all "clicks" actions

clicks=list[list["action"].str.contains('clicks')]

# sum column H to get number of source H reportings

H_on_clicks=int(clicks['H'].sum())

print('\n\nSource H reported on clicks ' + str(H_on_clicks) + ' times.')

print('\nCurrent time is ' + str(datetime.now()) + '  Elapsed time ' + str(datetime.now() - startTime))



