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
 
df = pd.read_excel('~/python/data/finance.xlsx', sheet_name='Sheet1')
 
#print(df)

fig= plt.figure(figsize=(16,8))
ax = plt.axes()

ax.plot(df.Date, df.Gross,linestyle='-',color='g')
ax.plot(df.Date, df.Income,linestyle='-',color='b')
plt.xticks(rotation=90)
plt.legend()
ax.set(xlabel='Date', ylabel='Amount',
       title='Finance Plot')
xticks = ax.xaxis.get_major_ticks()
i = 0
for xtick in xticks:
    if i%5:
        xtick.label1.set_visible(False)
    i = i + 1
