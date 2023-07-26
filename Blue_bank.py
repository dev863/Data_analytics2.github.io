# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 12:08:40 2023

@author: vaide
"""
import json 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

#to read json data
json_file = open('loan_data_json .json')
data = json.load(json_file)

#method 2 to read json data
with open('loan_data_json .json') as json_file:
    data = json.load(json_file)

#transform to data frame

loan_data = pd.DataFrame(data)

#finding unique values for the purpose column
loan_data['purpose'].unique()

#describe the data
loan_data.describe()

#describe the data for one column
loan_data['int.rate'].describe()
loan_data['fico'].describe()
loan_data['dti'].describe()

#using exp to get the annual income
income = np.exp(loan_data['log.annual.inc'])
loan_data['annualincome'] = income

#fico score

#Applying for loops to loan data 

length = len(loan_data)
ficocat = []
for x in range(0,length):
    category = loan_data['fico'][x]
    try:
        if category >=300 and category <400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 601 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 700:
            cat = 'Good'
        elif category >= 700:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
    except:
        cat = 'Unknown'
    ficocat.append(cat)
    
ficocat = pd.Series(ficocat)

loan_data['fico.category'] = ficocat 

#df.loc() as conditional statements 

loan_data.loc[loan_data['int.rate'] > 0.12,'int.rate.type'] = 'High'
loan_data.loc[loan_data['int.rate'] <= 0.12,'int.rate.type'] = 'Low'

#number of loans/rows by fico.category

catplot = loan_data.groupby(['fico.category']).size()

catplot.plot.bar(color = 'green')

plt.show()

purposecount = loan_data.groupby(['purpose']).size()

purposecount.plot.bar(color = 'red')

plt.show()

#scatter plots

ypoint = loan_data['annualincome']
xpoint = loan_data['dti']
plt.scatter(xpoint,ypoint,color = 'red')
plt.show()

#writing to csv
loan_data.to_csv('loan_cleaned.csv', index = True)
