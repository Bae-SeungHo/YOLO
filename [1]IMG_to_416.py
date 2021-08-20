#!/usr/bin/env python
# coding: utf-8

# In[5]:


from glob import glob
import PIL.Image as PIL
import os


# In[1]:


labels = input().split()


# In[24]:


for label in labels: 
	img = glob('.//'+label+'/*.jpg')
	img = [ PIL.open(img[i]).convert('RGB').resize((416,416)) for i in range(len(img))]
	if not os.path.exists(os.getcwd()+'//'+'export/images'):
   		os.makedirs(os.getcwd()+'//'+'export/images')
	[img[i].save('./export/images/'+label+'_'+str(i)+'.jpg','JPEG') for i in range(len(img))]


# In[ ]:




