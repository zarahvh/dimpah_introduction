#!/usr/bin/env python
# coding: utf-8

# ## Arrays

# The next new concept is the NumPy array. You often use this construct in data analysis. We want to employ the NumPy array to filter elements in our lists and even bring them together into two dimensions. Up to now we only had one dimension, but why not add one more?
# 
# NumPy has been a long-standing toolkit for data analysis. According to https://numpy.org/, it is 'the fundamental package for scientific computing with Python'. It features heavily in what is still a standard introduction in our field: https://wesmckinney.com/pages/book.html. It is a really good book to further work on the topics that are discussed in these introductions.
# 
# First, we have to import the library numpy. You always do that in Python with import. In this case, type in ```import numpy```.

# In[1]:





# Let’s move on from our gambling and look at social media. We will now introduce an example from social analytics brought to us by [dataquest.com](http://dataquest.io/), which we will come back to again later in the course. 
# 
# You have a LinkedIn account and a Facebook account and want to find out, which one has more views and is more successful. You collected the views per day for a particular week. 
# 
# Type in ```linkedin = numpy.array([16, 9, 13, 5, 2, 17, 14])``` to record the views for LinkedIn.

# In[ ]:





# This is how you create a NumPy array directly. If you are reminded of standard Python lists, you are right. For now, NumPy arrays and lists are basically the same for us. 
# 
# Now, please create the list ```facebook_list = [17, 7, 5, 16, 8, 13, 14]```. 

# In[ ]:





# You can transform lists easily into arrays with ```facebook = numpy.array(facebook_list)```. Try it.

# In[4]:





# Print out facebook to see that it is numpy array. 

# In[ ]:





# Matrices are another important concept in data analysis. They are two-dimensional arrays. They are more commmon than you think. For instance, black and white images are such matrices. They contain a pixel value at the horizontal and vertical dimension. 
# 
# We can create a matrix called views by simply combing linkedin and facebook. Type in ```views = numpy.array([linkedin, facebook])```.

# In[6]:





# Print out views.

# In[ ]:





# With `views.shape`, you can check the shape of the matrix. It has 2 rows and 7 columns.

# In[ ]:





# We can then ask a couple of good questions against the matrix views without having to reference the arrays it is made of. 
# 
# To find out on which days we had 13 views for either LinkedIn or Facebook, we type ```views == 13```. The == is the Boolean equivalence operator.

# In[ ]:





# When are views less than or equal to 14? Try ```views <= 14```.

# In[ ]:





# How often does facebook equal or exceed linkedin views times two? This is actually a quite advanced expression already. Try it with ```sum(facebook >= (linkedin * 2))```. 

# In[ ]:





# Take a moment to think about the components of this expression. Maybe, you want to take a piece of paper and a pen to write down all the components. Hint: Boolean variables can also be thought of a 0 for False and 1 for True.
# 
# Similar to arrays, we can access each element of a matrix, but this time we of course need 2 dimensions. ``views[0][1]`` will select the first row’s second element. Try it.

# In[ ]:





# The order of indexes is row first and then column. Try `views[1][4]`.

# In[13]:





# There is much more we can do. NumPy contains a lot of support functions.
# 
# We can, for instance, reorder the social media views, so that the social media companies are the columns and the rows are the days. 
# 
# If you remember your school days, you can do change the axes in a matrix by transposing it - in Python with numpy.transpose. Simply run `views_t = numpy.transpose(views)`. Print out views_t. 

# In[ ]:





# Array and matrix are important ideas for interactive data explorations. Many of the comparisons we did in this notebook cannot be done directly with Python lists. 
# 
# In the next session, we will be introduced to the idea of data frames, which takes the matrix one step further.

# In[ ]:




