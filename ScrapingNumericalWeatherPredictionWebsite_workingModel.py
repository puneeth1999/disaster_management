#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import html5lib


# In[3]:


from html5lib import html5parser


# In[4]:


from bs4 import BeautifulSoup
import requests


# In[5]:


#fileHandler = open("textFile.txt", "a")


# In[6]:


with open('bagalkot.html', "r") as f:
    page = f.read()
#tree = f.fromstring(page)


# In[7]:


page


# In[8]:


page = str(page)


# In[9]:


startIndex = page.find('\nRainfall')


# In[10]:


startIndex


# In[11]:


endIndex = page.find('\n\nNOTE')


# In[12]:


endIndex


# In[13]:


page = page[startIndex:endIndex]


# In[14]:


page


# In[15]:


page = page.rstrip('------------------- ------------------- ------------------- ------------------- ------------------- ------------------- ')


# In[ ]:





# In[ ]:





# In[16]:


page_content = page



font_data = page_content


# In[ ]:





# In[ ]:





# In[ ]:





# In[17]:


# font_data = page_content[1549:-1461]
# trimmed_font_data = font_data


# In[18]:


# try:
#     font_data=page_content.find_all('font')
#     font_data = str(font_data)
#     trimmed_font_data = font_data[1187:-208]
    
# except:
#     font_data = page_content[1549:-1461]
#     trimmed_font_data = font_data


# In[19]:


font_data


# In[ ]:





# In[20]:


type(font_data)


# In[ ]:





# In[21]:


font_data


# In[22]:


len(font_data)


# In[ ]:





# In[23]:


trimmed_font_data = font_data

trimmed_font_data


# In[24]:


# for i in trimmed_font_data:
#     #print(i)
#     try:
#         a = int(i)
#     except:
#         trimmed_font_data.strip
# print(trimmed_font_data)


# In[25]:


import pandas as pd


# In[26]:


data = trimmed_font_data
df = pd.DataFrame([x.split(' ') for x in data.split('\n')])
df


# In[27]:


df.to_csv('initial.csv')


# In[ ]:





# In[28]:


df


# In[29]:


dataframe = df


# In[30]:


dataframe[1] = dataframe[1].map(str) + ' '+dataframe[2] +' '+ dataframe[3] +' ' +dataframe[4]


# In[31]:


dataframe.drop([2,3,4], axis=1)


# In[32]:


del dataframe[4]
del dataframe[2]
del dataframe[3]
dataframe[0] = dataframe[0].map(str) + ' '+dataframe[1]
del dataframe[1]
dataframe.to_csv('initial.csv')


# In[33]:


dataframe


# In[34]:


dataframe[9] = dataframe[6] + dataframe[6] + dataframe[7] + dataframe[8]+ dataframe[9]  +dataframe[10] +dataframe[11] +dataframe[12] +dataframe[13] +dataframe[14] +dataframe[15] +dataframe[16] +dataframe[17] +dataframe[18] +dataframe[19] +dataframe[20] +dataframe[21] +dataframe[22] +dataframe[23]


# In[35]:


dataframe


# In[36]:


dataframe.to_csv('first.csv')


# In[37]:


for i in range(11, 24):
    del dataframe[i]


# In[38]:


dataframe.to_csv('second.csv')


# In[39]:


dataframe[27]


# In[40]:


dt = dataframe


# In[41]:


#dataframe[27] = dataframe[24] + dataframe[25] + dataframe[] + dataframe[8]+ dataframe[9]  +dataframe[10] +dataframe[11] +dataframe[12] +dataframe[13] +dataframe[14] +dataframe[15] +dataframe[16] +dataframe[17] +dataframe[18] +dataframe[19] +dataframe[20] +dataframe[21] +dataframe[22] +dataframe[23]

for i in range (24,41):
    if(i is 27):
        continue
    dt[27] += dt[i] 


# In[42]:


dt[27]


# In[43]:


dataframe = dt


# In[44]:


for i in range(29,41):
    del dataframe[i]


# In[ ]:





# In[ ]:





# In[45]:


dataframe.to_csv('third.csv')


# In[46]:


# dataframe.drop(16, axis = 1)
# dataframe.drop(19, axis = 1)

c1 = int(11)
c2 = int(12)
c3 = int(16)
c4 = int(19)


# In[47]:


try:
    dataframe.drop(c1, axis = 1)
except:
    print('not  possible')


# In[48]:


try:
    dataframe.drop(c2, axis = 1)
except:
    print('not  possible')


# In[49]:


try:
    dataframe.drop(c3, axis = 1)
except:
    print('not  possible')


# In[50]:


try:
    dataframe.drop(c4, axis = 1)
except:
    print('not  possible')


# In[51]:


#  del dataframe[11]


# In[52]:


#  del dataframe[12]


# In[53]:


#  del dataframe[16]


# In[54]:


#  del dataframe[19]
dataframe


# In[ ]:





# In[55]:


# dataframe.to_csv('conf2.csv')


# In[ ]:





# In[56]:


# dataframe[29] = dataframe[29] + dataframe[38] + dataframe[30] + dataframe[27] + dataframe[34]

for i in range(42,59):
    if i is 45:
        continue
    dataframe[45] += dataframe[i]


# In[57]:


dataframe[45]


# In[58]:


for i in range(46,59):
    del dataframe[i]


# In[59]:


dataframe.to_csv('fourth.csv')


# In[ ]:





# In[60]:



for i in range(61,79):
    if i is 63:
        continue
    dataframe[63] += dataframe[i]


# In[61]:


for i in range(64,78):
    del dataframe[i]


# In[62]:


dataframe.to_csv('fifth.csv')


# In[ ]:





# In[ ]:





# In[63]:


for i in range(1,9):
    for j in range(80,97):
        if(str(dataframe.at[i,j])=='None'):
            continue
        else:
            dataframe.at[i,80] = dataframe.at[i,j]
            


# In[64]:


dataframe[81]


# In[ ]:





# In[ ]:





# In[65]:


for i in range(82,97):
    try:
        del dataframe[i]
    except:
        print('oops, there\'s some kinda problem')


# In[66]:


dataframe.to_csv('me.csv')


# In[ ]:





# In[67]:


dataframe.dropna()


# In[ ]:





# In[68]:


cols_of_interest = [0,9,27,45,63,80]


# In[69]:


dataframe = dataframe[cols_of_interest]


# In[70]:


dataframe = dataframe.drop(0)


# In[71]:


dataframe = dataframe.drop(9)


# In[72]:


df = dataframe


# In[73]:


df.columns=['PARAMETERS', 'DAY-1','DAY-2','DAY-3','DAY-4','DAY-5']


# In[74]:


df


# In[75]:


df.reset_index


# In[76]:


df


# In[77]:


df['DAY-1'].astype('int64')


# In[78]:


df['DAY-2'].astype('int64')


# In[79]:


df['DAY-3'].astype('int64')


# In[80]:


df['DAY-4'].astype('int64')


# In[81]:


try:
    df['DAY-5'].astype('int64')
except:
    print('oops')


# In[82]:


df.dtypes


# In[83]:


df


# In[84]:


df.to_csv('finally.csv')


# In[85]:


df.to_excel('finalSheet.xlsx')


# In[ ]:





# In[ ]:





# In[ ]:




