import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#The Following is data on crime from the british government website www.gov.uk .
#Find the Data here, URL:
#https://www.gov.uk/government/statistics/historical-crime-data
data = r"rec-crime-1898-2002.xls"
#Population numbers for England and Wales retrieved from Wikipedia on 2018-08-01
#Find it here, URL:
#https://en.wikipedia.org/wiki/Demography_of_England#Historical_population
#https://en.wikipedia.org/wiki/Demography_of_Wales#Historical_population
pengla = r"pop_england.xlsx"
pwales = r"pop_wales.xlsx"
#DataFrame Crime, index-time columns-typeofcrime
crime = pd.read_excel(data, index_col=1, skiprows=0,skipfooter=74 , header=5)
crime = crime.drop('HO code',axis=0)
crime = crime.dropna(axis=1,how='all')
crime = crime.dropna(axis=0,how='all')
#DataFrames Population England, index-time
print (crime.columns.values)
#region 
#popul = pd.read_excel(data2,index_col=1,skipfooter=4)
#popul = popul.dropna(axis=0,how='all')*1000.0 #raw data per 1000 inhabs
#homicide = crime[crime.columns.values[0]]
#homicide.index = map(lambda x: str(x),homicide.index)
#popul.index = map(lambda x: str(x).strip('cu'),popul.index)
#remove duplicates for reindexing
#popul2 = popul[~popul.index.duplicated()]
#popul2 = popul2.reindex(homicide.index)
#popul2 = popul2[popul2.columns.values[0]]
#percap
#percap = homicide/popul2
#percap = percap.loc[:'1994']
#percap.index = map(lambda x: int(x),percap.index)
#total crime
#totcrime = crime[crime.columns.values[-1]]
#totcrime.index = map(lambda x: str(x),totcrime.index)
#totpercap = totcrime/popul2
#totpercap = totpercap.loc[:'1994']
#totpercap.index = map(lambda x:int(x),totpercap.index)
#endangering life crime
#endcrime = crime[crime.columns.values[6]]
#endcrime.index = map(lambda x: str(x),endcrime.index)
#endpercap = endcrime/popul2
#endpercap = endpercap.loc[:'1994']#.apply(lambda x: np.log(x))
#endpercap.index = map(lambda x:int(x),endpercap.index)
#print (endpercap)
#print (percap)
#percap.plot(kind='hist',use_index = True)#,x='year',y='homicides per capita')
#plt.plot(percap.index.values, percap*1000)
#plt.plot(totpercap.index.values, totpercap*1000)
#plt.plot(endpercap.index.values, endpercap)
#plt.xticks(rotation=90)
#plt.show()
#endregion
