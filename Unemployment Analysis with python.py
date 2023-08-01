#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install plotly


# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[3]:


df = pd.read_csv('Unemployment_Rate_upto_11_2020.csv')
df.head()


# In[4]:


df.info


# In[5]:


df.describe()


# In[6]:


df.isnull().sum()


# In[7]:


df.columns = ['States','Dates','Frequency','Estimated Unemployment rate','Estimated employed',
              'Estimated labor participation rate','Region','longitude','latitude']


# In[8]:


df


# In[9]:


#Look at the correlation between the feature of this dataset
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv('Unemployment_Rate_upto_11_2020.csv')
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(12,10))
sns.heatmap(df.corr())
plt.show


# In[10]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv('Unemployment_Rate_upto_11_2020.csv')
df.columns = ['States','Dates','Frequency','Estimated Unemployment rate','Estimated employed',
              'Estimated labor participation rate','Region','longitude','latitude']
plt.title("Indian Unemployement")
sns.histplot(x = 'Estimated employed',hue = 'Region',data = df)
plt.show()


# In[11]:


#See the unemployment rate according to different regions of India
plt.figure(figsize = (12,10))
plt.title('Indian Unemployment')
sns.histplot(x = 'Estimated Unemployment rate',hue = 'Region',data = df)
plt.show()


# In[12]:


#Creating a dashboard to analyze unemployment rate of each Indian state by region 
#Sunburst plot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

unemployment  = df[['States','Region','Estimated Unemployment rate']]
figure = px.sunburst(unemployment,path = ['Region','States'],
                     values = 'Estimated Unemployment rate',
                     width = 700, height = 700,color_continuous_scale = 'RdY1Gn',
                     title = 'Unemployment Rate in India')
figure.show()
                     

