#!/usr/bin/env python
# coding: utf-8

# # Data Analysis with Python
# 
# ## Unit 1 Basics

# ### Background
# 
# In two units that build upon each other, we offer you a chance to develop your own data analysis and machine learning skills in a field called data analysis or also sometimes data analytics (https://en.wikipedia.org/wiki/Analytics).
# 
# Analytics has a strong tradition, very established methods, and a broad range of applications in culture, economy, and society. Particular relevant for us are the two traditions of social media and cultural analytics/analysis. Social media analytics (https://en.wikipedia.org/wiki/Social_media_analytics) extends general analytics toward the analysis of social (media) relationships. Cultural analytics (https://en.wikipedia.org/wiki/Cultural_analytics) builds on  existing successful analytical methods and applies its techniques and methods to the study of cultural objects. 
# 
# In the course, you will gain knowledge about the theoretical and practical foundations of an analysis of socio-cultural objects. While experimenting, you will also learn about the limits of the current capacities as well as the exciting opportunities. 
# 
# Before you reach these opportunities, we will take you through the relevant foundations of Python in the first unit. This might seem abstract at times, but we promise you that we take you to the interesting parts as quickly as possible. The second unit presents digital methods from association mining to network analysis.

# ### Learning objectives
# 
# After completing this course, the learner will:
# 
# - Understand the key principles behind data analysis with Python for the humanities
# - Gain knowledge about key concepts behind data analysis with Python
# - Critically evaluate methods for data analysis and apply them to a wide range of fields in the humanities
# - Develop skills around critical dataset assessment
# - Develop research questions and strategies that can be addresses with data analysis
# - Write up reports on the outcomes of a data analysis

# ### Before you get started
# 
# You will be working with Jupyter notebooks, brought together as a GitBook (https://jupyter.org). Jupyter is a web-based computing environment, often used with the Python programming language  but other languages are also available. Jupyter notebooks contain both computer code and rich text elements including visualisations, maps or interactive elements. Content is shared within cells, which are the building blocks of notebooks for both code and text. Tbis introduction is the only notebook that does not contain code. Structured into cells, notebooks are human-readable as well as executable documents for data analysis. You can read a research story and interact with its execution and the methodologies at the same time. Sometimes, the coding cells will be already prepared for you. At other times, you will need to find your own solution.
# 
# If you feel uncertain about the environment, there are many video tutorial online like https://www.youtube.com/watch?v=H9Iu49E6Mxs.
# 
# The vidoes also explain how to install the environment on your own machine. You don't need to do this as you can run the notebooks directly in either Binder (https://mybinder.org/) or Google Colab (https://colab.research.google.com/). There should be links on top of your notebooks that look like:
# 
# ![title](https://i.stack.imgur.com/Vj5WW.png)
# 
# 
# Please, note you might need an account for these environments. Once you are set up, everything should run smoothly.
# 
# But if you want to run the environment on your own machine, you can go to https://www.anaconda.com/ and follow the instructions to install Python and notebooks from https://www.anaconda.com/products/distribution. We would not recommend this for beginners though, as it requires some understanding of command lines, environments, etc. Check out https://docs.jupyter.org/en/latest/running.html. This how you download a file from GitHub: https://www.wikihow.com/Download-a-File-from-GitHub. At the beginning, it is better to focus on the Python programming. It's hard enough.
# 
# Let's get started ...

# ## Unit 1: Interactive Data Exploration with Python
# 
# The first unit of the course provides the basics of interactive Python as well as a first real-life case study at the end. We focus on showing you how to use Python for data exploration and the basics of visualisation. You will master the basics of data analysis in Python including NumPy, SciKit-learn and Matplotlib. Once you finish this short course you can move on to module two (insert link once published).
# 
# We recomend to work from the dariahTeach environment and progress through the units from there. It contains additional exercises and links. But you can also work directly with the notebooks. If you prefer this, the easiest way is to keep this introduction notebook open and click from here through to the various units.
# 
# Take a quick look at the structure of the unit of what the sessions include.

# ### Starting with Python
# 
# #### The first notebook
# 
# This is an introduction to the programming language Python. You learn several basic skills such as addition and multiplication and get a general feeling of the environments.
# 
# Start the session from [here](https://zarahvh.github.io/dimpah_introduction/Notebooks/Basics/Interactive_Data_Exploration_with_Python/StartingPython.html).
# 
# #### Lists
# 
# Data analysis whether in the humanities or elsewhere is all about manipulating representations of data. This is why we introduce the most common way of collecting data in Python quickly. With so-called lists, you can collect several elements in the same variable. 
# 
# Start the session from [here](https://zarahvh.github.io/dimpah_introduction/Notebooks/Basics/Interactive_Data_Exploration_with_Python/PythonLists.html).
# 
# #### Arrays
# 
# Arrays are very similar to lists, but often preferred in data analysis, as they provide powerful additional tools. The session also introduces how to work with libraries in Python. Arrays are part of the famous NumPy library.
# 
# Start the session from [here](https://zarahvh.github.io/dimpah_introduction/Notebooks/Basics/Interactive_Data_Exploration_with_Python/Arrays.html).

# ### Dataframes
# 
# #### Introduction
# 
# The most important structure in Python to store and process data are ‘dataframes’. The library to do so in Python is Pandas that is a key part of our work. It is a flexible and easy to use open source data analysis and manipulation tool. With dataframes we can represent almost any kind of data. 
# 
# Start the session from [here](https://zarahvh.github.io/dimpah_introduction/Notebooks/Basics/Interactive_Data_Exploration_with_Python/DataFrames.html).
# 
# #### Dataframe Indexing
# 
# Dataframes are also very powerful because you can slice and transform the data in many different ways. For this, you need to learn about dataframe indexing.
# 
# Start the session from [here](https://zarahvh.github.io/dimpah_introduction/Notebooks/Basics/Advanced_Interactive_Data_Exploration_with_Python/DataFrameIndexing.html).

# ### Control Structures
# 
# Control structures are the last basic Python concepts before we move on to an actual data analysis and visualisation. They execute a piece of code based on a condition. You can recognize them in most programming languages by the keyword if. 
# 
# Start the session from [here](https://zarahvh.github.io/dimpah_introduction/Notebooks/Basics/Advanced_Interactive_Data_Exploration_with_Python/ControlStructures.html).

# ### Real-Life Data Analysis
# 
# #### Analysing racial bias in the US justice system
# 
# This session works through a detailed example of data exploration and analyse a very small part of the complex question of racism in the USA. We also learn how to conduct a simple statistical analysis.
# 
# Start the session from [here](https://zarahvh.github.io/dimpah_introduction/Notebooks/Basics/Advanced_Interactive_Data_Exploration_with_Python/Real-Life-Data.html).
# 
# #### Basic Visualisation of results
# 
# This sessions introduces how to visual results from your data analysis.
# 
# Start the session from [here](https://zarahvh.github.io/dimpah_introduction/Notebooks/Basics/Advanced_Interactive_Data_Exploration_with_Python/BasicVisualisation.html).
