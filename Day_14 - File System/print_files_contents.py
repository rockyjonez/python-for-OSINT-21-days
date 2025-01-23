import glob, os

os.chdir(r".\Day_14 - File System\test_dir") # Note quick and dirty way to get the right directory. "r"

for file in glob.glob("*.txt"): 

    with open (file) as current_file:
        print(current_file.readlines())
