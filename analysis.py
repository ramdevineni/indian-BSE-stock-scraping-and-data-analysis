
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import style
#changing local directory to csv file location
os.chdir('E:\\auto')
#reading prices of BSE Auto companies on 26/nov/2019 interval 1min
df=pd.read_csv('26novprice.csv')
#df
#getting % change in price with respect to initial value of day and adding data 
#to new dataframe
df_percentage=pd.DataFrame()
for i in df.columns[1:]:
    df_percentage[i]=(df[i]-df[i][0])/df[i][0]*100
#plt.show()
df_percentage.describe()
#removing motherson, bosch as they are outliers in BSE Auto 
df1=df_percentage.drop(['Motherson_Sumi','Bosch'],axis=1)
#getting the correlation of %change in price with other companies
sns.heatmap(df1.corr())
df1.describe()

style.use('fivethirtyeight')
plt.figure(figsize=(12,12))
df1.plot(lw=2)
plt.xlabel('time from 9:15am(step=1min)')
plt.ylabel('%change in price')
plt.legend(bbox_to_anchor=(1,1))
plt.savefig('%price change over the day.jpeg')
#df1['Apollo_Tyres'].plot()

#reading volume of BSE Auto companies on 26/nov/2019
df2=pd.read_csv('26novvolume.csv')
'''
analysing the values of volume, %error of apollo tyres company 
to understand trend in vol and % change in price in day
'''
y_axis_1=(df2['Apollo_Tyres']/1e+5)
y_axis_2=df1['Apollo_Tyres']
'''
defining x axis in step of 1 min from 9:15 to 3:32
'''
x=range(len(df1.index))
plt.plot(x,y_axis_1,label='volume in lakhs')
plt.plot(x,y_axis_2,label='% change in price')
plt.legend()
plt.xlabel('time from 9:15AM ,step =1 min')
plt.savefig('apollo.png')




