import os

#Directory name
directory = "Geeks"

#Parent Directory
parent_dir = "/home/pi/Desktop"

#path
path = os.path.join(parent_dir, directory)

#Remove the directory 'Geeks'
os.rmdir(path)

directory = "GeeksforGeeks"

path = os.path.join(parent_dir, directory)

os.rmdir(path)