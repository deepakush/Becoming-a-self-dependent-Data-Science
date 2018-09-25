

#Project
# 
# Before working on this assignment please read these instructions fully.Please familiarize your datasets with the criteria before beginning the assignment.
# 
# Q. This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **measures** (see below) for the region of **Delhi, National Capital Territory of Delhi, India**, or **India** more broadly.
# 
# Ans. I merged these datasets with data from different regions i Choose India and USA, two similar datasets! For instance, I want to compare ** India** to USA.

# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.

# Here are the assignment steps:
# 
#  * State the region and the domain category that your data sets are about (e.g., **India** and USA, on **measures**).
#  * State a question about the domain category and region that you identified as being interesting.
#  * Must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * Must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * Must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **measures**?  For this category you might look at the inputs or outputs to the given major changes in the measure compared to other regions.
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. 
# 
# 
# Link:
# India https://data.worldbank.org/indicator/SP.DYN.AMRT.MA?contextual=default&end=2016&locations=IN&name_desc=false&start=1960&view=chart
# 
#  USA https://data.worldbank.org/indicator/SP.DYN.AMRT.MA?contextual=default&end=2016&locations=US&name_desc=false&start=1960&view=chart
# 
# http://databank.worldbank.org/data/reports.aspx?source=2&type=metadata&series=SP.DYN.AMRT.MA

# In[23]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[46]:


df_ind = pd.read_excel('C:\\Users\\shikh\\OneDrive\\Desktop\\Indian_Rate.xlsx', skiprows=2)
df_ind.set_index(['Year'], inplace= True)
df_ind.rename(columns=({'Mortality rate(per 1,000 male adults)':'IND Mortality rate(per 1,000 male adults)'}), inplace =True)

df_ind.head()


# In[41]:


df_ind.plot(color='indigo')


# In[47]:


df_usa = pd.read_excel('C:\\Users\\shikh\\OneDrive\\Desktop\\United_States_Rate.xlsx', skiprows=2)
df_usa.set_index(['Year'], inplace= True)
df_usa.rename(columns=({'Mortality rate(per 1,000 male adults)':'USA Mortality rate(per 1,000 male adults)'}), inplace =True)

df_usa.head()


# In[48]:


df_usa.plot(color='firebrick')


# In[49]:


df_ind = pd.read_excel('C:\\Users\\shikh\\OneDrive\\Desktop\\Indian_Rate.xlsx', skiprows=2)
df_ind.set_index(['Year'], inplace= True)
df_ind.rename(columns=({'Mortality rate(per 1,000 male adults)':'IND Mortality rate(per 1,000 male adults)'}), inplace =True)
df_ind

df_usa = pd.read_excel('C:\\Users\\shikh\\OneDrive\\Desktop\\United_States_Rate.xlsx', skiprows=2)
df_usa.set_index(['Year'], inplace= True)
df_usa.rename(columns=({'Mortality rate(per 1,000 male adults)':'USA Mortality rate(per 1,000 male adults)'}), inplace =True)
df_usa

result = pd.concat([df_ind, df_usa], axis=1)
result.head()


# In[50]:


df_ind = pd.read_excel('C:\\Users\\shikh\\OneDrive\\Desktop\\Indian_Rate.xlsx', skiprows=2)
df_ind.set_index(['Year'], inplace= True)
df_ind.rename(columns=({'Mortality rate (per 1,000 male adults)':'IND Mortality rate (per 1,000 male adults)'}), inplace =True)
df_ind

df_usa = pd.read_excel('C:\\Users\\shikh\\OneDrive\\Desktop\\United_States_Rate.xlsx', skiprows=2)
df_usa.set_index(['Year'], inplace= True)
df_usa.rename(columns=({'Mortality rate (per 1,000 male adults)':'USA Mortality rate (per 1,000 male adults)'}), inplace =True)
df_usa

merged =pd.merge(df_usa, df_ind, left_index= True, right_index= True)

merged


# ### legend
# df.legend(loc='any direction')
# 
# any direction like = upper right,
# 	upper left, 
# 	lower left, 
# 	lower right,
# 	right,
# 	center left,
# 	center right,
# 	lower center,
# 	upper center,
# 	center,

# In[51]:


fig = plt.figure(figsize=(11,6))
ax =plt.subplot(111)

ax.plot(df_ind,'-', label='IND Mortality rate (per 1,000 male adults)', color='indigo', alpha=1)
ax.plot(df_usa,'-', label='USA Mortality rate (per 1,000 male adults)', color='firebrick', alpha=1 )
ax.legend(loc='upper center',bbox_to_anchor=(0.75, 1),fancybox=True, shadow= True, handlelength=1.9, borderpad=1.2, labelspacing=1)
ax.set_title('Male adult mortality rate in India & USA, 1990-2016')
ax.set_ylabel('per 1,000 male adults')
plt.show()

