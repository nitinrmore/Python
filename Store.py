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

warnings.simplefilter("ignore")



def csv_to_mysql(datadf, host, user, password):
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
            sql = "INSERT IGNORE INTO MyFinance.Store\
                    SET StoreId = "+str(row[0])+",\
                    StoreName = '"+row[1]+"',\
                    CategoryId = "+str(row[2])+";"
            cursor.execute(sql)
            #print(sql)

    
        print('Succuessfully loaded the table from csv.')
        con.close()
        
    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)

# Execution Example
#load_sql = "LOAD DATA LOCAL INFILE '/Users/nitinrmore/Downloads/CreditCard1.csv' INTO TABLE MyFinance.CreditLoadTemp FIELDS TERMINATED BY ',' ENCLOSED BY '"' IGNORE 1 LINES;"
load_sql = ""
data = pd.read_csv('Data/Store.csv')


host = 'localhost'
user = 'root'
password = 'mysqlroot#1'
csv_to_mysql(data, host, user, password)