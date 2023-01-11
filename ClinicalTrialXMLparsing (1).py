#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Very unoptimized initial exploration
import xml.sax


# In[2]:


xml.sax.make_parser()


# In[3]:


xml.sax.parse(xmlfile,contenthandler[,errorhandler])


# In[8]:


# import OS module
import os

# Get the list of all files and directories
path = "C://Users//neelk//Desktop//CTD"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

# prints all files
print(dir_list)


# In[19]:


dir_list2 = os.listdir(path + "//" + dir_list[1])
firstXMLpath = path + "//" + dir_list[1] + "//" + dir_list2[1]
print(firstXMLpath)


# In[23]:


import json
import xmltodict


# In[22]:


pip install xmltodict


# In[36]:


json.loads(json_data)['clinical_study']['study_type']


# In[65]:


import json
import xmltodict
import numpy as np
import pandas as pd
study_type_full = []
path = "C://Users//neelk//Desktop//CTD"
dir_list = os.listdir(path)
for i in (range(len(dir_list))):
    print(str(i+1) + " out of " + str(len(dir_list)), end = "\r")
    dir_list2 = os.listdir(path + "//" + dir_list[i])
    for j in range(len(dir_list2)):
        pXMLpath = path + "//" + dir_list[i] + "//" + dir_list2[j]
        with open(pXMLpath, encoding='utf-8') as xml_file:
            data_dict = xmltodict.parse(xml_file.read())
            json_data = json.dumps(data_dict)
            study_type_full = np.append(study_type_full, json.loads(json_data)['clinical_study']['study_type'])


# In[62]:


pd.value_counts(np.array(study_type_full))


# In[43]:


i


# In[44]:


j


# In[45]:


json_data


# In[50]:


b'\x81'.decode('Latin1') 
b'\x81'.decode('Latin2') 
b'\x81'.decode('iso8859') 
b'\x81'.decode('iso8859-2') 


# In[60]:


with open(pXMLpath, encoding='utf-8') as xml_file:
            data_dict = xmltodict.parse(xml_file.read())


# In[66]:


json_data


# In[68]:


json.loads(json_data)['clinical_study']


# In[ ]:




