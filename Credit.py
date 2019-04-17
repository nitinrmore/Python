#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 18:02:24 2019

@author: nitinmore
"""
"""
import xlrd 

loc = ("~/python/data/finance.xlsx")

wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
# For row 0 and column 0 
print(sheet.cell_value(0, 0))
"""
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib.pyplot as plt
 
dfm = pd.read_excel('~/python/data/finance.xlsx', sheet_name='Credit')
df = dfm.groupby('MonYY')['Amount Updated'].sum().reset_index(name ='TotalAmount')
dfg = dfm[dfm.ExpenseType == 'Grocery'].groupby('MonYY')['Amount Updated'].sum().reset_index(name ='GroceryAmount')
dff = dfm[dfm.ExpenseType == 'Food'].groupby('MonYY')['Amount Updated'].sum().reset_index(name ='FoodAmount')
dfu = dfm[dfm.ExpenseType == 'Utility'].groupby('MonYY')['Amount Updated'].sum().reset_index(name ='UtilityAmount')

#dft = [df,dfg,dff,dfu]
dft = pd.merge(df,dfg,on='MonYY')
dft = pd.merge(dft,dff,on='MonYY')
dft = pd.merge(dft,dfu,on='MonYY')
#df.rename(index=str, columns={"Mon-YY": "MonYY"})
print(dft) 
#print(df)

fig= plt.figure(figsize=(10,6))
ax = plt.axes()

ax.plot(dft.MonYY, dft.TotalAmount,linestyle='-',color='g')
ax.plot(dft.MonYY, dft.GroceryAmount,linestyle='-',color='b')
ax.plot(dft.MonYY, dft.FoodAmount,linestyle='-',color='r')
ax.plot(dft.MonYY, dft.UtilityAmount,linestyle='-',color='y')
plt.xticks(rotation=90)
plt.legend()
ax.set(xlabel='MonYY', ylabel='Amount',
       title='Finance Plot')
"""
xticks = ax.xaxis.get_major_ticks()
i = 0
for xtick in xticks:
    if i%5:
        xtick.label1.set_visible(False)
    i = i + 1
"""
