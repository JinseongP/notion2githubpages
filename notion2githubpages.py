#!/usr/bin/env python
# coding: utf-8

# In[1]:


import zipfile
import glob
import time
import shutil
import os
import re


# In[2]:


target="Export-*.zip"

date=time.localtime()

path_list = glob.glob(target)

posts_folder_path='_posts/'
images_folder_path='assets/images/'

if not os.path.exists(posts_folder_path):
    os.makedirs(posts_folder_path)
if not os.path.exists(images_folder_path):
    os.makedirs(images_folder_path)


# In[4]:


for path in path_list:    
    
    zip_path = zipfile.ZipFile(path)
    
    images = None
    if len(zip_path.namelist())>1:
        images = zip_path.namelist()[1:]
    post = zip_path.namelist()[0]

    exported_filename = post.split('.')[0]
 
    ########################### input
    
    print("Title for "+exported_filename+": ")
    title = input ()
    print("Excerpt for "+exported_filename+": ")
    excerpt = input()#'exp'
    print("Category for "+exported_filename+": ")
    categories = input()
    print("Tags (separated by '/') for "+exported_filename+": ")
    tags = input()
    tags = tags.split('/')
    
    filename = str(date.tm_year)+"-"+str(date.tm_mon)+"-"+str(date.tm_mday)+"-"+re.sub('[\/:*?"<>|]','',title)
    ###########################


    zip_path.extractall()

    with open(post, 'r+', encoding='UTF8') as file:
        readcontent = file.read()  
        file.seek(0, 0)
        file.truncate(0) 
        file.write("---"+"\n")
        file.write("title: "+title+"\n")
        file.write("excerpt: "+excerpt+"\n")
        file.write("categories:"+"\n"+"  - "+categories+"\n")
        file.write("tags:"+"\n")
        for tag in tags:
            file.write("  - "+tag+"\n")
        file.write("---"+"\n")
              
        if images is not None:
            for line in readcontent.splitlines():
                if 'png' in line:
                    imagename = (line.split('.')[0].split('/')[1])
                    line = '!['+imagename+'.png]({{site.url}}/'+images_folder_path+filename+'/'+imagename+'.png){:.center-image}'
                file.write(line+'\n')        
        else:
            file.write(readcontent) 

        file.close()

    shutil.move(post, posts_folder_path+filename+".md")
    if images is not None:
        shutil.move(exported_filename, images_folder_path+filename)
    zip_path.close()
    os.remove(path)


# In[ ]:




