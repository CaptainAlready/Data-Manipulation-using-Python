import pandas as pd
import csv
import re
import array as arr
import matplotlib.pyplot as plt
import mysql.connector
 
 
#filter by 4 year span
def InfoByYear(y,x,df):
if(y - x == 48):
 for i in range (x,y):
  a.append(i)
 df = df.iloc[:,a]
else: print("Den prokeitai gia diasthma tesarwn xronwn\n")
return df
 
 
 
#INPUT OF DESIRED DATASET
ex = False
while ex == False:
flag = input("Select dataset :\n1)Arrivals at tourist accommodation establishments\n2)Arrivals of non-residents at tourist accommodation establishments\n3)Nights spent at tourist accommodation establishments\n4)Nights spent by non-residents at tourist accommodation establishments\n")
#pass the tsv files to pandas dataframes
if flag == str("1"):
  df1 = pd.read_table('Arrivals at tourist accommodation establishments')
  ex = True
elif flag == str("2"):
  df2 = pd.read_table('Arrivals of non-residents at tourist accommodation establishments')
  ex = True
elif flag == str("3"):
 df3 = pd.read_table('Nights spent at tourist accommodation establishments')
 ex = True
elif flag == str("4"):
 df4 = pd.read_table('Nights spent by non-residents at tourist accommodation establishments')
 ex = True
else:
 print("Invalid selection")
 
val = input("Select country aside from greece : ")
 
 
 
#collect the data for EL and another country
if flag == str("1"):
  df1 = df1.loc[df1['c_resid,unit,nace_r2,geo\\time'].str.endswith("EL") | df1['c_resid,unit,nace_r2,geo\\time'].str.endswith(val)]
elif flag == str("2"):
  df2 = df2.loc[df2['unit,nace_r2,partner,geo\\time'].str.endswith("EL") | df2['unit,nace_r2,partner,geo\\time'].str.endswith(val)]
elif flag == str("3"):
  df3 = df3.loc[df3['c_resid,unit,nace_r2,geo\\time'].str.endswith("EL") | df3['c_resid,unit,nace_r2,geo\\time'].str.endswith(val)]
elif flag == str("4"):
  df4 = df4.loc[df4['unit,nace_r2,partner,geo\\time'].str.endswith("EL") | df4['unit,nace_r2,partner,geo\\time'].str.endswith(val)]
 
 
 
#GET YEAR SPAN
a = arr.array('i', [0])
val1 = input("Enter starting YEAR|MONTH|MONTHNUMBER ex: 2021M01 : ")
val2 = input("Enter final YEAR:  ")
 
 
#GET YEAR INDEX
if flag == str("1"):
   x = df1.columns.get_loc(val1 + " ")
   y = df1.columns.get_loc(val2 + " ")
elif flag == str("2"):
   x = df2.columns.get_loc(val1 + " ")
   y = df2.columns.get_loc(val2 + " ") 
elif flag == str("3"):
   x = df3.columns.get_loc(val1 + " ")
   y = df3.columns.get_loc(val2 + " ")
elif flag == str("4"):
   x = df4.columns.get_loc(val1 + " ")
   y = df4.columns.get_loc(val2 + " ")
 
 
 
#GET DESIRED INFO INTO PANDAS DATA
if flag == str("1"):
  df1 = InfoByYear(y,x,df1)
elif flag == str("2"):
  df2 = InfoByYear(y,x,df2)
elif flag == str("3"):
  df3 = InfoByYear(y,x,df3)
elif flag == str("4"):
  df4 = InfoByYear(y,x,df4)
 
#GET DATA FOR PLOTING
 
if flag == str("1"):
  alexis = df1.loc[df1['c_resid,unit,nace_r2,geo\\time'] == str("TOTAL,NR,I551-I553,EL")]
  alexis2 = df1.loc[df1['c_resid,unit,nace_r2,geo\\time'] == str("TOTAL,NR,I551-I553," + val)]
elif flag == str("2"):
   alexis = df2.loc[df2['unit,nace_r2,partner,geo\\time'] == str("NR,I551-I553,WORLD,EL")]
   alexis2 = df2.loc[df2['unit,nace_r2,partner,geo\\time'] == str("NR,I551-I553,WORLD," + val)]
elif flag == str("3"):
   alexis = df3.loc[df3['c_resid,unit,nace_r2,geo\\time'] == str("TOTAL,NR,I551-I553,EL")]
   alexis2 = df3.loc[df3['c_resid,unit,nace_r2,geo\\time'] == str("TOTAL,NR,I551-I553," + val)]
elif flag == str("4"):
   alexis = df4.loc[df4['unit,nace_r2,partner,geo\\time'] == str("NR,I551-I553,WORLD,EL")]
   alexis2 = df4.loc[df4['unit,nace_r2,partner,geo\\time'] == str("NR,I551-I553,WORLD," + val)]
 
 
 
#LISTS FOR PLOTING
ELxdatalist = []
ELydatalist = []
OTHERxdatalist = []
OTHERydatalist = []
 
 
#GET COLUMNS
for i in range(1,y-x + 1):
ELxdatalist.append(alexis.columns[i])
OTHERxdatalist.append(alexis2.columns[i])
 
 
#GET VALUES OF COLUMNS
for i in range(len(ELxdatalist)):
 d = ELxdatalist[i]
 d2 = OTHERxdatalist[i]
 ELydatalist.append(alexis.iloc[0][d])
 OTHERydatalist.append(alexis2.iloc[0][d2])
 
 
#ELIMINATE UNRELATED CHARS FOR EL
for i  in range(len(ELydatalist)):
  if ":" in ELydatalist[i]: ELydatalist[i] = 0
  else:
    IntVar = int("".join(filter(str.isdigit, ELydatalist[i])))
    ELydatalist[i] = IntVar
 
 
#ELIMINATE UNRELATED CHARS FOR OTHER COUNTRY
for i  in range(len(OTHERydatalist)):
  if ":" in OTHERydatalist[i]: OTHERydatalist[i] = 0
  else:
    IntVar = int("".join(filter(str.isdigit, OTHERydatalist[i])))
    OTHERydatalist[i] = IntVar
 
 
 
#export to csv
if flag == str("1"):
  csvel = df1.loc[df1['c_resid,unit,nace_r2,geo\\time'].str.endswith("EL")]
  csvother = df1.loc[df1['c_resid,unit,nace_r2,geo\\time'].str.endswith(val)]
elif flag == str("2"):
  csvel = df2.loc[df2['unit,nace_r2,partner,geo\\time'].str.endswith("EL")]
  csvother = df2.loc[df2['unit,nace_r2,partner,geo\\time'].str.endswith(val)]
elif flag == str("3"):
  csvel = df3.loc[df3['c_resid,unit,nace_r2,geo\\time'].str.endswith("EL")]
  csvother = df3.loc[df3['c_resid,unit,nace_r2,geo\\time'].str.endswith(val)]
elif flag == str("4"):
  csvel = df4.loc[df4['unit,nace_r2,partner,geo\\time'].str.endswith("EL")]
  csvother = df4.loc[df4['unit,nace_r2,partner,geo\\time'].str.endswith(val)]
 
csvel.to_csv('EL', index = True , header = True , sep = "\t")
csvother.to_csv(val, index = True , header = True , sep = "\t")
 
 
 
#create database
from pandas.io import sql
import pymysql
from sqlalchemy import create_engine
 
mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password=""
)
mycursor = mydb.cursor()
mycursor.execute("DROP DATABASE mydatabase")
mycursor.execute("CREATE DATABASE mydatabase")
 
csvel.columns = csvel.columns.str.strip()
csvother.columns = csvother.columns.str.strip()
engine = create_engine("mysql+pymysql://root:@localhost/mydatabase")
csvel.to_sql('EL', engine, index=False)
csvother.to_sql(val, engine, index=False)
#NAME OF DATABASE: mydatabase
#execute on mySql with SELECT * FROM table_name\G
 
 
 
#Ploting the figures
plt.figure("EL",figsize=(10,10))
plt.plot(ELxdatalist, ELydatalist)
plt.xticks(rotation=90)
 
if flag == str("1"):
  plt.title('Arrivals at tourist accommodation establishments in EL')
elif flag == str("2"):
   plt.title('Arrivals of non-residents at tourist accommodation establishments in EL')
elif flag == str("3"):
  plt.title('Nights spent at tourist accommodation establishments in EL')
elif flag == str("4"):
  plt.title('Nights spent by non-residents at tourist accommodation establishments in EL')
 
plt.figure('DE',figsize=(10,10))
plt.plot(OTHERxdatalist,OTHERydatalist)
plt.xticks(rotation=90)
if flag == str("1"):
  plt.title('Arrivals at tourist accommodation establishments in ' + val)
elif flag == str("2"):
   plt.title('Arrivals of non-residents at tourist accommodation establishments in ' + val)
elif flag == str("3"):
  plt.title('Nights spent at tourist accommodation establishments in ' + val)
elif flag == str("4"):
  plt.title('Nights spent by non-residents at tourist accommodation establishments in EL ' + val)
 
plt.show()
