#!/usr/bin/env python
# coding: utf-8

import urllib.request
auto = "https://www.moneycontrol.com/markets/indian-indices/top-bseauto-companies-list/20?classic=true"
page = urllib.request.urlopen(auto)

from bs4 import BeautifulSoup as soup
page_html=page.read()
page.close()
S = soup(page_html,'html.parser')

#print(S.prettify())

table=S.findAll("table",{"class":"responsive"})
print("auto")

table1=table[0]
rows=table1.findAll("tr")
#print(len(rows))
head_row=rows[0]
head_columns=head_row.findAll("th")
#print(len(head_columns))
# for head in head_columns:
#     print(head.text)
#getting current time from datetime library
from datetime import datetime
import pandas as pd
t=datetime.now()
#adding first column time 
last_price_list=[t.strftime('%X')]
volume_price_list=[t.strftime('%X')]
column=['time']

for row in rows[1:]:
    columns=row.findAll('td')
    column.append(columns[0].text.replace(' ','_'))
    try:
        #converting str to string and replacing ',' in price & volume with '' and converting to float
        last_price_list.append(float(columns[1].text.replace(' ','').replace(',','')))
    except:
        #making value as zero incase no numeric data is present in cell
        last_price_list.append(0.)
    try:
        volume_price_list.append(float(columns[3].text.replace(' ','').replace(',','')))
    except:
         volume_price_list.append(0.)
print(len(last_price_list))
time=datetime.now()
df_price=pd.DataFrame(data=[last_price_list],index=[time.strftime("%X")],columns=column)
#print(df1)
try:
    #reading prev csv file
    df3=pd.read_csv('26novprice.csv')
    #print(df3)
    # adding present time step data  
    frames1=[df3,df_price]
    #print(frames1)
    # concating two dataframes
    result1=pd.concat(frames1)
    #print(result1)
    result1.to_csv('26novprice.csv',index=None)
except:
    #for the first runcase in day csv is empty 
    df_price.to_csv('26novprice.csv')

df_volume=pd.DataFrame(data=[volume_price_list],index=[time.strftime("%X")],columns=column)
#print(df2)
try:
    df4=pd.read_csv('26novvolume.csv')
    #print(df4)
    frames2=[df4,df_volume]
    #print(frames2)
    result2=pd.concat(frames2)
    #print(result2)
    result2.to_csv('26novvolume.csv',index=None)
except:
    df_volume.to_csv('26novvolume.csv')
# repeat the process each min by using windows task scheduler 

    
    


# # In[7]:




# # t=datetime.now()
# # for row in rows[1:]:
# #     columns=row.findAll('td')
# #     try:
# #         float(columns[5].text.replace(' ','').replace(',',''))
# #         print("float")
# #     except:
# #         print(type(0.))


# # In[8]:


# # df1.to_csv('file.csv',index=None)
# # df2.to_csv('file1.csv',index=None)


# # In[ ]:




