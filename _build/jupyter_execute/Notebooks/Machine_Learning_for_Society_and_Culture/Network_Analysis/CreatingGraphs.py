#!/usr/bin/env python
# coding: utf-8

# ## Graphs from Data

# In this session, we would like to start digging into the details of (social) network analysis. Let’s use a famous example from the past. Zachary’s karate club is a social network of friendships of 34 members of a karate club at a US university in the 1970s. It is described in W. W. Zachary, An information flow model for conflict and fission in small groups, Journal of Anthropological Research 33, 452-473 (1977). It is a famous early example of successful social network analysis. According to Wikipedia, ‘during the study a conflict arose between the administrator and instructor, which led to the split of the club into two. Half of the members formed a new club around the instructor members from the other part found a new instructor or gave up karate. Based on collected data Zachary assigned correctly all but one member of the club to the groups they actually joined after the split.’ https://en.wikipedia.org/wiki/Zachary%27s_karate_club. Let's see whether we can recreate this analysis.
# 
# First we load some of the libraries we are always using. Run the code below.

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as plt


# Now to the main star of this show, which is the networkx library: https://networkx.org/. 
# 
# Load this commonly used network library with `import networkx as nx`.

# In[2]:


import networkx as nx 


# You have two dataframes  in the environment. 
# 
# The first is karate_nodes, which contains the nodes of the network with information about the karate club members. Run the code below.

# In[3]:


karate_nodes = pd.read_csv("https://tinyurl.com/2p9byesa")
karate_nodes.head()


# The second dataframe karate_edges contains the edges with information whether one member likes another and by how much (weight). Run the code below.

# In[4]:


karate_edges = pd.read_csv("https://tinyurl.com/mtmwc8hd")
karate_edges.head()


# Now, let’s create a graph with these these edges and nodes. Each graph is just that, a collection of edges and nodes. In our case, we can easily create the graph from the edge list in karate_edges. The networkx command is:
# ```
# G = nx.from_pandas_edgelist(karate_edges, source = "from", target = "to", create_using=nx.DiGraph(), edge_attr = True)
# ```
# 
# The first argument is the dataframe, the second the source node, the third is the target node. We also tell from_pandas_edgelist to create a directed graph with create_using=nx.DiGraph() and to keep all the edge attributes with edge_attr = True.

# In[ ]:





# Unfortunately, it is not very easy to add all the attributes of the nodes. https://newbedev.com/networkx-setting-node-attributes-from-dataframe explains how this is done by creating first a dictionary of dictionaries from karate_nodes.
# 
# Type in: `node_attr = karate_nodes.set_index('id').to_dict('index')`. This will first set the index of karate_nodes to the ids of all nodes. to_dict will then add the row values as another dictionary. 
# 
# Check out how this looks for a row by adding `node_attr[2]`.

# In[ ]:





# To set all the node attributes, now run `nx.set_node_attributes(G, node_attr)`.

# In[ ]:





# With `print(nx.info(G))`, you print out information about the graph. 

# In[ ]:





# `G.nodes()` provides a view of nodes.

# In[ ]:





# `G.edges()` provides a view of edges.

# In[ ]:





# Let's check that we added the attributes correctly with `G.nodes.data()`.

# In[ ]:





# To get the age of node 1, type `G.nodes[1]['age']`.

# In[ ]:





# There are a lot of options here and it is good at this moment to check out the documention. To get only edges linked to nodes 1 and 3, type `G.edges([1, 3])`.

# In[ ]:





# We can observe the node together with its attributes. 
# 
# If we want to now only see the age attribute of each node, we access it using `nx.get_node_attributes(G, 'age').values()`. get_node_attributes returns a dictionary with the node's id as the key and the age the value. With values(), we only receive the values().

# In[ ]:





# It's a dictionary. You would have to cast to a list to get only the ages. Do you know how?
# 
# Let's try an plot this graph. It's easy in networkx. Just run `nx.draw(G)`.

# In[ ]:





# There is a great number of options to improve this graphy. You can, for instance, add the labels, use curved edges  and reduce the arrow size. Try: `nx.draw(G, with_labels=True, connectionstyle="arc3,rad=0.4", arrowsize=0.4)`
# 

# In[ ]:





# In the next session, we will explore more options how to improve this graph.
