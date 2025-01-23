import glob, os, re 

regexp = re.compile('[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+')

os.chdir(r".\Day_14 - File System\test_dir") # Note quick and dirty way to get the right directory. "r"

for file in glob.glob("*"): 

    with open (file) as current_file:
        current_file_content=current_file.read()       
        if regexp.search(current_file_content):
            print("Match in file: "+file)
            print(current_file_content)
