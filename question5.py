# 5. what was the total cost per view for all video ads, truncated to two decimal places?

import pandas as pd
import numpy as np

from datetime import datetime
startTime = datetime.now()

source1 = pd.read_csv("~/Downloads/source1.csv")
source2 = pd.read_csv("~/Downloads/source2.csv")

# grab campaign ids of type video from source 2

video_ads = source2[source2["ad_type"].str.contains("video")]

# add up total video ad spend

total_video_ad_spend = video_ads['spend'].sum()

print('\nTotal spent on video ads $' + '{:,.2f}'.format(total_video_ad_spend))

# use campaign ids from source2 dataset to generate new list from source1 of all video ads

campaign_IDs = video_ads.iloc[:,0]
df2 = pd.DataFrame()

for cid in campaign_IDs:
	print('\rProcessing CID ' + cid,end='')
	matches = source1[source1["campaign_id"].str.contains(cid)]
	if not matches.empty:
		df2 = df2.append(matches)
		
# add up total impressions from this list
		
total_video_ad_impressions = df2['impressions'].sum()
print('\n' + '{:,}'.format(total_video_ad_impressions) + ' Total video ad impressions.')

# divide total spend by total impressions to yield cost per view

cost_per_view=total_video_ad_spend / total_video_ad_impressions
print('Cost per video ad view is $' + '{:.2f}'.format(cost_per_view))

print('\nCurrent time is ' + str(datetime.now()) + '  Elapsed time ' + str(datetime.now() - startTime))
