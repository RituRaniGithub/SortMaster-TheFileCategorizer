#!/usr/bin/env python
# coding: utf-8

# Sort Master - The File Categorizer

# In[ ]:


import os       #os Module provides a way to interact with Operating system 
import shutil   #shutil lets you perform file operations. It will be helpful in moving the file later.

path = input("Enter the directory path to sort: ")


# In[ ]:


# Getting unique file extensions present in the directory
file_extensions = set()                                #Initiallizing an empty set to store unique file extensions
for file in os.listdir(path):             
    if os.path.isfile(os.path.join(path, file)):
        file_extension = os.path.splitext(file)[1]
        file_extensions.add(file_extension)
        
#"file" variable iterates through the items in the user specified directory, 
#and lists down all files and folders in the directory. It then identify the files and
# extract their file extensions using os.path.splitext(),
#For example, if the file variable contains the value "document.txt", os.path.splitext(file) will return a tuple
#with two elements: ("document", ".txt"). #To access the file extension specifically, 
#we use [1] to retrieve the second element of the tuple and store the unique extensions in the file_extensions set. 


# In[ ]:


# Creating folders for each unique file extension

for extension in file_extensions:
    folder_name = extension[1:] + " files" # this removes the dot from the extension and add "files" suffix. For example, if the extension is ".txt", the folder name will be "txt files".
    folder_path = os.path.join(path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

#This code creates a separate folder for each unique file extension present in the directory. 
#The folder name is constructed based on the extension. It removes the existing dot and add "files" to help identify it.
#If a folder with the same name already exists, it is not created again to avoid duplication.


# In[ ]:


# Sorting and moving the files to the corresponding folders
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        file_extension = os.path.splitext(file)[1]
        folder_name = file_extension[1:] + " files"
        destination_folder = os.path.join(path, folder_name)
        shutil.move(os.path.join(path, file), os.path.join(destination_folder, file))

print("Sorting completed.")

#the code iterates through each file in the directory, identifies the file extension,
#constructs the destination folder path based on the extension, and moves the file to the corresponding folder.

