import os

# Specify the directory path
path = "new folder"

# Get the list of files and folders
contents = os.listdir(path)

print("Contents of the directory:")
for item in contents:
    print(item)