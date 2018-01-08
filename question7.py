# 7. what combination of state and hair color had the best CPM?

import pandas as pd
import numpy as np

from datetime import datetime
startTime = datetime.now()

source1 = pd.read_csv("~/Downloads/source1.csv")
source2 = pd.read_csv("~/Downloads/source2.csv")


# calculate CPM for each state & hair color combo

# get all unique state & hair color combos into a list

states=['AK','AL','AR','AZ','CA','CO','CT','DC','DE','FL','GA','HI','IA','ID','IL','IN','KS','KY','LA','MA','MD','ME','MI','MN','MO','MS','MT','NC','ND','NE','NH','NJ','NM','NV','NY','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VA','VT','WA','WI','WV','WY']
colors=['white','red','brown','black','pink','purple','green','blue','orange']

# build list of all possible state & hair color combos

all_combos=[]
for state in states:
	for color in colors:
		combo=state+'_'+color
		all_combos.append(combo)
		
# set up new data frame for total impressions, indexed by combo
		
impressions_by_combo = pd.DataFrame(columns=['impressions'],index=[all_combos])

print('\n\nBuilding table of total impressions by combo.')

for combo in all_combos:
	matches = source1[source1["audience"].str.contains(combo)]
	if not matches.empty:
		impressions_by_combo.loc[combo]=matches['impressions'].sum()
	
# set up new data frame for total ad spend, indexed by combo

ids=pd.DataFrame()
ad_spend_by_combo = pd.DataFrame(columns=['spend'],index=[all_combos])

print('\nBuilding table of total spending by combo.')

for combo in all_combos:
	id_matches = source1[source1["audience"].str.contains(combo)]
	if not id_matches.empty:
		ids=ids.append(id_matches)
	for cid in id_matches['campaign_id']:
		print("\rProcessing CID " + cid, end='')
		spend_matches=source2[source1["campaign_id"].str.contains(cid)]
		ad_spend_by_combo.loc[combo]=spend_matches['spend'].sum()
print('\n')

# set up new data frame for CPM, indexed by combo

CPM_by_combo = pd.DataFrame(columns=['CPM'],index=[all_combos])

print('\nBuilding table of CPM by combo.')

for combo in all_combos:
	total_spending=ad_spend_by_combo.loc[combo]
	ts=int(total_spending.iloc[0])
	total_impressions=impressions_by_combo.loc[combo]
	ti=int(total_impressions.iloc[0])
	CPM = (ts / ti) * 1000
	CPM_by_combo.loc[combo]=CPM
	
print(CPM_by_combo.sort_values(by=['CPM']))

# sort the list of CPM by state/hair combo in ascending order of CPM

CPM_sorted=pd.DataFrame()
CPM_sorted=CPM_by_combo.sort_values(by=['CPM'])


for item in CPM_sorted.index[0]:
	print('\nThe combination of ' + str(item) + ' had the best CPM.')
  

print('\nCurrent time is ' + str(datetime.now()) + '  Elapsed time ' + str(datetime.now() - startTime))


	
	

		
	


		






