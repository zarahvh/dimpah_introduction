# Interactive Data Exploration with Python

## Data Frames

The most important structure in Python to store and process data are ‘data frames’. 

The library to do so is Pandas that is a key part of our work. It is another library just like numpy. With `import pandas as pd`, we tell Python to use the acronym pd for accessing pandas operations. This way we avoid having to type in pandas all the time. 

Try `import pandas as pd`.

import pandas as pd

Before we continue, we need to recreate the data from the last session. Please run the code below.

import numpy

linkedin = numpy.array([16, 9, 13, 5, 2, 17, 14])
facebook = numpy.array([17, 7, 5, 16, 8, 13, 14])
views = numpy.array([linkedin, facebook])
views_t = numpy.transpose(views)

Just like matrixes, data frames also have rows and columns but can hold different types of variables in each of their columns. 

Think about it for a moment. The power! This way, we can record any observation in the world. Any observation will have different attributes we associate with it. For instance, flowers can be of different types and colours. With data frames we can record each observation of flowers by recording it in rows and assign to the columns the various features we observe like colour, type, etc. This way the whole world is for us to record in data frames!

In order to get our week together into a single data frame, we create `my_week_df = pd.DataFrame(views_t, columns = ['Facebook', 'LinkedIn'])`. To create my_week_df, first the DataFrame function from Pandas (pd) is called with the transposed views. It is given the columns attribute with a list of names for the columns. 

my_week_df = pd.DataFrame(views_t, columns = ['facebook', 'linkedin'])

Print out my_week_df.

my_week_df

Just like matrixes, we can select rows and columns. For that, we need the operator iloc[row][column]. We need to use the Pandas iloc function here but otherwise it is the same principle as for lists and arrays. 

Select row 1, column 2 with `my_week_df.iloc[0][1]`. Please note, that this function uses [] brackets instead of (). I guess they wanted to give it the numpy feel.

my_week_df.iloc[0][1]

Do you remember how to select multiple elements in a list? 

It is similar for data frames. In order to select row 1 and 2, type in `my_week_df.iloc[0:2][:]`. This means that the first colon operator selects everything between its first index and the second index – 1. The second colon operator uses : to select all columns.

my_week_df.iloc[0:2][:]

You can also leave out the [:]. Run `my_week_df.iloc[1]` to select the second row.

my_week_df.iloc[1]

Any idea how to select the second column rather than a row? Take a look at https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html, and you will find out that it is `my_week_df.iloc[:, 1]`. Try it.

my_week_df.iloc[:, 1]

Do you know how to select the third and forth row?

my_week_df.iloc[3:5, :]

You can also select the facebook column directly with `my_week_df['facebook']`. 

my_week_df['facebook']

If you use two [[ ]], you get back a new dataframe. Try `my_week_df[['facebook']]`.

my_week_df[['facebook']]

Let's add another column to our dataframe, which we call 'happy' for our happy days in the week.

First define a list `happy = [False, True, False, True, False, True, False]`.

happy = [False, True, False, True, False, True, False]

We can then append this list to the dataframe by naming a new column and assign happy to it. Run ``my_week_df['happy'] = happy``.

my_week_df['happy'] = happy

Print out my_week_df.

my_week_df

Say, we would like to select all days, we were happy. We first define a selector series for the happy days with `happy_days = df['happy'] == True`. Remember the numpy arrays? This is very similar.

happy_days = my_week_df ['happy'] == True

Print out happy_days.

happy_days

It is a 'Series' of Booleans. Series is yet another term for lists and arrays. Pandas calls single columns things like that. I know there are lots of names here ...

Now, we use the Boolean selector to create `happy_days_df = df.loc[happy_days]`.

happy_days_df = my_week_df.loc[happy_days]

It looks complicated but it is actually just a combination of statements we already know. Take some time and look at the expression happy_days_df. What kind of parts can you identify? How are the rows/days selected when you were happy?

Print out happy_days_df.

happy_days_df

If you would like to select all the days/rows when you had more views on LinkedIn than Facebook, you can proceed in a similar way. First define the selector with `small = my_week_df['linkedin'] > my_week_df['facebook']`.

small = my_week_df['linkedin'] > my_week_df['facebook']

Then, create a new data frame with `small_df = my_week_df.loc[small]`.

small_df = my_week_df.loc[small]

Print out small_df.

small_df

That’s almost it for data frames. 

I promise they get more interesting once we start working with real data. One more thing you often want to do is to sort a data frame according to one of its columns. We have another Pandas function for that called sort_values. Run `sorted_df = my_week_df.sort_values(by=['facebook'])` to sort my_week_df by the values in the facebook column.

sorted_df = my_week_df.sort_values(by=['facebook'])

Print out sorted_df.

sorted_df

That’s it for the most important concepts around data frames in Python. 

Next, we move on to some real-life datasets and more advanced data exploration.

