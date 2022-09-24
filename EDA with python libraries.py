#!/usr/bin/env python
# coding: utf-8

# # EDA with python libraries

# # 1. Pandas Profiling

# In[2]:


pip install pandas-profiling


# In[3]:


import pandas as pd
from pandas_profiling import ProfileReport


# In[4]:


df = pd.read_csv("C:\\Users\\Praful Bhojane\\OneDrive\\Documents\\Travel.csv")


# In[5]:


df


# In[6]:


profile_report = ProfileReport(df, title="Pandas Profiling Report")


# In[24]:


profile_report


# In[ ]:





# # 2.Autoviz

# In[15]:


pip install autoviz


# In[16]:


import autoviz


# In[18]:


from autoviz.AutoViz_Class import AutoViz_Class


# In[19]:


auto_viz = AutoViz_Class()


# In[22]:


filename = "C:\\Users\\Praful Bhojane\\OneDrive\\Documents\\train.csv"
sep = ","
dft = auto_viz.AutoViz(
    filename,
    sep=",",
    depVar="",
    dfte=None,
    header=0,
    verbose=0,
    lowess=False,
    chart_format="svg",
    max_rows_analyzed=150000,
    max_cols_analyzed=50,
    save_plot_dir=None
)


# In[ ]:





# # 3.d-tale

# In[38]:


pip install dtale


# In[41]:


import dtale
import pandas as pd


# In[42]:


df1  = pd.read_csv("C:\\Users\\Praful Bhojane\\OneDrive\\Documents\\AgentPerformance.csv")


# In[45]:


dtale.show(df1)


# In[35]:





# In[ ]:




