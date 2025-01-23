import glob, os

os.chdir(r".\Day_14 - File System\test_dir") # Note quick and dirty way to get the right directory. "r"


print ("TXT files")
for file in glob.glob("*.txt"): 
    print(file)

print ("ALL files")
for file in glob.glob("*"): 
    print(file)
