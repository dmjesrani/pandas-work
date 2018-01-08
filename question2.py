# 2. how many campaigns spent on more than 4 days?

import pandas as pd
import numpy as np

from datetime import datetime
startTime = datetime.now()

source1 = pd.read_csv("~/Downloads/source1.csv")
source2 = pd.read_csv("~/Downloads/source2.csv")

# pull just the campaign IDs from source2 into a series

campaign_IDs=source2.iloc[:,0]

# set up a dataframe to store the campaign_ids which occur on more than 4 days

cols = ['campaign_id']
morethan4 = pd.DataFrame(columns=cols)
cntr = 0

# iterate the master list of campaign IDs in the source2 dataset
# for each cid test to see if it occurs in the list more than 4 times
# if so, add that cid to a new list called morethan4

for cid in campaign_IDs:	
	matches = source2[source2["campaign_id"].str.contains(cid)]
	row_count = matches.shape[0]
	if row_count > 4:
		print('\rCID ' + cid + ' spent on more than 4 days.',end='')
		morethan4.loc[cntr,'campaign_id'] = cid
		cntr += 1
		
# remove all duplicates from the list to yield the unique ids with more than 4 occurrences 
		
uniques = pd.DataFrame()		
uniques=morethan4.drop_duplicates(['campaign_id'],keep='first')

# count the number of rows in uniques to yield the number of campaign IDs which spent on 
# more than 4 days

final_days_count=uniques.shape[0]
print('\n' + str(final_days_count) + ' campaigns spent on more than 4 days.')

print('\nCurrent time is ' + str(datetime.now()) + '  Elapsed time ' + str(datetime.now() - startTime))








