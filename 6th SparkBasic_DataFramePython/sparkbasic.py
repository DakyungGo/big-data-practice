import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1,3,5,np.nan,6,8])
dates = pd.date_range('20170101',periods = 6)
dates

df = pd.DataFrame(np.random.randn(6,4), index = dates, columns=list('ABCD'))
df

# Create a dataframe with dates as your index
States = ['NY','NY','NY','NY','FL','FL','GA','GA','FL','FL']
data = [1.0,2,3,4,5,6,7,8,9,10]
idx = pd.date_range('1/1/2012',periods=10, freq='MS')
df1 = pd.DataFrame(data, index=idx, columns=['Revenue'])
df1['State'] = States
df1

# Create a second dataframe
data2 = [10.0, 10.0, 9, 9, 8, 8, 7, 7, 6, 6]
idx2 = pd.date_range('1/1/2013', periods=10, freq='MS')
df2 = pd.DataFrame(data2, index=idx2, columns=['Revenue'])
df2['State'] = States
df2

df = pd.concat([df1, df2])
df

# Method 1
# make a copy of original df
newdf = df.copy()

newdf['x-Means'] = abs(newdf['Revenue'] - newdf['Revenue'].mean())
newdf['1.96*std'] = 1.96*newdf['Revenue'].std()
newdf['Outlier'] = abs(newdf['Revenue'] - newdf['Revenue'].mean()) > 1.96*newdf['Revenue'].std()
newdf

# Method 2
# Group by item

# make a copy of original df
newdf = df.copy()
State = newdf.groupby('State')
State

for idx, data in State: #DataFrameGroupBy
    print (idx, data)


# Method 2
# Group by multiple item

# make a copy of original df
newdf = df.copy()

StateMonth = newdf.groupby(['State',lambda x: x.month])

newdf['Outlier'] = StateMonth.transform( lambda x: abs(x-x.mean()) > 1.96*x.std())
newdf['x-Mean'] = StateMonth.transform( lambda x: abs(x-x.mean()))
newdf['1.96*std'] = StateMonth.transform( lambda x: 1.96*x.std())
newdf


# Method 3
# Group by item

# make a copy of original df
newdf = df.copy()

State = newdf.groupby('State')

def s(group):
    group['x-Mean'] = abs(group['Revenue'] - group['Revenue'].mean())
    group['1.96*std'] = 1.96*group['Revenue'].std()
    group['Outlier'] = abs(group['Revenue'] - group['Revenue'].mean()) > 1.96*group['Revenue'].std()
    return group

Newdf2 = State.apply(s)
Newdf2

file_name = "./analyzed_american.csv"
Newdf2.to_csv(file_name)

