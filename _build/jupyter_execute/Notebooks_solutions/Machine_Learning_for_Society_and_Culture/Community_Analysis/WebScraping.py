#!/usr/bin/env python
# coding: utf-8

# ## Web Scraping
# 
# The web has become a unique source of data for community analysis . Munzert et al. (2014) in their book on 'Automated data collection (...). A practical guide to web scraping and text mining' (John Wiley & Sons) emphasize in the Introduction that 'the rapid growth of the World Wide Web over the past two decades tremendously changed the way we share, collect, and publish data. Firms, public institutions, and private users provide every imaginable type of information and new channels of communication generate vast amounts of data on human behavior. What was once a fundamental problem for the social sciences — the scarcity and inaccessibility of observations — is quickly turning into an abundance of data. This turn of events does not come without problems. (…), traditional techniques for collecting and analyzing data may no longer suffice to overcome the tangled masses of data.' (p. XV). 
# 
# In short, we can find lots of data on the web. A big problem with web data is, however, that it is often inconsistent and heterogeneous. To get access to it, one often has to visit multiple web sites and assemble their data together. Finally, the data is generally published without reuse in mind, which implies that the data can be of low quality. That said, the web is so vast that it still provides an often overwhelming source of exciting data. 
# 
# Let's take a look at how we can access web data in general by scraping web sites but first let's load the relevant packages you should already be familiar with. Run the cell below.

# In[1]:


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# Staying with our example of political communities, we will scrape data on the current composition of the US Senate from Wikipedia. 
# 
# This can be a complex task and requires additional libraries. But in this case, we can rely on Pandas directly with its read_html function that does all the hard work for you. Check it at https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_html.html.
# 
# All the content on the web is presented to us in a language called HyperText Markup Language (HTML; https://en.wikipedia.org/wiki/HTML). HTML is of course a way of presenting content on the web in a universal way. It also contains so-called hyperlinks that let you jump from web content to web content. 
# 
# If you are interested in the further details of HTML, why not take some time now to visit the excellent http://www.w3schools.com/html/, which contains a lot of practical exercises to learn everything about HTML and other web technologies. 
# 
# Each document on the web is identified by a URL. We set the url to the wikipedia page of current US senators and run the code below.

# In[2]:


url = 'https://en.wikipedia.org/wiki/Current_members_of_the_United_States_Senate'


# With the read_html function of Pandas, we can read in the web content behind the URL. However, if you check the documentation you need to provide Pandas with further details.
# 
# Unfortunately, web content in HTML format is not very structured and often simply chaotic. We would like to download only the table of the page of current US Senators and need to find a so-called 'match' for read_html to choose that table from the HTML document. 
# 
# Fortunately, for us there are many existing strategies to determine exactly the HTML element we would like to select. I looked for specific names in the table that are not repeated in the rest of the wiki page. Run: `senator_wiki = pd.read_html('https://en.wikipedia.org/wiki/List_of_current_United_States_senators', match = 'Richard Shelby')`.

# In[3]:


senator_wiki = pd.read_html('https://en.wikipedia.org/wiki/List_of_current_United_States_senators', match = 'Richard Shelby')


# If it all worked as it should run the code below to create our senators dataframe.

# In[4]:


senators = senator_wiki[0]
senators.head()


# Fortunately, the data is already of fairly good quality, but we still need to clean the data a bit.
# 
# Let's do some basic cleaning, where we ignore the strange textual errors and focus on the various columns that require direct attention. Please:
# 
# (1) Create a 'Party' column from whatever name read_html has given that column. In my case, it was called Party.1

# In[5]:


senators['Party'] = senators['Party.1']


# (2) Make sure that the 'Term up' is of type int.
# 
# Transfrom the column 'Term up' into an integer column with `senators['Term up'] = senators['Term up'].astype(int)`.

# In[6]:


senators['Term up'] = senators['Term up'].astype(int)


# (3) Clean the column 'Born' to only contain the numerical age and rename it to 'Age'.
# 
# As you can see the column Born contains the age of the senator, which we would like to extract from the string. As far as we can see these are the two digits in an otherwise string of letters. So, in (age 87) it is 87. To extract the 87, we can use regular expressions with Pandas. Take a look at https://www.dataquest.io/blog/regular-expressions-data-scientists/. We need the str.extract function https://pandas.pydata.org/docs/reference/api/pandas.Series.str.extract.html, which is very powerful. Run `senators['Age'] = senators['Born'].str.extract(r'.*(\d\d)')`.
# 
# The expression with extract says to read (r) all characters in the string (.*) and look for two digits (\d\d) to return these. Regular expressions require some practice and trial and error in my experience.

# In[ ]:


senators['Age'] = senators['Born'].str.extract(r'.*(\d\d)')


# (4) Create a 'Years in Office' column that uses the information in 'Assumed office' to calculate how long the senator has served. Make sure that this column is of type int.
# 
# We first need to know which year we are currently in. We will use this to calculate the years left in office. We can use the datetime library and its now() function. Run the code below.

# In[ ]:


import datetime
year_ = datetime.datetime.now().year
year_


# The years in the office of a senator can be calculated by subtracting from year_ the year when the office was assumed. We can use our regular expression knowledge and simply look for the strings which are four consecutive numbers (\d\d\d\d) and return those. Type in `senators['Years in Office'] = year_ - senators['Assumed office'].str.extract(r'.*,.*(\d\d\d\d).*').astype(int)`. Observe that we use astype(int) to transform the extracted string into an int.

# In[ ]:


senators['Years in Office'] = year_ - senators['Assumed office'].str.extract(r'.*,.*(\d\d\d\d).*').astype(int)


# Finally, let's delete all unnecessary columns that you now changed such as 'Born' and 'Party.1'. Run the code below.

# In[ ]:


senators.drop(['Party.1', 'Born'], 1, inplace = True)
senators.head()


# Just like before, we now would like to ask questions against the dataset and explore it. 
# 
# In particular, we would like to understand the pressure on parties during the next election for the US Senate. At the time of writing, these were the 2022 elections for Congress. We could now reuse some of the strategies for exploring data in Pandas we have learned about earlier.
# 
# Let's look into the questions when their seats are up again for the senators. Create a new dataframe with copy() from senators that only contains the 'Senator', 'State', 'Party', 'Occupation(s)', 'Years in Office' and 'Term up' columns. Call it senators_seatup.
# 
# Run `senators_seatup = senators[['Senator', 'State', 'Party', 'Occupation(s)', 'Years in Office', 'Term up']].copy()`.

# In[ ]:


senators_seatup = senators[['Senator', 'State', 'Party', 'Occupation(s)', 'Years in Office', 'Term up']].copy()


# Take a look at the first couple of rows of the data, and you will only find those columns you selected.

# In[ ]:


senators_seatup.head()


# What are the types? Do you need to change them?

# In[ ]:


senators_seatup.dtypes


# In my case, they were ok. They are only strings and ints - all in the right place.
# 
# Next, we would like to determine the next time an election is held. This information is in the 'Term up' column, where it is the smallest value. Assign that value to a variable next_election and pring it out by running 
# ```
# next_election = senators_seatup['Term up'].min()
# next_election
# ```

# In[ ]:


next_election = senators_seatup['Term up'].min()
next_election


# Now, we select the rows/observations that are relevant for the next election and filter the senators_seatup rows with next_election. Assign the results to senators_seatup_next. Do you remember how to do this? If not check https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html for a quick reference.

# In[ ]:


senators_seatup_next = senators_seatup[senators_seatup['Term up'] == next_election]


# Display all the senators whose seats are up.

# In[ ]:


senators_seatup_next


# So far so good. Let's next group observations together to gain composite insights. Let's look at the senators per US state. Use senators_seatup_next and the columns 'State' and 'Term up' to display the number of terms that are up in the next election. Run `senators_seatup_next[['State', 'Term up']].groupby(['State'], as_index=False).count()`.

# In[ ]:


senators_seatup_next[['State', 'Term up']].groupby(['State'], as_index=False).count()


# At least in 2022, there were quite a few senators up for re-election. How does it look for you? 
# 
# Finally, we wanted to look into the election challenges per party. Select 'Party' and 'Term up' and group by party to display the results with count(), please. You can do it ...

# In[ ]:


senators_seatup_next[['Party', 'Term up']].groupby(['Party'], as_index=False).count()


# Republicans had  more seats to lose in 2022. You might see different results depending on the election you look at. Let's try and find out a little bit more about the senators up for re-election.  What is their median time in office if you group them by party? 
# 
# That's it for today's analysis of communities with the additional bonus of learning a little bit about how to harvest data from the web, which is already advanced stuff. Thank you ...
