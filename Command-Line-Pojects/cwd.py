#import os module
import os

#get current working directory
cwd = os.getcwd()

#print the current working directory CWD
print("Current working directory: ", cwd)

#change the current working directory
os.chdir('LED-Collection-Projects')
cwd = os.getcwd()
print("Current working directory: ", cwd)