import requests
from bs4 import BeautifulSoup
import csv
import json
import io
import sys
reload(sys)
sys.setdefaultencoding('utf8')





recharge_url='https://paytm.com/recharge'
response=requests.get(recharge_url);

body=response.text

soup=BeautifulSoup(body,"html.parser")

op_list=soup.find('div',attrs={"class":"_1lpy"}).find('ul').find_all('img')
operators=[x['title'].encode('utf-8') for x in op_list]  

my_dict={};
line_index=0;
flag=0;


for op in operators:
	cir_url='https://paytm.com/recharge/'+op+'-prepaid-mobile-online-recharge'
	#print "sending response"
	response2=requests.get(cir_url);
	#print "Response received"

	
	body2=response2.text
	
	soup2=BeautifulSoup(body2,"html.parser")
	cir_list=soup2.find('div',attrs={"class":"bRmh"}).findAll('a');
	circles=[a.text.encode('utf-8') for a in cir_list]
	print(circles)
	#offer_url='https://paytm.com/recharge/'
response3=requests.get(recharge_url)
body3=response3.text
soup3=BeautifulSoup(body3,"html.parser")
offer_list=soup3.find('script',{"id":"source"})
offer=offer_list['data-initial-state']

reply=json.loads(offer.encode('utf-8'))
residue=reply['rechargePlans']
offers=[]
for resi in residue:
	if resi['name']=='Mobile':
		for item in resi['items']:
			off=item['url'].split('/')[-1].encode('utf-8');
			
			if off not in offers:
				offers.append(off)
			else:
				break;

		#for operator in operators:
print(operators)
print(circles)
print(offers)


			

	
		

				