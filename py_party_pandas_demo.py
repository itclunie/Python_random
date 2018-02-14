import pandas as pd

df = pd.read_csv('csvpath', usecols=[0,2,3,4], skiprows=1, nrows=50) #select cols and rows you want

df['newcolname']=none #add new column