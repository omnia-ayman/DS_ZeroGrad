#!/usr/bin/env python
# coding: utf-8

# ### Training titanic data for analysis
# The training set should be used to build your machine learning models. For the training set, we provide the outcome (also known as the “ground truth”) for each passenger. Your model will be based on “features” like passengers’ gender and class. You can also use feature engineering to create new features.
# 
# ### variable  Definition
# survival 	Survival 	0 = No, 1 = Yes
# 
# pclass 	Ticket class 	1 = 1st, 2 = 2nd, 3 = 3rd
# 
# sex 	Sex 
# 
# Age 	Age in years 
# 
# sibsp 	# of siblings / spouses aboard the Titanic
# 
# parch 	# of parents / children aboard the Titanic 
# 
# ticket 	Ticket number
# 
# fare 	Passenger fare
# 
# cabin 	Cabin number 
# 
# embarked 	Port of Embarkation 	
# C = Cherbourg, Q = Queenstown, S = Southampton
# 
# 
# 
# ### Variable Notes
# 
# pclass: A proxy for socio-economic status (SES)
# 1st = Upper
# 2nd = Middle
# 3rd = Lower
# 
# age: Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5
# 
# sibsp: The dataset defines family relations in this way...
# Sibling = brother, sister, stepbrother, stepsister
# Spouse = husband, wife (mistresses and fiancés were ignored)
# 
# parch: The dataset defines family relations in this way...
# Parent = mother, father
# Child = daughter, son, stepdaughter, stepson
# Some children travelled only with a nanny, therefore parch=0 for them.

# ## Importing needed datasets

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import KNNImputer
sns.set()


# ## Reading the file as dataframe

# In[2]:


data = pd.read_csv("train.csv")
data.head(3)


# ## Data Description

# In[3]:


data.info()


# In[4]:


data.describe()


# In[5]:


round(data.isnull().mean() * 100 , 1)


# In[6]:


data.duplicated().sum()


# In[7]:


data.nunique()


# ## Data Cleaning

# While data description phase, we can determine some info about the dataset such as :
# 
#     1-  we do not have benefit from some columns: passengerid , passenger name and ticket.
#     
#     2-  Data does not have any duplicates.
#     
#     3- Data types and input are unique with correct types.
#     
#     4- The column Cabin is 77.1% null so we can drop it.
#     
#     5- The column Embarked is 0.2% null so we can manage it to fillout empty cells.
#     
#     6- The column Age with about 20% null values can be filled out using knn and machine learning tip to predict the value responding to the 3 neighbors features.

# In[8]:


## Dealing with unwanted columns
data.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
data.isnull().sum()


# In[9]:


## Dealing with Embarked column
round(data["Embarked"].value_counts(normalize = True) * 100, 2)
data["Embarked"].isnull().sum()
data["Embarked"].fillna(data['Embarked'].max , inplace = True) 


# In[10]:


## Dealing with age using knn imputers 
imp = KNNImputer(n_neighbors = 3)
data[['Age']] = imp.fit_transform(data[['Age']])
data.isnull().sum()


# In[11]:


data.info()


# ## Data Analysis
# After our data was cleaned : Dropping unwanted dat and filling others to ensure that it is clean with zero isnull values, we can use analysis to get the main KPIs and ingo needed to be visualized

# In[12]:


def MainInfoCatCount (data , col):
    print("The column : " ,col)
    print(round(data[col].value_counts(normalize = True)*100 , 2))
    sns.countplot(x=col, data=data);


# In[13]:


## column survied
MainInfoCatCount (data , "Survived")


# In[14]:


## column sex
MainInfoCatCount (data , "Sex")


# In[15]:


## column pclass
MainInfoCatCount (data , "Pclass")


# In[16]:


## column Age
print(round(data["Age"].describe(), 2))
sns.histplot(x="Age", data=data);


# In[74]:


#make 2*4 plots
fig, ax = plt.subplots(1, 4, figsize=(20,6))
for i, col in enumerate(['Pclass','Sex', 'SibSp','Parch']):
    #i is making the index of the array 00 01 10 12 22 and so on...
    sns.barplot(x=col, y= 'Survived', data=data, ci=None, ax = ax[i%4])
    #ax[i//4, i%4].axhline(data.Survived.mean(), color='black', linestyle='--')
plt.show()


# In[75]:


sex = pd.merge(data[data["Sex"] == "female"].groupby("Pclass").Survived.mean(), data[data["Sex"] == "male"].groupby("Pclass").Survived.mean(), on = "Pclass")


# In[79]:


sex.rename(columns= {'Survived_x': 'female_survived', 'Survived_y': 'male_survived'}, inplace=True)
sex.reset_index(inplace = True)


# In[80]:


sns.barplot(x='female_survived', y='male_survived', hue= 'Pclass', data=sex, ci=None);


# In[71]:


data.groupby(['Pclass', 'Sex']).Survived.mean()


# In[ ]:




