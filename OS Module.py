
import os

# Finding the current working directory

print(os.getcwd())

# You can change the directory in by a function

os.chdir("/Users/tanguduavinash/Desktop/")

'''
This is a path function with basename, dirname & split
Basename: It gives the basename whatever it is
Dirname:  It prints directory name
Split:    It gives both directory name and pathname
isfile:   It prints if the given path is file or not
isdir:    It prints if the given path is directory or not
splitext: It splits the path and the .extension file

'''

os.path.basename("/Users/tanguduavinash/Desktop/os.py")
>>> os.py
os.path.dirname("/Users/tanguduavinash/Desktop/os.py")
>>> '/Desktop'
os.path.split("/Users/tanguduavinash/Desktop/os.py")
>>> ('/Desktop', 'os.py')
os.path.isdir("/Users/tanguduavinash/Desktop/os.py")
>>> False
os.path.isfile("/Users/tanguduavinash/Desktop/os.py")
>>> True
os.path.spliext("/Users/tanguduavinash/Desktop/os.py")
>>> ('/Desktop/os', '.py')

print(os.listdir()) # It will print all the files inside your current directory

# Creating a New Folder on your directory

print(os.mkdir("New Folder"))
print(os.makedirs("New Folder")) # By this you can create a sub directory
                                 # In realtime we use 'makedirs'

# Removing or deleting a directory

print(os.remove("filename")) # In realtime we remove rather than removedirs

print(os.removedirs("filename")) # This will remove/delete all the sub directories as well

# Renaming a directory

print(os.rename("Original Name", "New Name"))

# Printing all the information of the particular file:

print(os.stat("filename"))
print(os.stat("filename").st_size) # Size of that file which is a .extension
print(os.stat("filename").st_mtime) # Time when it was created or formed

# Home Directory

print(os.environ.get('HOME'))


# It will yeilds the directory path

print(os.walk())

# This method will give required fields you want by giving certain functions:

for dirnames, dirpath, filenames in os.walk(os.getcwd())
    print("Directory", dirnames)
    print("Current Path", dirpath)
    print("Files", filenames)
    print()





