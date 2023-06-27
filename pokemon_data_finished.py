#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv')

# print(df.head(3))

print(df)


# In[10]:


# read the headers

print(df.columns)



# In[12]:


# read each column
print(df['Name'[0:7]])


# In[14]:


#read each row
print(df.head)
#print(df.iloc[1]) - to see what is that one specific location


# In[15]:


#read a specific location
print(df.iloc[2,1])


# In[18]:


df.loc[ df['Type 1'] == "Fire" ]


# In[19]:


df.loc[ df['Type 1'] == "Grass" ]


# In[21]:


df.describe()


# In[22]:


df.sort_values('Name')


# In[23]:


df.sort_values('Name', ascending=False)


# In[27]:


df.sort_values( ['Type 1', 'HP'] )


# In[28]:


df.head(5)


# In[34]:


df['Total']= df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

df.head(5)
#  another way to see the total is to manually add the numbers
# to drop the column df = df.drop(columns+['Total'])


# In[40]:


#cols = df.columns.values
#df = df[cols[0:4] + [cols[-1]]+cols[4:12]]

#df.head(5)


# In[41]:


#df.to_csv('modified.cvs')


# In[45]:


df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') ]


# In[50]:


new_df =df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & df['HP'] > 70 ]

new_df


# In[51]:


#new_df.to_csv(filtered.csv)


# In[52]:


df.loc[df['Name'].str.contains('Mega')]
# df.loc[~df['Name'].str.contains('Mega')] This ~ means that I am looking for data that does not have "Mega" included in the name 


# In[56]:


df.loc[df['Type 1'] == 'Fire', 'Type 1'] == 'Flamer'

df.tail(15)


# In[58]:


df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = 'TEST VALUE'

df


# In[60]:


#df = pd.read_csv('modified.csv')

#df


# In[63]:


df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False)


# In[64]:


df.groupby(['Type 1']).sum()


# In[65]:


for df in pd.read_csv('https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv', chunksize=5):
    print('CHUNK DF')
    print(df)


# In[ ]:




