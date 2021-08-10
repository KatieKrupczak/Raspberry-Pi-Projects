import os

# Directory
directory = "GeeksforGeeks"

# Parent Directory Path
parent_dir = "/home/pi/Desktop"

# Path
path = os.path.join(parent_dir, directory)

# Create the directory GeeksForGeeks in ~/home/pi/Desktop
os.mkdir(path)
print("Directory '% s' created" % directory)

# Directory 
directory = "Geeks"

# Parent Directory Path
parent_dir = "/home/pi/Desktop"

# mode
mode = 0o666

# Path
path = os.path.join(parent_dir, directory)

# Create the directory Geeks in /home/pi/Desktop with mode 0o666
os.mkdir(path, mode)
print("Directory '% s' created" % directory)