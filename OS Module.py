
import os
'''
This exports:
  - all functions from posix or nt, e.g. unlink, stat, etc.
  - os.path is either posixpath or ntpath
  - os.name is either 'posix' or 'nt'
  - os.curdir is a string representing the current directory (always '.')
  - os.pardir is a string representing the parent directory (always '..')
  - os.sep is the (or a most common) pathname separator ('/' or '\\')
  - os.extsep is the extension separator (always '.')
  - os.altsep is the alternate pathname separator (None or '/')
  - os.pathsep is the component separator used in $PATH etc
  - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
  - os.defpath is the default search path for executables
  - os.devnull is the file path of the null device ('/dev/null', etc.)
'''

# This will give the entire path of your file /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/os.py

print(os.__file__) 

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





