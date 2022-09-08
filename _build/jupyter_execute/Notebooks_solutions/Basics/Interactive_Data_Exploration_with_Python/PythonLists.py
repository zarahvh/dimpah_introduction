#!/usr/bin/env python
# coding: utf-8

# ## Python Lists

# This was a lot of stuff in the first lesson. Unfortunately, this is necessary but once you have learned one programming language all of this becomes quite obvious and repetitive. 
# 
# And, there is more. We need to also learn one more important concept in Python. With so-called lists, you can collect several elements in the same variable. This is immensely useful as we will see later.
# 
# Let’s try lists, which store an ordered set of values called elements. A list can contain any number of elements using brackets. Type in ```numeric_list = [1, 10, 49]``` to create a numeric list of three numbers.

# In[1]:


numeric_list = [1,10,49]


# To check that the new list exists, please type ```numeric_list```.

# In[2]:


numeric_list


# We can also create a string/characters list, with ```string_list = ['abc', 'def', 'ghi']```.

# In[3]:


string_list = ['abc', 'def', 'ghi']


# To check that the new vector exists, please type ```string_list```.

# In[4]:


string_list


# Lists are useful to, for instance, hold your poker winnings during the week. You do not play on Saturday and Sunday, but record all the other 5 days, by entering ```poker_list = [140, -50, 20, -120, 240]```. 
# 
# Thank you datacamp.com for this example! An excellent resource to learn data science things btw, but unfortunately you have to pay for it.

# In[5]:


poker_list = [140, -50, 20, -120, 240]


# You feel this is your lucky week. So, you play roulette, too. Please record your winnings with ```roulette_list =[-24, -50, 100, -350, 10]```.

# In[6]:


roulette_list =[-24, -50, 100, -350, 10]


# Because you prefer it organised, you would now like to name each of the entries. This is possible in Python with dictionaries. Please create an empty dictionary by typing ```names_poker = {}```.

# In[7]:


names_poker = {}


# To create a dictionary (which is like a named list), simply use the {} and then for each element the key to access the element comes first, then a ‘:’, and finish it with the value. 
# 
# So, in order to create a dictionary containing all your poker winnings type in ```names_poker = {'Monday': 140,'Tuesday': -50, 'Wednesday': 20, 'Thursday': -120, 'Friday': 240}```.
# 
# Dictionaries are further explained at https://www.w3schools.com/python/python_dictionaries.asp. Also a good resource to learn some more Python.

# In[8]:


names_poker = {'Monday': 140,'Tuesday': -50, 'Wednesday': 20, 'Thursday': -120, 'Friday': 240}


# Now you can access a single element with ```names_poker['Monday']```. Type it in.

# In[9]:


names_poker['Monday']


# Next, you are interested in how much you win in poker and roulette per day. 
# 
# You can simply add up all the elements in the list. Remember that we can use built-in functions? To add up elements in a list we can use the function sum, which comes directly with Python. Try it with ```sum(poker_list)```.

# In[10]:


sum(poker_list)


# And of course we can also do ```sum(roulette_list)```.

# In[11]:


sum(roulette_list)


# In order to get our total winnings per day for the week, we can simply add both lists with the Python sum function. Type in ```total_week = sum(poker_list) + sum(roulette_list)```.

# In[12]:


total_week = sum(poker_list) + sum(roulette_list)


# Print out total_week.

# In[13]:


total_week


# We have almost covered everything there is to know about lists. One more important concept is that lists are indexed. Using square brackets, we can select the first, second and third element directly with 0, 1, 2, etc. respectively. So, the index count in Python starts with 0 for the first element. The last element is then the length of the list n – 1. 
# 
# To select Monday’s poker winning (first day of the week) simply use square brackets [] and type ```poker_monday = poker_list[0]```.

# In[14]:


poker_monday = poker_list[0]


# Print out poker_monday.

# In[15]:


poker_monday


# You can also select more than one element with the colon operator. 
# 
# In order to select your winnings from Tuesday to Friday, please run ```roulette_selection_list = roulette_list[1:5]```.  The first value, left of the colon, is the first index to select (in this case Tuesday). The last value is the first index NOT to select (here an imaginary Saturday). Print out roulette_selection_list.

# In[16]:


roulette_selection_list = roulette_list[1:5]
roulette_selection_list


# This is called list slicing in Python and requires some getting used to.
# 
# If you have a list l, these are the options:
# 
# ```
# - l[start:stop]  # items start through stop-1
# - l[start:]      # items start through the rest of the array
# - l[:stop]       # items from the beginning through stop-1
# - l[:]           # a copy of the whole array
# ```
# 
# To find out about our roulette winnings from Tuesday to Friday, we can use sum again. Try ```sum(roulette_selection_list)```.

# In[17]:


sum(roulette_selection_list)


# Using the index we can also update elements in lists. 
# 
# Let’s  set the Wednesday winnings of roulette_selection_vector to 1000 with ```roulette_selection_list[1] = 1000```.

# In[18]:


roulette_selection_list[1] = 1000


# Print out  roulette_selection_list.

# In[19]:


roulette_selection_list


# Well done. Your introduction to lists (and dictionaries) is done.
