#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:06:20 2019

@author: nitinmore
"""

import pymysql
import pandas as pd
import sys
import warnings
import matplotlib.pyplot as plt

warnings.simplefilter("ignore")
host = 'localhost'
user = 'root'
password = 'mysqlroot#1'



def mysql_to_df(query, host, user, password):
    '''
    The function creates a dataframes from the result of SQL
    in MySQL database.
    '''
    try:
        con = pymysql.connect(host=host,
                                user=user,
                                password=password)
        print('Connected to DB: {}'.format(host))
        
        df = pd.read_sql(query, con)
        #df_cat = pd.read_sql('select * from MyFinance.Category', con)
        
        print('Dataframes has been created successfully')
        con.close()
        
        return df

    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)

'''
# Execution Example
sql = 'Select * From MyFinance.CreditLoad_STG'
file_path = '/Users/nitinrmore/Downloads/CreditCard1.csv'
'''
query = 'select * from MyFinance.Store'

df_store = mysql_to_df(query,host, user, password)
#print(df_store)
#print(df_cat)

def csv_to_mysql(datadf,cardname, host, user, password):
    '''
    This function load a csv file to MySQL table according to
    the load_sql statement.
    '''
    try:
        con = pymysql.connect(host=host,
                                user=user,
                                password=password,
                                autocommit=True,
                                local_infile=1)
        print('Connected to DB: {}'.format(host))
        # Create cursor and execute Load SQL
        cursor = con.cursor()
        
        
        for index,row in datadf.iterrows():
            #print(type(hash(row[0]+str((row[1]))+row[4])))
            StoreId = 0
            CategoryId = 0
            for indexstore,rowstore in df_store.iterrows():
                if row[2].replace("'","").find(rowstore[1]) >= 0:
                    StoreId = rowstore[0]
                    CategoryId = rowstore[2]
                    break
            #print(StoreId,CategoryId)
            amount = str(row[1]*-1) if cardname =='CO' else str(row[1])
            #print(amount)
            sql = "INSERT IGNORE INTO MyFinance.CreditLoad_STG\
                    SET idCreditLoad_STG = '"+str(hash(row[0]+str((row[1]))+row[2]))+"',\
                    TransDate = '"+row[0]+"',\
                    TransAmount = '"+amount+"',\
                    TransDesc = '"+row[2].replace("'","")+"',\
                    StoreId = '"+str(StoreId)+"',\
                    CategoryId = '"+str(CategoryId)+"',\
                    CardName = '"+cardname+"';"
            cursor.execute(sql)
            #print(sql)

    
        print('Succuessfully loaded the table from csv.')
        con.close()
        
    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)

def mysql_update(datadf, host, user, password):
    '''
    This function load a csv file to MySQL table according to
    the load_sql statement.
    '''
    try:
        con = pymysql.connect(host=host,
                                user=user,
                                password=password,
                                autocommit=True,
                                local_infile=1)
        print('Connected to DB: {}'.format(host))
        # Create cursor and execute Load SQL
        cursor = con.cursor()
        
        recordcount = 0
        for index,row in datadf.iterrows():
            #print(type(hash(row[0]+str((row[1]))+row[4])))
            StoreId = 0
            CategoryId = 0
            for indexstore,rowstore in df_store.iterrows():
                if row[2].replace("'","").find(rowstore[1]) >= 0:
                    StoreId = rowstore[0]
                    CategoryId = rowstore[2]
                    recordcount=recordcount+1
                    break
            print(row[2])
            #print(StoreId,CategoryId)
            sql = "UPDATE MyFinance.CreditLoad_STG\
                    SET StoreId = "+str(StoreId)+",\
                    CategoryId = "+str(CategoryId)+"\
                    WHERE idCreditLoad_STG = '"+row[0]+"';"
                    
            cursor.execute(sql)
            #print(sql)

    
        print('Succuessfully updated {} records.'.format(recordcount))
        con.close()
        
    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)
        

fileload = 0

if fileload == 1:
    data = pd.read_csv('Data/CreditCard1.csv')
    cardname = 'WF'
    dataWF = data.filter(['Date','Amount','Desc'],axis=1)
    csv_to_mysql(dataWF,cardname, host, user, password)
    #print(dataWF)
    
    data = pd.read_csv('Data/Chase.csv')
    dataC = data.filter(['Post Date','Amount','Description'],axis=1)
    cardname = 'C'
    csv_to_mysql(dataC,cardname, host, user, password)
    
    data = pd.read_csv('Data/CapitalOne.csv')
    dataCO = data.filter(['Posted Date','Debit','Description'],axis=1)
    cardname = 'CO'
    #print(dataCO)
    csv_to_mysql(dataCO,cardname, host, user, password)

queryC = 'select * from MyFinance.CreditLoad_STG where StoreId = 0'
dfc = mysql_to_df(queryC,host, user, password)
print('{} records needs to be updated.'.format(len(dfc)))

mysql_update(dfc,host, user, password)

query = 'select str_to_date(TransDate,"%m/%d/%y") TransDate,TransDesc,\
        TransAmount*-1 TransAmount,StoreName,CategoryName,CardName,\
        DATE_FORMAT(str_to_date(TransDate,"%m/%d/%y"),"%Y-%m") YearMonth\
        from MyFinance.CreditLoad_STG cr\
        inner join MyFinance.Store s on cr.storeid = s.storeid\
        inner join MyFinance.Category c on cr.categoryid = c.categoryid order by 1;'
df_credit = mysql_to_df(query,host, user, password)
dfs = df_credit.groupby(['YearMonth'])['TransAmount'].sum().reset_index()
df = df_credit.groupby(['CategoryName','YearMonth'])['TransAmount'].sum().reset_index()
#df.unstack().plot(kind='bar',stacked=True)
df_credit.groupby(['CategoryName','YearMonth'])['TransAmount'].sum().unstack().plot(kind='bar',stacked=True)
#plt.yticks([])
plt.show()
df_credit.groupby(['CardName','YearMonth'])['TransAmount'].sum().unstack().plot(kind='bar',stacked=True)
#plt.yticks([])
plt.show()
print(df)
#df = df[df['YearMonth']=='2019-05']
#print(df_credit)
# gca stands for 'get current axis'
#ax = plt.gca()
#df.plot(kind='bar',x='CategoryName',y='TransAmount',ax=ax)


#print(df)
print(dfs)