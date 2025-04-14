import os
# Specify the directory you want to list
directory_path = '/your/directory/path'

# list all files and directories in the specify
contents = os.listdir(directory_path)

# print each file and directory name
for item in contents:
    print(item)