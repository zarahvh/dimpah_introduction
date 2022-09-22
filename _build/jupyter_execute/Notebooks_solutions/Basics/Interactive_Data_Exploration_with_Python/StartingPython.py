#!/usr/bin/env python
# coding: utf-8

# ## Starting with Python interactively

# This is an introduction to the programming language Python where we focus on interactive data exploration. There are lots of other more general introductions to Python as well. If you are interested in Python as a programming language, why not try one of the many online environments that help you learn it? We like the Code Academy course https://www.codecademy.com/learn/learn-python but there are many more.

# A notebook is split into cells. You can run each cell with code by clicking on the arrow/Run in the top menu. Go to the next cell and click on it. Then, click on arrow/Run in the menu and you should see 4 + 3 = 7 as an output.

# In[1]:


4 + 3


# Now, let’s try it yourself by typing in ```12 - 5``` into the cell below. And then click on arrow/Run again.

# In[2]:


12 - 5


# This works a little like a calculator from your school days.
# 
# Brackets can be used to indicate that operators in the sub-expression take precedence - just like at school math. Try typing in ```(5 * 3) - 4```.

# In[3]:


(5 * 3) - 4


# All this is very similar to what you know from calculators. But computers can process many other symbols as well. Other important symbols include ‘strings’, which you know as words. These can be any number of characters like a, b, c, etc. but also -, 1 or & count as characters.
# 
# Let’s try this ... 
# 
# Please, type ```'Hello World'``` into the next cell. The quotation marks indicate that this is a string. You could also use ```"Hello World"```.

# In[4]:


'Hello World'


# What do you see when you enter ```type('string')```?

# In[5]:


type('string')


# There are many more types, which we will cover throughout the course. Check out https://realpython.com/python-data-types/ for an overview.
# 
# Booleans are another important type. They evaluate whether an assumption is True or False. Please, type ```4 < 5```. What do you get back?

# In[6]:


4 < 5


# Another concept that discriminates programming languages from calculators are variables. They are basically names for places in the computer’s memory where we can store things. We create variables with the Python assignment operator ```=```. 
# 
# Let’s try that and assign the value 5 to the variable my_apples. Please, type in ```my_apples = 5```.

# In[7]:


my_apples = 5


# Well done. 
# 
# Now print out my_apples. Just type ```my_apples```.

# In[8]:


my_apples


# Numbers in Python are generally either integers (those without a floating point) or floats (those with a floating point). Check out https://docs.python.org/3/library/stdtypes.html for an overview of all the different numerical types in Python.
# 
# Now let’s try to assign two variables.
# 
# Type ```my_oranges = 6```.

# In[9]:


my_oranges = 6


# You have created two variables my_apples and my_oranges.
# 
# Just like numbers we can add two numerical variables. Please try it with ```my_apples + my_oranges```.

# In[10]:


my_apples + my_oranges


# We can also assign the result to a new variable my_fruit. Please type ```my_fruit = my_apples + my_oranges```.

# In[11]:


my_fruit = my_apples + my_oranges


# To check that the new variable exists, please enter ```my_fruit```.

# In[12]:


my_fruit


# But we can only combine variables of the same type. Please assign the string 'six' to my_oranges with ```my_oranges = 'six'```.

# In[13]:


my_oranges = 'six'


# Now let’s try and ‘add’ my_apples and my_oranges. Type ```my_apples + my_oranges``` and you will get an error. 

# In[14]:


my_apples + my_oranges


# Variables are very important in any programming language. 
# 
# A final key idea for this first session is the function. It is  a predefined set of commands. On your calculator you can, for instance, use the inv function to get the inverse of a number. Python also has a lot of pre-defined functions like inv. But in any programming language you can also define your own functions. We will come back to this later in much more detail. For now, we focus on how to use functions.
# 
# In Python, functions are called with arguments in brackets. They are often found in extra libraries that are basically collections of functions. More on that also later ...
# 
# Please run ```round(9.5)``` to run the built-in math function round in Python. You should get 10. round is the function name and 9.5 is the only 'argument' as the input into functions is called.

# In[19]:


round(9.5)


# That's already it for the first session. Lots of ideas that will help you with getting into Python. You will get used to them with practice. Why not try now to look at https://www.codecademy.com/learn/learn-python to practice.

# In[ ]:




