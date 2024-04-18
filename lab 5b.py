#Sarah Morrison

import pandas as pd

url_to_csv = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv'

df = pd.read_csv(url_to_csv)

# 1) Create a groupby object using "clarity" and "color" as the keys
grouped = df.groupby(['clarity', 'color'])

# 2) Display the describe() output JUST for group color=E, clarity=SI2
grouped.get_group(('SI2', 'E')).describe()
# 3) Display the max value for price in each group
grouped['price'].max()
#or
grouped.apply(lambda g: g.sort_values['price'].tail(1))
# 4) Display the min value for price in each group
grouped['price'].min()

# 5) Write four different functions:
#    - one that works with map on the values in a column
#    - one that works with apply on the values in a row
#    - one that works with apply on the values in a column
#    - one that works with apply on a groupby object
def map_func(v):
    return v + 10
df['x'].map(map_func)

def apply_row_func(r):
    r['x'] = (r['x'] + r['y'] * r['z'])
    return r
def apply_col_func(c):
    return c - c.mean()
def groupby_func(g):
    g['new_col'] = g['x'] - g['y'].mean() 
    return g

df.groupby('cut').apply(groupby_func)
# 6) Display only the maximum price for each clarity.
df.groupby('clarity')['price'].max()
# 7) Stretch goal! Which clarity of diamond has the diamond that is
#    the largest outlier in size (carats) from the mean for that group?
zc = df.groupby('clarity',
                group_keys=False)['carat'].apply(
                    lambda v: (v - v.mean())/v.std())
df['zscore'] = zc
df.groupby('clarity')['zscore'].max()
