#!/usr/bin/env python
# coding: utf-8

# ## DataFrame Indexing

# In this part, we work towards exploring and visualising real-life datasets using Python and Pandas and query questions of racial bias in death sentences. Before we can explore real-life datasets, we need to discuss a couple of more advanced Python constructs. First, indexes of dataframes.
# 
# First, we need load the libraries Pandas and Numpy. You can run more than one statement in a cell. So, type in: 
# 
# ```
# import numpy as np 
# import pandas as pd
# ```

# In[1]:


import numpy as np 
import pandas as pd


# To introduce Pandas indexes, we will use the famous iris dataset, every data analyst will know. It contains observations about flowers/irises. The details can be found here: https://archive.ics.uci.edu/ml/datasets/iris. 
# 
# ```
# The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. 
# Attribute Information:
# 1. sepal length in cm
# 2. sepal width in cm
# 3. petal length in cm
# 4. petal width in cm
# 5. class:
# -- Iris Setosa
# -- Iris Versicolour
# -- Iris Virginica
# ```
# 
# Read up on the history of the dataset https://en.wikipedia.org/wiki/Iris_flower_data_set. It was published by a famous statistician called Ronald Fisher (https://en.wikipedia.org/wiki/Ronald_Fisher) who was also a eugenist. It is important to know about this dark history of statistics, too. Check out the Wikipedia entries for more information.
# 
# Run the following code to load iris from a library and assign it to a dataframe called df.

# In[2]:


from sklearn.datasets import load_iris

data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)


# Do you at least a little bit understand what is going on here? You access the sklearn.datasets library and then load the iris dataset before transforming it into a data frame.
# 
# You can look at the first ten observations/rows by typing in df with head(). Type in `df.head(10)`.

# In[3]:


df.head(10)


# Contemplate a bit how the plants are described. Where is the beauty of a flower? The dataframe is a good example of using features to describe observations.
# 
# Now, select the first 10 rows into a new data frame with `my_df = df.head(10)`.

# In[4]:


my_df = df.head(10)


# Next, we want to show you how to add an index to a dataframe. An index can be anything that has unique values in Pandas. First, we create such an index as an array.
# 
# The Python function range allows us to create a list of integers (a number that can be written without a fractional component). To create an array ind of 10 numbers starting from 0, run ```ind = np.array(range(0, 10))```. At the same time, also print it out. We will use ind to index the iris data frame.

# In[5]:


ind = np.array(range(0, 10))


# Let's assign a column called ind to the iris dataframe my_df. Do you remember how? Yes, it is ```my_df['ind'] = ind```. 
# 
# Also print out my_df. Ignore any warning. This is for demonstration purposes only.

# In[6]:


my_df['ind'] = ind


# You can now set the ind column to be the index of the dataframe, which will make selecting items, slicing, etc. much faster and consistent. 
# 
# Type in ```my_df.set_index('ind', inplace=True)```. And print out my_df.

# In[7]:


my_df.set_index('ind', inplace=True)


# The earlier warning came as Pandas prefers us to create an index not for a column but the whole data. 
# 
# So, let's do this again. This time, we create a new datafame directly with an index. Type in ```my_df2 = pd.DataFrame(df.head(10), index = ind)```. Print my_df2 out.

# In[8]:


my_df2 = pd.DataFrame(df.head(10), index = ind)


# This should look exactly like the start of the original iris dataframe df. Pandas automatically creates an index when you call pd.DataFrame. You could, however, make any sequence of unique values into an index. Let's give the flowers (artificial) names and index the my_df2 directly with them.
# 
# First, we create an array ```flower_names = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])```. Type it in.

# In[9]:


flower_names = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])


# Now, we recreate my_df2 with the flower_names as the index.  
# 
# First, we need to add a new column called names to the data frame with ```my_df2['names'] = flower_names```.

# In[10]:


my_df2['names'] = flower_names


# Next we can use ```my_df2.set_index('names', inplace = True)``` to update the index of my_df2. Print out my_df2.

# In[11]:


my_df2.set_index('names', inplace = True)


# With the names index, we can directly select rows for different flower names values using the .loc function. To select a single name type in ```my_df2.loc['a']```.

# In[12]:


my_df2.loc['a']


# Let's pick up two flowers. Type in ```my_df2.loc[['c','d']]```.

# In[13]:


my_df2.loc[['c','d']]


# You can also select certain columns with a second list of column names. Try ```my_df2.loc[['c','d'], ['sepal length (cm)','sepal width (cm)']]```.

# In[14]:


my_df2.loc[['c','d'], ['sepal length (cm)','sepal width (cm)']]


# You can also select ranges of index labels. Try ```my_df2.loc['c':'f']```.

# In[15]:


my_df2.loc['c':'f']


# Finally, a logical selection is also possible with an indexed dataframe directly --- not just via selectors as previously discussed. 
# 
# Try to retrieve all entries with petal width (cm) = 0.2 by typing in ```my_df2.loc[my_df2['petal width (cm)'] == 0.2]```. Yes, you have to repeat the dataframe inside the [].

# In[16]:


my_df2.loc[my_df2['petal width (cm)'] == 0.2]


# There is so much more you can do with dataframes in Pandas. One more function you will use quite a bit: value_counts(). It counts the number of times a value appears in a column. Try it with ```my_df2['petal width (cm)'].value_counts()```.

# In[17]:


my_df2['petal width (cm)'].value_counts()


# Indexing is a big topic in the Pandas world and unfortunately a bit complicated. Check out https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html. The book Python for Data Analysis is also a great reference. Its author Wes McKinney has actually created Pandas.
