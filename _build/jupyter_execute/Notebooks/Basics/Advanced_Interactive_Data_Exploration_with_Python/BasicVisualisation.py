#!/usr/bin/env python
# coding: utf-8

# ## Plotting data

# Those last plots did look promising, didn’t they? Let’s start from the beginning and go through basic plots in Python.
# 
# To make it a bit more interesting, we return to the LinkedIn and Facebook view numbers. We would like to investigate their relationship. Let's create our Linkedin and Facebook views of the week again and also create a dataframe df to hold them. Run the code below. Do you understand what it is doing?

# In[1]:


import pandas as pd
import numpy as np

linkedin = np.array([16, 9, 13, 5, 2, 17, 14])
facebook = np.array([17, 7, 5, 16, 8, 13, 14])

df = pd.DataFrame(zip(linkedin, facebook), columns = ['LinkedIn', 'Facebook'])
df


# The earlier boxplot function came directly with the Pandas library. There are some limited plots in Pandas called basic plots: https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html. It would be easy to plot the linkedin and facebook data directly as a line plot with df.plot().

# In[ ]:





# While Pandas, plots normally provide only a quick overview of the data - in this case it is actually very good because the data is quite simple. The plot function would, however, struggle with the death penalty dataset, as it contains different types of columns.
# 
# We want more control and use the most popular libraries in Python to plot and visualise. According to https://matplotlib.org/, 'Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python'.
# 
# Next, we import Matplotlib in the standard way with import matplotlib.pyplot as plt. Run the code below.
# 
# We also need to tell Jupyter Notebook to display plots inline with the %matplotlib inline 'magic command'. We will cover more details on this when we move to advanced visualisations.

# In[2]:


import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# With the Matplotlib function plt.plot, we simply plot a Numpy array. Try `plt.plot(linkedin)`.

# In[ ]:





# That’s ok but not very pretty. Let's make it darker blue and add dots for the points with `plt.plot(linkedin, marker='o', color='blue')`.
# 
# Check out the Matplotlib documentation at https://matplotlib.org/stable/contents.html.

# In[ ]:





# Please, now type ```plt.title(‘LinkedIn’, color=‘red’, fontsize=20)``` to create a red main title of font size 20.

# In[ ]:





# Nice. But now the plot is missing. Let's add it back and run:
# 
# ```
# plt.plot(linkedin, marker='o', color='blue')
# plt.title('LinkedIn', color='red', fontsize=20)
# ```
# 
# As you can see we need to build a plot step by step ...

# In[ ]:





# Better. 
# 
# Next, we would like to compare LinkedIn and Facebook views and create a graph containing both. 
# 
# First let’s set the xlabel (x-axis label) to Days and the ylabel to views. Run:
# 
# ```
# plt.plot(linkedin, marker='o', color='blue')
# plt.xlabel('Days')
# plt.ylabel('Views')
# ```

# In[ ]:





# Let’s add the facebook graph and run:
# 
# ```
# plt.plot(linkedin, marker='o', color='blue')
# plt.plot(facebook, marker='x', color='red')
# plt.xlabel('Days')
# plt.ylabel('Views')
# ```
# 
# As said, we build a plot step by step.

# In[ ]:





# Add a title: 'LinkedIn-Facebook-Week'. Can you find out how?
# 
# (Tip: Adapt plt.title and use color='red', fontsize=20)?

# In[ ]:





# There are many more ways to improve this graph. You can, for instance, add a better x-axis description. We need to use the plt.xticks function and give it two arguments. The first is ticks, which is a list of the current labels. The second is labels, which is a list of the new labels. Easy ...
# 
# Run:
# 
# ```
# plt.plot(linkedin, marker='o', color='blue')
# plt.plot(facebook, marker='x', color='red')
# plt.xlabel('Days')
# plt.ylabel('Views')
# plt.title('LinkedIn-Facebook-week', color='red', fontsize=20)
# plt.xticks(ticks=[0,1,2,3,4,5,6], labels=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'])
# ```

# In[ ]:





# To get rid of all that additional plotting information on top, use plt.show() at the end to immediately display open figures. Run:
#     
# ```
# plt.plot(linkedin, marker='o', color='blue')
# plt.plot(facebook, marker='x', color='red')
# plt.xlabel('Days')
# plt.ylabel('Views')
# plt.title('LinkedIn-Facebook-Week', color='red', fontsize=20)
# plt.xticks(ticks=[0,1,2,3,4,5,6],labels=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'])
# plt.show()
# ```

# In[ ]:





# Finally, let us add a legend in the bottom left corner like in our original plot. We need to add plt.legend() at the end before plt.show(). Try it ...

# In[ ]:





# Much better. You could add this graph already to your presentations. It looks good enough. There are, however, a million ways to improve this even further in Python/Matplotlib. If you are interested, just search the web for all the fantastic visualisations people have created with Matplotlib. 
# 
# But, we will move on to look at how visualisations can be used with a dataframe. Remember, dataframes are the workhorses of Python, which we use in almost all our data analysis tasks.

# Let’s create a simple barplot of facebook views with a barplot using Matplotlib directly with Pandas: https://en.wikipedia.org/wiki/Bar_chart. Run ```df['Facebook'].plot.bar()```.

# In[ ]:





# And, finally let's create an advanced version by using the same as above but adding the days and a title. You can also change the colours of each bar with the color argument.
# 
# Run:
# 
# ```
# df['Facebook'].plot.bar(color=['red', 'blue', 'purple', 'green', 'lavender', 'yellow', 'orange'])
# plt.title('Facebook')
# plt.xticks(ticks=[0,1,2,3,4,5,6],labels=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'])
# plt.show()
# ```

# In[ ]:





# We can also create a stacked barplot and show both the views of facebook and linkedin using the same function as before but now adding stacked=True as an argument.
# 
# Run:
# 
# ```
# df.plot.bar(stacked=True)
# plt.title('Views')
# plt.xticks(ticks=[0,1,2,3,4,5,6],labels=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'])
# plt.show()
# ```

# In[ ]:





# That's it for our basic visualisation exercises. We will have later a session that will build on this but for now we are done with our introduction to interactive Python.

# In[ ]:




