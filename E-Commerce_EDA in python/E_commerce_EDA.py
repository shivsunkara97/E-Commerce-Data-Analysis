#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns


# In[3]:


#Defining the Business Problem
#1.What are the best selling products and categories?
#2.What is the average order value?
#3.What is the customer retention rate?
#4.What is the customer acquisition cost?
#5.Which marketing channels drive the most traffic and sales?


# In[4]:


df1=pd.read_csv('Customer.csv')
df1.head()
df2=pd.read_csv('Transactions.csv')
df2.head()
df3=pd.read_csv('prod_cat_info.csv')
df3.head()


# In[5]:


df1.head()


# In[6]:


df2.head()


# In[7]:


df2=df2.rename(columns={'cust_id':'customer_Id'})


# In[8]:


#Merging Entire dataset


# In[9]:


df4=pd.merge(df2,df1,how='left',on='customer_Id')


# In[10]:


df4.head()


# In[11]:


E_commerce_data=pd.merge(df4,df3,how='left',on='prod_cat_code')
E_commerce_data.head()


# In[12]:


#checking info about dataset


# In[29]:



print(E_commerce_data.shape)
print(E_commerce_data.info())
print(E_commerce_data.describe())


# In[14]:


# Check for missing values
print(E_commerce_data.isnull().sum())


# In[24]:


E_commerce_data[E_commerce_data['Gender'].isnull()].head()


# In[30]:


#Replacing null values with NA


# In[32]:


E_commerce_data=E_commerce_data.fillna('Na',inplace=True)


# In[58]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[36]:


# Explore the distribution of each numerical variable


# In[63]:


sns.histplot(E_commerce_data['Total_amt_with_tax'], kde=True)
plt.title('Distribution of Total Amount with Tax')
plt.show()


# In[66]:


sns.countplot(x='Gender', data=E_commerce_data)
plt.title('Gender Distribution')
plt.show()


# In[67]:


sns.countplot(x='city_name', data=E_commerce_data)
plt.title('City Distribution')
plt.xticks(rotation=90)
plt.show()


# In[68]:


sns.countplot(x='prod_cat', data=E_commerce_data)
plt.title('Product Distribution')
plt.xticks(rotation=90)
plt.show()


# In[19]:


Sales_Returned= E_commerce_data.loc[E_commerce_data['Total_amt_with_tax']<0,'Total_amt_with_tax'].sum()
Sales_Returned


# In[21]:


Products_Returned= E_commerce_data.loc[E_commerce_data['Total_amt_with_tax']<0,'Qty'].sum()
Products_Returned


# In[23]:


Average_order_value=E_commerce_data['Total_amt_with_tax'].mean()
Average_order_value


# In[71]:


sns.boxplot(x='city_name', y='Total_amt_with_tax', data=E_commerce_data)
plt.title('Total Amount after Tax by City')
plt.xticks(rotation=90)
plt.show()


# In[ ]:




