# 1. what was the total spent against people with purple hair?

import pandas as pd
import numpy as np

from datetime import datetime
startTime = datetime.now()

# set up dataframes for each source

source1 = pd.read_csv("~/Downloads/source1.csv")
source2 = pd.read_csv("~/Downloads/source2.csv")


# extract a dataframe of only those served to with purple hair

purple_hair_dataframe = source1[source1["audience"].str.contains("purple")]

# pull only campaign_id column from purple_hair_dataframe into iterable list

campaign_IDs = purple_hair_dataframe.iloc[:,0]

# set up dataframe for match results against source2 dataset

df2 = pd.DataFrame()

# iterate campaign_id column and match against all in source2 dataset

for cid in campaign_IDs:
	print('\rProcessing CID ' + cid,end='')
	matches = source2[source2["campaign_id"].str.contains(cid)]
	if not matches.empty:
		df2 = df2.append(matches)
		
# df2 holds all source2 dataset match results for each campaign_id
# sum the spend column to get total spent on serving ads to people with purple hair.

total_spend_purple_hair = df2['spend'].sum()

print('\n\n$' + '{:,.2f}'.format(total_spend_purple_hair) + ' spent on ads served to people with purple hair.')

print('\nCurrent time is ' + str(datetime.now()) + '  Elapsed time ' + str(datetime.now() - startTime))

		

