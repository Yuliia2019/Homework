import os
base_directory = "C:\\"
files = os.listdir (base_directory)
print files
sum_files = 0
sum_dirs = 0
for file_name in files:
    if os.path.isdir(base_directory+file_name):
        sum_dirs+=1
    elif os.path.isfile(base_directory+file_name):
        sum_files+=1
print len (files), sum_files, sum_dirs
