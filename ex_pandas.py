import ex_pandas as pd
import ex_numpy as np
import ex_matplotlib.pyplot as plt


#Series
pd.Series([5775, 373, 7, 42, np.nan, 33])
pd.Series(["cubs","royals","giants","sox","giants","cards","giants","...",None])

# Datetime index
dt_index = pd.date_range(start='2015-1-1', end='2015-11-1', freq='m')
dt_series = pd.Series(data= np.random.randn(10), index = dt_index)
dt_series

# Extracyt by date
dt_series[pd.to_datetime('2015-02-28')]
dt_series['2015-02-28']

#Indexing
series_1 = pd.Series(np.random.randn(5), index = ['California', 'Alabama', 'Indiana', 'Montana', 'Kentucky'])
series_2 = pd.Series(np.random.randn(5), index = ['Washington', 'Alabama', 'Montana', 'Indiana', 'New York'])

# add Series
series_1 + series_2

#DataFrames

pd.DataFrame({'a': [1,2], 'b': [2,5], 'c': [3,6]}, index=['foo', 'bar'])

pd.DataFrame(data=[[1, 2, 3], [4, 5, 6]],
             columns=['a', 'b', 'c'],
             index=['foo', 'bar']
            )

df = pd.DataFrame(np.random.randn(10, 5), index=dt_index, columns=[x for x in 'abcde'])
df

# each dataframe column is a series:
col = df.a
type(col)

# so is each row.
row = df.loc['2015-01-31']
type(row)


# The columns all have the same index: The row names!
col.index


# What's the index for the rows? the column names!
row.index


# When one row is returned it is a Series (not a dataframe)
df.a


df['a']

# Return subset / multiple columns
df[['a','b']]


# Advanced Indexing
df.loc['2015-05-31':'2015-08-31', 'c':'e'] # Ranges by index label

df.iloc[2:-3, 2:5] # Ranges by index number.

#Fancy Indexing

dt_index = pd.date_range('2015-1-1', '2015-12-31', freq='m')
df = pd.DataFrame(np.random.randn(12,5), index=dt_index)
df.head()

# Adding new column
df['state'] = ['Alabama', 'Alaska' , 'Arizona'] * 4
df.head()

df = df.reset_index()
df.rename(columns={'index': 'date'}, inplace=True)
df = df.set_index(['state', 'date'])
df.head()

df.loc['Alabama'].head()

# this doesn't work because the date is not the primary (first) index
try:
    df.loc['2015-01-31']
except KeyError as e:
    print("ERROR: {}".format(e))

# but this does
df.loc[df.index.get_level_values('date') == '2015-01-31']

df.loc[('Alabama', '2015-01-31')] #or you can do this.


#I/O
df = pd.read_csv('data/winequality-red.csv', delimiter=';')


df.head()  #Display the first x rows (default is 5)

df.shape

df.columns


df.info()


df.describe().round(3)

df.tail()

#Boolean Masks

 # Pandas
#
#
# ## Pandas Series
# `pandas.series` are one dimensional np.ndarray vectors **with an index**

# In[24]:


pd.Series([5775, 373, 7, 42, np.nan, 33])


# In[25]:


pd.Series(["cubs","royals","giants","sox","giants","cards","giants","...",None])


# ## Datetime Index

# In[26]:


# Datetime index
dt_index = pd.date_range(start='2015-1-1', end='2015-11-1', freq='m')
dt_series = pd.Series(data= np.random.randn(10), index = dt_index)
dt_series


# In[27]:


dt_series[pd.to_datetime('2015-02-28')]
dt_series['2015-02-28']


# ## General Indexing
# - Pandas makes excellent use of informative indexes.
# - An index works like a dictionary key, enabling fast lookups of the data associated with the index.
# - Indexes also enable fast group-by, merge and time-series operations.
# - When you're really in the zone with pandas, you'll be thinking about indexes all the time.

# In[28]:


series_1 = pd.Series(np.random.randn(5), index = ['California', 'Alabama', 'Indiana', 'Montana', 'Kentucky'])
series_2 = pd.Series(np.random.randn(5), index = ['Washington', 'Alabama', 'Montana', 'Indiana', 'New York'])


# Pandas uses the index by default to align series for mathematical operations

# In[29]:


series_1 + series_2


# ## DataFrames
# `pandas.DataFrames` are set of `pandas.Series` that share the same index.
# There is more than one way to skin a cat.

# In[30]:


pd.DataFrame({'a': [1,2], 'b': [2,5], 'c': [3,6]}, index=['foo', 'bar'])


# In[31]:


pd.DataFrame(data=[[1, 2, 3], [4, 5, 6]],
             columns=['a', 'b', 'c'],
             index=['foo', 'bar']
            )


# In[32]:


df = pd.DataFrame(np.random.randn(10, 5), index=dt_index, columns=[x for x in 'abcde'])
df


# In[33]:


# each dataframe column is a series:
col = df.a
type(col)


# In[34]:


# so is each row.
row = df.loc['2015-01-31']
type(row)


# In[35]:


# The columns all have the same index: The row names!
col.index


# In[36]:


# What's the index for the rows? the column names!
row.index


# ## Slice or View of a DataFrame

# In[37]:


# When one row is returned it is a Series (not a dataframe)
df.a


# In[38]:


df['a']


# In[39]:


# Return subset / multiple columns
df[['a','b']]


# ## Advanced Indexing
# `.loc` `.iloc` and `.xi`

# In[40]:


df.loc['2015-05-31':'2015-08-31', 'c':'e'] # Ranges by index label.


# In[41]:


df.iloc[2:-3, 2:5] # Ranges by index number.


# In[42]:


df.ix[2:-3,2:5] # Tries to estimate your request -- soon to be deprecated!


# In[43]:


df.ix['2015-05-31':'2015-08-31', 'c':'e']


# DO NOT USE `.ix`
# We show it because you may see it in legacy code, and should know what it is.  But remember, in Python it is better to be explicit than implicit.

# --------------------------------------------------------------------------------------------
# ## Fancy Indexing

# In[44]:


dt_index = pd.date_range('2015-1-1', '2015-12-31', freq='m')
df = pd.DataFrame(np.random.randn(12,5), index=dt_index)
df.head()


# In[45]:


# Adding new column
df['state'] = ['Alabama', 'Alaska' , 'Arizona'] * 4
df.head()


# In[46]:


df = df.reset_index()
df.rename(columns={'index': 'date'}, inplace=True)
df = df.set_index(['state', 'date'])
df.head()


# In[47]:


df.loc['Alabama'].head()


# In[48]:


# this doesn't work because the date is not the primary (first) index
try:
    df.loc['2015-01-31']
except KeyError as e:
    print("ERROR: {}".format(e))


# In[49]:


# but this does
df.loc[df.index.get_level_values('date') == '2015-01-31']


# In[50]:


df.loc[('Alabama', '2015-01-31')] #or you can do this.


# ## IO

# In[51]:


df = pd.read_csv('data/winequality-red.csv', delimiter=';')


# In[52]:


df.head()  #Display the first x rows (default is 5)


# In[53]:


df.shape


# In[54]:


df.columns


# In[55]:


df.info()


# In[56]:


df.describe().round(3)


# In[57]:


df.tail()


# ## Boolean Masks

# In[58]:


boolean_mask = df['chlorides'] <= df.chlorides.quantile(0.01)


# In[59]:


df[boolean_mask].shape


# In[60]:


# we use masks all the time in pandas (and numpy for that matter)
df[df.chlorides <= df.chlorides.quantile(0.01)]


# In[61]:


# we can easily extend this to more conditionals in our mask
df[(df['chlorides'] >= 0.04) & (df['chlorides'] < 0.08)].head()


# In[62]:


df.groupby('quality') # Note that this returns back to us a groupby object. It doesn't actually
                      # return to us anything useful until we perform some aggregation on it.


# In[63]:


# we can also group by multilple columns by passing them in in a list.
# pandas will group by the second column within the groups created by the first groupby.
df.groupby(['pH', 'quality']).mean()['chlorides']


# ## Add / Remove Columns

# In[64]:


# compute a new feature from the data
df['pct_free_sulf'] = df['free sulfur dioxide'] / df['total sulfur dioxide']


# In[65]:


df.head()


# In[66]:


# Drop a row
df.drop('pct_free_sulf', axis=1).head()


# In[67]:


# looks like the column is gone! let's check
df.columns


# In[68]:


# huh??? The operation is not inplace by default.
df.drop('pct_free_sulf', axis=1, inplace=True)
print(df.columns)


# ## Handling Missing Values
# * http://pandas.pydata.org/pandas-docs/stable/missing_data.html

# In[69]:


miss_val_df = pd.DataFrame(
    [[1, 2, 3], [4, np.nan, 6]],
    columns=['a', 'b', 'c'],
    index=['foo', 'bar'])

miss_val_df


# When we come across a missing value, we can choose to impute or drop the missing value, or do nothing.

# In[70]:


miss_val_df.fillna(0)


# In[71]:



miss_val_df.dropna(how='any')


# In[72]:


miss_val_df.dropna(how='all')


# ## Merge
#
# Pandas supports SQL-like joins.  left, right, outer, and inner joins all work as you would expect.
# Here are lots of examples: http://pandas.pydata.org/pandas-docs/stable/merging.html

# In[73]:


df1 = pd.DataFrame(
    [[1, 2, 3], [4, 5, 6]],
    columns=['a', 'b', 'c'])

df2 = pd.DataFrame(
    [[26, 2, 25], [52, 5, 50]],
    columns=['z', 'b', 'y'])

print(df1)
print(df2)


# In[74]:


df1.merge(df2, how='inner')


# In[75]:


df3 = pd.DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    columns=['a', 'b', 'c'])


# In[76]:


df1.merge(df2).merge(df3, how='inner')


# In[77]:


df1.merge(df2).merge(df3, how='outer')


# ## Concatenate
# * adding *rows*
# * see also: df.append()

# In[78]:


df1 = pd.DataFrame(
    {'Col1': range(5), 'Col2': range(5), 'Col3': range(5)})
df2 = pd.DataFrame(
    {'Col1': range(5), 'Col2': range(5), 'Col4': range(5)},
    index=range(5, 10))


# In[79]:


df1


# In[80]:


df2


# In[81]:


# concatenate along the row index
pd.concat([df1, df2], axis=0)


# In[82]:


# concatenate along the column index
pd.concat([df1, df2], join='outer', axis=1)


# ## Conclusion
# - There a literally a billion things you can do in Pandas.
# - It is a powerful tool for exploratory data analysis, visualization and organization.
# - It is often my go-to when I start on a new dataset or a new problem.
# - Here is one of my favorite all-time pandas resources: [useful pandas snippets](https://gist.github.com/bsweger/e5817488d161f37dcbd2)
# - Now go forth and explore!














