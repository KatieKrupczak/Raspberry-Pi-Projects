import os

#function to get the current working directory
def current_path():
    print("Current working directory: "+ os.getcwd())
    print()

#Driver's code

#print cwd before
current_path()

#change the cwd
os.chdir('../')

#print cwd after
current_path()