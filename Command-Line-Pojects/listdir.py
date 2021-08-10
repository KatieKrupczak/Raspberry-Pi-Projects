import os

#get the list of all files and directories in the root directory
path = "/"
dir_list = os.listdir(path)

print("Files and directories in '",path,"' :")

#print the list
print(dir_list)