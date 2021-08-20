#!/usr/bin/env python
# coding: utf-8

# In[1]:


from glob import glob
import os
from sklearn.model_selection import train_test_split
import PIL.Image as PIL


# In[6]:


input_test_size = 0.2


# In[3]:


imglist = glob('export/images/*.jpg')
if not imglist:
    print('load Failed')
train,test = train_test_split(imglist,test_size=input_test_size,random_state=2000)


# In[4]:


if not os.path.exists(os.getcwd()+'//'+'train/images'):
    os.makedirs(os.getcwd()+'//'+'train/images')
if not os.path.exists(os.getcwd()+'//'+'test/images'):
    os.makedirs(os.getcwd()+'//'+'test/images')
    
if not os.path.exists(os.getcwd()+'//'+'train/labels'):
    os.makedirs(os.getcwd()+'//'+'train/labels')
if not os.path.exists(os.getcwd()+'//'+'test/labels'):
    os.makedirs(os.getcwd()+'//'+'test/labels')
train_list = [ PIL.open(train[i]).convert('RGB').resize((416,416)) for i in range(len(train))]
test_list = [ PIL.open(test[i]).convert('RGB').resize((416,416)) for i in range(len(test))]
[train_list[i].save('./train/images/'+train[i].split('\\')[-1],'JPEG') for i in range(len(train_list))]
[test_list[i].save('./test/images/'+test[i].split('\\')[-1],'JPEG') for i in range(len(test_list))]

