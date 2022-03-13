#!/usr/bin/env python
# coding: utf-8

# # Advanced Interactive Data Exploration with Python
# 
# ## Little Control Structures

# We will soon come back to real-life datasets. But before that we need to introduce a few more aspects from Python, the programming language, which you might need in data analysis tasks. This part is probably least about interactive data exploration but is common to all programming languages.
# 
# The first topic are control structures. Control structures execute a piece of code based on a condition. You can recognize them in most programming languages by the keyword if. In Python, they look like the following:

# In[1]:


medium = 'LinkedIn'

if (medium == 'LinkedIn'):
    print('Showing LinkedIn information')


# The first statement creates a variable medium with 'LinkedIn' as a value. The control structure starts with if, then uses a condition to evaluate to a Boolean (medium == 'LinkedIn'), followed by a colon. The statement to execute follows in the next line.  print('Showing LinkedIn information') will print out if the condition is met.
# 
# Important: Observe the indentation, which is a way of telling Python that a group of statements belongs together as a block. Blocks can be regarded as the grouping of statements for a specific purpose. Python really does not like it if you mess with its indentation. Check https://www.dummies.com/programming/python/how-to-indent-and-dedent-your-python-code/.

# Now, also assign ```num_views = 14```.

# In[2]:


num_views = 14


# Let’s try to confirm whether we are popular with ```if num_views > 15``` then print `'You are very popular!'` How do you do it?

# In[3]:


if (num_views > 15):
    print('you are very popular!')


# You can combine Boolean expressions/conditions also logically. The keyword 'and' stands for a logical and, while 'or' stands for the logical or in Python. 
# 
# Try the logical combination and and type in:
# 
# ```
# if (num_views > 15) and (medium == 'LinkedIn'):
#     print('You are popular on LinkedIn!')
# ```
# 
# Explain the results!

# In[4]:


if (num_views > 15) and (medium == 'LinkedIn'):
    print('You are popular on LinkedIn!')


# Finally, you can also tell the computer to do other work if the condition is not fulfilled. You need to use the keyword else. Run the code below and opserve the indentation ...

# In[5]:


if (num_views > 15) and (medium == 'LinkedIn'):
    print('Condition met.')
    print('You are popular on LinkedIn!')
else:
    print('Condition not met.')
    print('Try to be more visible!')


# Another important concept in Python data analysis are for-loops. They are used for iterating over a sequence (like a list or even a secquence of letters or a string). The code below shows the syntax. Try it.

# In[6]:


for letter in 'LinkedIn':
    print(letter)


# For-loops can be very useful to perform repeated operations on collections of data, which is something we often want to do. So, for instance, loops could be used to get the square of each element in a list/array. Or, we could use them to calculate the average value of a numeric column in a data frame, etc.
# 
# The next cell introduces the ```for l in list``` construct, which is a short form for going through elements in a list. Run the following to square each number in our list ind and observe the code:
# 
# ```
# import numpy as np
# 
# ind = np.array(range(0, 10))
# for i in ind:
#     print(i**2)
# 
# ```
# 
# ```i**2``` is the power-operator in Python.

# In[7]:


import numpy as np

ind = np.array(range(0, 10))
for i in ind:
    print(i**2)


# However numpy also has easier operators to apply functions to the entire array at once, which is why we often prefer using it over standard Python. 
# 
# Run ```np.square(ind)``` and admire the simplicity. 

# In[8]:


np.square(ind)


# Here, numpy is simply amazing and super fast. 
# 
# Let's say we want to take the average of our linkdin and facebook views. First load the social media data again by running the code below.

# In[9]:


linkedin = np.array([16, 9, 13, 5, 2, 17, 14])
facebook = np.array([17, 7, 5, 16, 8, 13, 14])


# Now run ```np.average(linkedin)``` to get the average of the LinkedIn array.

# In[10]:


np.average(linkedin)


# To add 2 to each element in a numpy array we simply type the name of the array + 2. Try ```facebook + 2```.

# In[11]:


facebook + 2


# You can also combine these arrays to get one exciting average count for all our social media with `np.average(facebook + linkedin)`.

# In[12]:


np.average(facebook + linkedin)


# You can also play with numpy's other functions such as np.char.str_len. This counts the number of character for each entry in the flower_names list. 
# 
# Run 
# ```
# flower_names = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
# np.char.str_len(flower_names)
# ``` 
# and find out that ...

# In[13]:


flower_names = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
np.char.str_len(flower_names)


# The outcome is not very surprising given that we made up the names of each flower and were so lazy to just use one letter each.
# 
# What happens if you type in ```np.char.upper(flower_names)```?

# In[14]:


np.char.upper(flower_names)


# For our final example, run ```np.size(flower_names)```.

# In[15]:


np.size(flower_names)


# This returns obviously the lengths of flower_names. After this exercusion, let's return next to real-life datasets.

# In[ ]:




