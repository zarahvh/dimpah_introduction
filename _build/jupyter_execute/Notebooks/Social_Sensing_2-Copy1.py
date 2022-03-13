#!/usr/bin/env python
# coding: utf-8

# #  Network Analysis
# 
# ## Graph Visualisation

# In this session, we will try and create more advanced network visualisations. First, we recreate the Karate network. Run the code below.

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as plt
import networkx as nx

karate_nodes = pd.read_csv("https://tinyurl.com/2p9byesa")
karate_edges = pd.read_csv("https://tinyurl.com/mtmwc8hd")
G = nx.from_pandas_edgelist(karate_edges, source = "from", target = "to", create_using=nx.DiGraph(), edge_attr = True)
node_attr = karate_nodes.set_index('id').to_dict('index')
nx.set_node_attributes(G, node_attr)


# There is a great number of options to improve this graphy. You can, for instance, add the labels, use curved edges and reduce the arrow size. Try: `nx.draw(G, with_labels=True, connectionstyle="arc3,rad=0.4", arrowsize=0.4)`.

# In[2]:


nx.draw(G, with_labels=True, connectionstyle="arc3,rad=0.4", arrowsize=0.4)


# This graph already indicates that some members hold the whole network together by being the main link between them. You might remember that this is what the original analysis of the Karate network was about. Let’s investigate this further and visualise the degree by which members are connected to other members. A graph degree basically counts the number of connections a member has to other members. Let’s overwrite the size of each nodes with the degree. First though we need to calculate the degree for each node. That’s very easy using igraph’s degree function. Simply type graph.degree()

# In[3]:


degree_list = [50*g.degree[n] for n in g.nodes()]
degree_list[:5]


# Now, let’s reassign the size of the nodes with setting vertex_size= vertex_size=graph.degree()

# In[ ]:


nx.draw(g, pos, node_color=list(partition.values()), node_size=degree_list, with_labels= True, cmap=plt.cm.Set3)


# The new graph clearly shows  where the potential breaking points in the network are. Social network analysis is a very powerful tool with a large community already out there. Check it out and happy playing!

# That’s it for today. You have learned a lot of things about how to create social sensing networks. This is one of the most important social analytics techniques, and you can impress friends and family now with pretty graphs using the structure of social networks. Next time, we will look into content analysis using text mining.

# In[ ]:





# We could do the same, but then with the actual names, remember how we accessed the ids? Do the same with the names. We can do this with the labels argument for nx.draw. It requires a dictionary mapping node id to the first name. That's easy to get with `node_labels = nx.get_node_attributes(G, 'first_name')`. 

# In[2]:


node_labels = nx.get_node_attributes(G, 'first_name')


# Now add this to nx.draw: `nx.draw(G, with_labels=True, labels=node_labels, connectionstyle="arc3,rad=0.4", arrowsize=0.4)`.

# In[3]:


nx.draw(G, with_labels=True, labels=node_labels, connectionstyle="arc3,rad=0.4", arrowsize=0.4)


# Let’s say we want to colour our network nodes based on gender as well as size them based on age. We will also change the width of the edges based on their weight. We need to apply a series of changes to the attributes pf our igraph. To get the different colors for different genders we need to add these colors to our dataframe karate_nodes.
#  
# The Matlib colour names are listed at: https://matplotlib.org/stable/gallery/color/named_colors.html
# 
# np.where is one of the many functions of numpy that we will use a lot. It chooses either x or y (second and third argument) depending on the condition in the first argument. Type in:
# ```
# karate_nodes['colour'] = np.where(karate_nodes['gender']== 'F', 'tomato', 'skyblue')
# karate_nodes.head()
# ```

# In[4]:


karate_nodes['colour'] = np.where(karate_nodes['gender']== 'F', 'tomato', 'skyblue')
karate_nodes.head()


# Now draw the graph again with another attribute node_color=np.array(karate_nodes['colour']). Type in: `nx.draw(G, node_color=np.array(karate_nodes['colour']), with_labels=True, labels=node_labels)`.

# In[5]:


nx.draw(G, node_color=np.array(karate_nodes['colour']), with_labels=True, labels=node_labels) 


# We also wanted to change the node size based on age. We could, for example, multiply the age by 10 to get the size that we want. Add `node_size = 10*np.array(karate_nodes['age'])` as an attribute to nx.draw.

# In[6]:


nx.draw(G, node_color=np.array(karate_nodes['colour']), node_size = 10*np.array(karate_nodes['age']),
                         with_labels=True, labels=node_labels) 


# The weight of the like-relationship will determine the width of the arrow between two nodes. All we need to do is add another attribute. Type:
# ```
# nx.draw(G, node_color=np.array(karate_nodes['colour']),
#         node_size = 10*np.array(karate_nodes['age']),
#         with_labels=True, labels=node_labels,
#         width= 0.25 * np.array(karate_edges['weight']))
# ```

# In[7]:


nx.draw(G, node_color=np.array(karate_nodes['colour']),
        node_size = 10*np.array(karate_nodes['age']),
        with_labels=True, labels=node_labels,
        width= 0.25 * np.array(karate_edges['weight']))


# Actually, these graphs have never been great. Too many overlaps ...
# 
# You can  plot graphs with different layouts to avoid overlaps. To adjust the graph layout, networkx contains layout generators, which try to place the vertices and edges in a way that is more visually appealing. They position ('pos') the nodes and edges on a plane defined by x- and y-values.
# 
# There are many layout functions, let's first try a random one. Type:
# ```
# pos = nx.random_layout(G)
# 
# nx.draw(G, pos, node_color=np.array(karate_nodes['colour']),
#         node_size = 10*np.array(karate_nodes['age']),
#         with_labels=True, labels=node_labels,
#         width= 0.25 * np.array(karate_edges['weight']))
# ```

# In[8]:


pos = nx.random_layout(G)

nx.draw(G, pos, node_color=np.array(karate_nodes['colour']),
        node_size = 10*np.array(karate_nodes['age']),
        with_labels=True, labels=node_labels,
        width= 0.25 * np.array(karate_edges['weight']))


# We can now change the layout parameter and use another function. Fruchterman Reingold (https://en.wikipedia.org/wiki/Force-directed_graph_drawing) is a very popular layout algorithm. It's called spring layout in NetworkX. Change the first line of the last cell into `pos = nx.spring_layout(G)`.

# In[9]:


pos = nx.spring_layout(G)

nx.draw(G, pos, node_color=np.array(karate_nodes['colour']),
        node_size = 10*np.array(karate_nodes['age']),
        with_labels=True, labels=node_labels,
        width= 0.25 * np.array(karate_edges['weight']))


# This is a bit better. Less overlap. Let's try another layout. Replace the pos line with `pos = nx.kamada_kawai_layout(G)`.
# 
# Also, the edges are too dark. A good trick is often to set their colours to greyscale. Also add:
# ```
# nx.draw(G, pos, node_color=np.array(karate_nodes['colour']),
#         node_size = 10*np.array(karate_nodes['age']),
#         with_labels=True, labels=node_labels,
#         edge_color="silver",
#         width = 0.25 * np.array(karate_edges['weight']))
# ```

# In[10]:


pos = nx.kamada_kawai_layout(G)

nx.draw(G, pos, node_color=np.array(karate_nodes['colour']),
        node_size = 10*np.array(karate_nodes['age']),
        with_labels=True, labels=node_labels,
        edge_color="silver",
        width = 0.25 * np.array(karate_edges['weight']))


# Ok. At least everything is readable ... But it is still difficult to see any interesting patterns in the network. Remember, e.g., the original insight from the 1970s paper of the karate club? It described how the larger community of the whole club was effectively the result of several separate communities of members and split thererfore according to trust placed in either the administrator or instructor. Thus the whole karate club community can split up easily. Graph analysis comes with a lot of so-called community detection algorithms that support such investigations. We will use what many consider one of the best algorithms in this domain. Louvain is explained at https://towardsdatascience.com/louvain-algorithm-93fde589f58c. 
# 
# Let's first load the library with `from community import community_louvain`. Run the cell below.

# In[11]:


#Keep cell

#install with pip install python-louvain
from community import community_louvain


# Louvain requires undirected graphs. We create an undirected copy with `g = G.to_undirected()`.

# In[12]:


g = G.to_undirected()


# Now let's create the optimal partition of the graph according to Louvain. Run `partition = community_louvain.best_partition(g)`. Print out the items of the dictionary with `partition.items()`.

# In[13]:


partition = community_louvain.best_partition(g)
partition.items()


# Louvain create four partitions (0 - 3). Let's plot these partitions by colour-coding the nodes. Run:
# ```
# pos = nx.spring_layout(g)
# nx.draw(g, pos, node_color=list(partition.values()), with_labels=True, cmap=plt.cm.Set3)
# ```
# cmap=plt.cm.Set3 is new and chooses a colormap for Python to assign a colour to each partition. Colormaps are very powerful: 
# https://www.analyticsvidhya.com/blog/2020/09/colormaps-matplotlib/

# In[14]:


pos = nx.spring_layout(g)
nx.draw(g, pos, node_color=list(partition.values()), with_labels=True, cmap=plt.cm.Set3)


# Nice but we can do even better with the help of stackoverflow (https://stackoverflow.com/questions/43541376/how-to-draw-communities-with-networkx). We have added a function `pos = community_layout(g, partition)` that let's you plot partitions by separating them out clearly. Run the cell below.
