#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
#dataset: https://vincentarelbundock.github.io/Rdatasets/datasets.html (flchain.csv)
data = pd.read_csv('flchain.csv', delimiter=',')
len(data)


# age = age in years, 
# sex = F=female, M=male, 
# sample.yr = the calendar year in which a blood sample was obtained,
# kappa = serum free light chain, kappa portion,
# lambda = serum free light chain, lambda portion,
# flc.grp = the FLC group for the subject, as used in the original analysis,
# creatinine = serum creatinine,
# mgus = 1 if the subject had been diagnosed with monoclonal gammapothy (MGUS),
# futime = days from enrollment until death. Note that there are 3 subjects whose sample was obtained on their death date,
# death = 0=alive at last contact date, 1=dead,
# chapter = for those who died, a grouping of their primary cause of death by chapter headings of the International Code of Diseases ICD-9.

# In[15]:


data.head()


# In[16]:


data.describe()
data.chapter.describe()


# In[17]:


column_target = ['death']
columns_train = ['age', 'sex', 'kappa', 'lambda', 'flc.grp', 'creatinine', 'mgus', 'futime'] #, 'chapter']


# In[18]:


X = data[columns_train]
Y = data[column_target]


# In[19]:


#NaN value present in data
X['creatinine'].isnull().sum()
#X['chapter'].isnull().sum()


# In[20]:


#fill NaN value with Mean or Mediam value
X['creatinine'] = X['creatinine'].fillna(X['creatinine'].median())


# In[21]:


#Let F = 1, M = 0
d = {'F':0, 'M':1}
X['sex'] = X['sex'].apply(lambda x:d[x])


# In[22]:


X.head()


# In[23]:


from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = .33, random_state = 10)


# In[31]:


# from sklearn import svm
# clf = svm.LinearSVC()

# clf.fit(X_train, Y_train)
# print(clf)
# print(clf.predict(X_test[0:10]))
# print(clf.score(X_test, Y_test))


# In[32]:


from lifelines import KaplanMeierFitter


# In[33]:


kmf = KaplanMeierFitter()


# In[34]:


T = data['futime']
C = data['death']


# In[35]:


kmf.fit(T, C)


# The removed column contains the number of observations removed during that time period, whether due to death (the value in the observed column) or censorship. So the removed column is just the sum of the observed and censorship columns. The entrance column tells us whether any new subjects entered the population at that time period. Since all the players we are studying start at time=0 (the moment they were drafted), the entrance value is 15,592 at that time and 0 for all other times.
# 
# The at_risk column contains the number of subjects that are still alive during a given time. The value for at_risk at time=0, is just equal to the entrance value. For the remaining time periods, the at_risk value is equal to the difference between the time previous period's at_risk value and removed value, plus the current period's entrance value.

# In[39]:


kmf.event_table


# In[36]:


get_ipython().run_line_magic('pylab', 'inline')
figsize(12, 6)
kmf.plot()


# In[ ]:





# In[38]:


# from lifelines import CoxPHFitter

# cph = CoxPHFitter()
# cph.fit(data, duration_col='futime', event_col='death', show_progress=False)


# In[ ]:




