import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

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
popeng = pd.read_excel(pengla,index_col=0, skiprows=2, skipfooter=6, header=0, converters={'Pop.': lambda x: float(str(x).replace('.','').replace(',',''))})
popeng = popeng.drop(columns=popeng.columns.values[1])
popwal = pd.read_excel(pwales,index_col=0, skiprows=2, skipfooter=6, header=0, converters={'Pop.': lambda x: float(str(x).replace('.','').replace(',',''))})
popwal = popwal.drop(columns=popwal.columns.values[1])
#reindex and impute missing values by polinomial interpolation
#cdex = np.unique(np.vectorize(lambda x: str(x)[:4])(crime.index.values))
pdex = range(int(popeng.index.values[0]),int(popeng.index.values[-1])+1)
peng = popeng.reindex(pdex).interpolate(method = 'polynomial', order = 3)
pwal = popwal.reindex(pdex).interpolate(method = 'polynomial', order = 3)
ptot = peng.add(pwal)[peng.columns.values[0]]
ptot.index = map(lambda x: int(x),ptot.index)
#split up crime data old/new rules application
cro = crime.loc[:'1998/9 (old rules)',:]
crn = crime.loc['1998/9 (new rules)59':,:]
#for now we focus on the old rules
#TODO: add data for newer dates
cro = cro.drop([cro.index.values[-2]])
cro.index = np.unique(np.vectorize(lambda x: str(x)[:4])(cro.index.values)).astype(int)
#homicide
homic = cro[cro.columns.values[0]].interpolate(method = 'polynomial', order=1).ffill().bfill()
attem = cro[cro.columns.values[1]].interpolate(method = 'polynomial', order=1).ffill().bfill()
endal = cro[cro.columns.values[6]].interpolate(method = 'polynomial', order=1).ffill().bfill()
#percapita
hpc = homic/ptot[homic.index.values]
apc = attem/ptot[homic.index.values]
epc = endal/ptot[homic.index.values]
spc = hpc.add(epc.add(apc))
#plot the results
plt.plot(np.asarray(spc.index),np.asarray(hpc),label = 'Homicide')
plt.plot(np.asarray(spc.index),np.asarray(apc),label = 'Attempted Murder')
plt.plot(np.asarray(spc.index),np.asarray(epc),label = 'Serious Wounding Endangering Life')
plt.plot(np.asarray(spc.index),np.asarray(spc),label = 'SUM')
plt.xlabel('Year')
plt.ylabel('Per Capita')
plt.legend()
plt.show()


