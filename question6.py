# 6. how many source B conversions were there for campaigns targeting NY?

import pandas as pd
import numpy as np

from datetime import datetime
startTime = datetime.now()

source1 = pd.read_csv("~/Downloads/source1.csv")
source2 = pd.read_csv("~/Downloads/source2.csv")

# grab campaigns targeting NY from source1 dataset

NY_campaigns = source1[source1["audience"].str.contains("NY")]

# get those campaign IDs and generate a new list from matching them against source2

campaign_IDs = NY_campaigns.iloc[:,0]

# set up new dataframe for matches of campaign ID against source2 dataset

df2 = pd.DataFrame()

for cid in campaign_IDs:
	print('\rProcessing CID ' + cid,end='')
	matches = source2[source2["campaign_id"].str.contains(cid)]
	if not matches.empty:
		df2 = df2.append(matches)

# from that list, extract the json from the actions column into a new dataframe

actions=df2.iloc[:,4]

row_count=actions.shape[0]

# create a new dataframe for the imported json actions data

list=pd.DataFrame()

print('\nImporting json data: ')
for action in actions:
	json_str=action
	data=pd.read_json(json_str)
	list=pd.concat([list,data])
	
#create new dataframe of 'conversions'

conversions=list[list["action"].str.contains('conversions')]

# from the list of conversions, total up column for source B

B_conversions=int(conversions['B'].sum())

print('\nThere were ' + str(B_conversions) + ' source B conversions for campaigns targeting NY.')

print('\nCurrent time is ' + str(datetime.now()) + '  Elapsed time ' + str(datetime.now() - startTime))




