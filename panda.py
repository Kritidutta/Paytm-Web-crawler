
import csv
import pandas as pd
import numpy as np


df=pd.read_csv('output.csv');
df['Country_geo_code']='IN';


if df['Operator'].any()=='Airtel':
	df['Operator_MCC']=23
#elif:
                                                                                                                             





df['Is 2G']=df['Description'].str.contains('\b2G\b').astype(int)
df['Is 3G']=df['Description'].str.contains('\b3G\b').astype(int)
df['Is 4G']=df['Description'].str.contains('\b4G\b').astype(int)
df['Currency']='INR'

if df['Category'].any()=='roaming':
	df['Is Roaming']=0;
	
else:
	df['Is Roaming']=1;
df['Is International Roaming']=~df['Description'].str.contains('IR|International Roaming|UNLIMITED FREE|ISD Pack').astype(int)

#df['Data Amount']=df['Description'].str.extractall(r'([0-9]+(\.[0-9][0-9]?)?\s?GB|[0-9]+(\.[0-9][0-9]?)?\s?MB)').groupby(level=0).apply(lambda x: ','.join(x[0]).replace(' ',''))

#print(type(df['Data Amount']))
df['Price']=df['Price'].str.extract(r'([0-9]{1,4})').astype(int)

if df['Validity'].any()=='1 Day':
	df['Is data limit one day']=True
else:
	df['Is data limit one day']=False


df_postquota=df['Description'].str.extract(r'([0-9]*?\s?kbps)')
df['Post_Quota_speed']=df_postquota.str.extract(r'([0-9]{1,4})');
df['Post_Quota_speed']=df['Post_Quota_speed'].fillna('0')
df['Post_Quota_speed'].astype(int)

df['Post_Quota_speed_unit']=df_postquota.str.extract(r'([a-zA-Z]+)');

df['Validity_unit']=df['Validity'].str.extract(r'([a-zA-Z]+)');
df['Validity']=df['Validity'].str.extract(r'([0-9]{1,4})');
df['Validity']=df['Validity'].fillna('0');
df['Validity'].astype(int)

df['Day_data_limit']=df['Description'].str.extract(r'((?i)\d+(?:\.\d{1,2})?\s?[MG]B(?=\s+(?:\S+\s+){0,2}day\b))')
print df['Day_data_limit']





#df['Post_Quota_speed_unit'].str.split('k')[1]
#print df3
#print df['Post_Quota_speed']
#print df['Post_Quota_speed_unit']

#df.to_csv('dummy.csv')


#df.to_csv('clean.csv')












