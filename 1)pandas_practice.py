import numpy as np
import pandas as pd

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 11)
pd.set_option('display.max_rows', 100)

df = pd.read_csv('death.csv', sep=',')

#help(pd.read_csv)

# show us only five first rows
print(df.head)

# rows x columns in this table
print(df.shape)

# names of columns 
print(df.columns)

# show us common information about this data frame
print(df.info())

# remake type of some columns in this data frame
#df['Churn'] = df['Churn'].astype('int64')

# show us statistic of data that we have
print(df.describe())

# show statistics for choosen types
print(df.describe(include=['object', 'bool']))

# counter for repetitions of some value, specially used for bool variables
print(df['Churn'].value_counts())

# try to count some mean values for this type
print(df['Area code'].value_counts(normalize=True))

# accending - for decreasing sort, by - for name of column and also by multiply parameters with list
print(df.sort_values(by=['Total day charge', 'Churn'], 
        ascending=[False, True]).head())

# mean values of columns for reason if data frame at index parameter is equal to some condition
print(df[df['Churn'] == 1].mean())

# for choose current range of searching from this matrix (loc - name indexing, iloc - indexes)
print(df.loc[0:5, 'State':'Area code'])
# if we want to pick first or last row: df[:1] or df[-1:] 

# applying function to a data frame, it also can be lambda function
print(df.apply(np.max))

# renaming values in columns with map:
#d = {'No' : False, 'Yes' : True}
#df['International plan'] = df['International plan'].map(d)
#df.head()

# renaming values in columns with replace:
#df = df.replace({'Voice mail plan': d})
#df.head()

print(pd.crosstab(df['Churn'], df['International plan'], margins=True))

