# Community Detection

## Political Communities

Today, we start exploring political and social community data using a popular exploration technique with association mining like clustering. It is very effective and easy to use. We will gain some real insights about US politics as well as communities in social networking sites.

Another focus today will be to introduce you to the problems of real life social datasets, which often lack the quality to be processed easily. For instance, you will learn various strategies of dealing with missing entries either by removing them completely or by trying to replicate its values. The kind of social data we are dealing with is vast and unorganized, which makes organizing it for analysis no easy task. In reality, you will spend most of your time on working through such data challenges. 

Finally, today will be dedicated to data exploration and the insights you can gain here. Exploring data is not necessarily a very structured part of your work. 

You might remember the power of Pandas functions like head(), describe(), etc. to quickly explore essential components of data. Some people consider data exploration to be the most important part in the data analysis process, as it is really important to understand each aspect of the data and the way it is represented. In social and cultural analytics, most of our work is based on data exploration techniques rather than prediction. We will cover prediction later in the course. 

First load all the standard Pandas, etc. Python libraries, which should be familiar to you.

Run the code below.

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
%matplotlib inline

## Clustering 

In this section, we concentrate on introducing the power of digital methodologies and data exploration using a particular method called clustering, which is closely related to the understanding of political and social communities. We will look at the basics of clustering that delivers you powerful results very fast. In particular, we will use the k-means algorithm, which was invented by MacQueen in the late 1960s (https://en.wikipedia.org/wiki/K-means_clustering). Despite being ancient in terms of computer lives, k-means is still widely used as it delivers good results with great performance. Performance in computing describes the effort we need in terms of computational resources. You will generally notice performance by the execution time. 

https://machinelearningmastery.com/clustering-algorithms-with-python/ provides a good overview of clustering algorithms that are implemented in Python.

k-means tries to develop clusters by 
(1) initialising a pre-defined number (k) of randomly chosen centroids in space. Centroids are simply the centre points of clusters. 
(2) The algorithm assigns each observation to the cluster with the closest centroid. 
(3) Based on how balanced this assignment is, the centroids are recalculated and steps 1 and 2 are repeated until the algorithm balances out. 

Let's move on to some actual work.

In a first exercise, we will use k-means to understand voting behaviour in the US senate. We selected a senate that was not too partisian as we would like to investigate changing voting behaviour.

The data is a subset of the data from https://www.dataquest.io/blog/k-means-clustering-us-senators/.

Please, run the code below to create the congress_114 data frame, which contains the voting behaviour of 114th US Senate. According to Wikipedia (https://en.wikipedia.org/wiki/114th_United_States_Congress), the 114th Congress met in Washington, D.C. from 3 January 2015 to 3 January 2017, during the final two years of Barack Obama's presidency. 

The 2014 elections gave the Republicans control of the Senate (and control of both houses of Congress) for the first time since the 109th Congress. With 247 seats in the House of Representatives and 54 seats in the Senate, this Congress began with the largest Republican majority since the 71st Congress of 1929–1931. There are 23 Democrats, 1 Independent and 33 Republicans in our dataset. Please note that this does not represent the full 114th congress but a sample. 

congress_114 = pd.read_csv("https://tinyurl.com/2p8vyp99")

To warm up check the first five entries of the dataset. It contains the name of a particular senator, his/her party and home state as well as for each bill whether the senator voted for the bill (1) or against it (0). Check out the first 5 rows in congress_114 with head().

congress_114.head(5)

Next check the last five records. You know how of course ...

You will see that the last record contains lots of NaN values, which stand in Python for missing values. This is the voting record of a senator who was not able to vote. In real-life datasets, you will see quite a few of these kinds of records – maybe because they never existed or they were not recorded in the first place, etc.

congress_114.tail(5)

There are many strategies to deal with these kinds of missing records or 'dirty' data. Here, we will use the brute-force version and simply remove it from the data set. It is only one record and is completely missing. So, removing these records should be safe.

First check that there is really only one record by displaying all null entries in the dataset. Run `congress_114[congress_114.isnull().any(axis=1)]`. isnull() checks for NaN entries and any(axis=1) applies this to all columns.

congress_114[congress_114.isnull().any(axis=1)]

That's only one record missing, and the person has really not voted at all. This makes us confident that we can just delete them ...

Remove the record. The easiest is to simply remove all the records with NaN values. Pandas has a function for that. Type in `congress_114 = congress_114.dropna()`.

congress_114 = congress_114.dropna()

Check the last 5 elements again to make sure that the observation with NaN values (of the senator who missed votes) is really gone.

congress_114.tail(5)

Finally, check how many democrats, republicans and independents there are in the dataset congress_114. As you can see this is only a subset of the 100 senators. Type in `congress_114.iloc[:,2].value_counts()` to select column 3 with iloc and apply value_counts().

congress_114.iloc[:,2].value_counts()

We want to improve the content of the dataframe next and make the types fit better. To this end, we change the float types to integers. 

This is actually quite hard work in things like Pandas. You need to first select the right columns in the data frame. You could just count the column numbers, as it is a very small data frame. But there is a trick to find the indexes automatically. We match the beginnings of the column names and are only interested in those that start with "bill-". 

Check first the names of the columns to verify that there is a pattern you can exploit. Run `congress_114.columns`.

congress_114.columns

Next, use the string function startswith() to select only the 'bills-' columns. Assign them to bill_cols and print it out with:
```
bill_cols = congress_114.columns.str.startswith("bill-")
bill_cols
```

bill_cols = congress_114.columns.str.startswith("bill-")
bill_cols

With the Pandas loc function and bill_cols, you can select all the bill columns. Make them all integer columns with astype(int): `congress_114.loc[:, bill_cols] = congress_114.loc[:, bill_cols].astype(int)`.

congress_114.loc[:, bill_cols] = congress_114.loc[:, bill_cols].astype(int)

Check that everything has come out as planned by running dtypes. 

BTW, you will have noticed that string types are objects in Pandas ...

congress_114.dtypes

## Clustering with K-means

Many of the decisions in analytics are more an art than a science. We need to often estimate many parameters – either based on previous experience or using background knowledge. K-means is famous for heavily depending on k or the number of clusters we want to assign. We need to tell Python which k to use. 

In order to find a good starting point for k, we can use our own knowledge about how the US senate is structured. We would like to investigate voting clusters, and we know that the US senate is dominated by 2 major parties. So, it seems like a good idea to start with two clusters (k = 2), as we can assume that there should be two major party-based voting clusters. Please, assign k = 2.

Run the code below.

k = 2

Next, we need to understand what we would like to cluster and choose the relevant features as input into the k-means algorithm. If you look back into your earlier explorations of the dataset, you can see that the first 4 columns do not contain voting behaviour. They have the name, state, etc. of the various senators. The voting behaviour can be found in columns 5 to 19. Use either the column indexes or bill_cols to create a new dataframe congress_114_voting, which only contains the voting behaviour. Tip you need to use congress_114.loc[:, bill_cols] to create congress_114_voting. Also, print out the first couple of rows of congress_114_voting.

congress_114_voting = congress_114.loc[:, bill_cols]
congress_114_voting.head()

Great, we are ready to cluster the votes. Check out the details of k-means in the SKlearn documentation: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

Its main arguments are the dataset to cluster and the number of clusters. We can leave all the other inputs at their defaults. 

First import KMeans from sklearn.cluster by running the code below.

from sklearn.cluster import KMeans

Now, run KMeans and fit it with n_clusters  = k. Check the documentation and you will find that it is:
```
kmeans = KMeans(n_clusters  = k) 
kmeans.fit(congress_114_voting)
```

kmeans = KMeans(n_clusters  = k) 
kmeans.fit(congress_114_voting)

This should not have taken too long, as the dataset is very small. 

In the meantime, you can celebrate that you have just run a machine learning algorithm. k-means is a fairly simply one, but still a standard example of an unsupervised machine learning algorithm. Unsupervised machine learning means that you do not have to train the computer in advance about the kind of results you expect. You can also check out what that means in a wonderful Coursera/Stanford course under https://www.coursera.org/learn/machine-learning/lecture/olRZo/unsupervised-learning. The course is legendary and gives you in-depth knowledge of machine learning. 

The cluster assignments are stored as a one-dimensional NumPy array in kmeans.labels_. Here’s a look at the first five predicted labels. Run the code below.

#Keep cell

kmeans.labels_[:5]

Ok, so now that we have run our first machine learning algorithms, what do we do with the results? A good first step for k-means and other clustering algorithms is to check out the size of the clusters. Who do you expect to belong to each cluster?

Use np.bincount with kmeans.labels_, please, and run `np.bincount(kmeans.labels_)`.

np.bincount(kmeans.labels_)

These numbers show that there is not really a clear division between Republicans and Democrats, as the clusters do not correspond to the numbers each party has in the senate. 

Create a new dataframe congress_114_result, which contains the first 4 columns of congress_114 as well as the cluster assignments for each senator by kmeans. Take a moment to reflect what we gain from such a new dataframe?

Type in:
```
congress_114_result = congress_114.loc[:, np.logical_not(congress_114.columns.str.startswith('bill-'))].copy()
congress_114_result["cluster"] = pd.Series(kmeans.labels_)
```

congress_114_result = congress_114.loc[:, np.logical_not(congress_114.columns.str.startswith('bill-'))].copy()
congress_114_result["cluster"] = pd.Series(kmeans.labels_)

Because we like it tidy, we give the columns of congress_114_result new readable names. We can do this by assigning the columns directly to a list of names: `congress_114_result.columns = ['index','name','party', 'state', 'cluster']`.

congress_114_result.columns = ['index','name','party', 'state', 'cluster']

Let's take a look at the composition of  congress_114_result. This time we want to take a look at the whole congress_114_result. What do you see?

congress_114_result

Finally, let's take a look at the composition of our 2 clusters. 

In this case, we want to count how often a Democrat appears in cluster 1 or how often in cluster 2; similarly, how often is a Republican part of either cluster 1 or 2. Please note that there are also Independent senators. 

In order to compare party and cluster features, use pd.crosstab: https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html. With the crosstab function, we can count the frequency of the combination of two columns. Simply run: `pd.crosstab(congress_114_result['party'], congress_114_result['cluster'])`.

pd.crosstab(congress_114_result['party'], congress_114_result['cluster'])

Take a minute to interpret the results. Which party is more coherent in its voting behaviour? Can you identify the outliers by looking through the result data frame? 

k = 2 seems to have been a fairly good choice as there is a lot of overlap between parties and voting clusters. But if you want to practice further, why not rerun the analysis with a different k?