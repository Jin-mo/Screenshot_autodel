import platform
import os

cwd = os.getcwd()

if platform.system() == "Windows":
    
    print("We're in Windows")
    os.chdir("Change to the directory/location where the file/folder is")
    cwd = "Location of specified Directory"

elif platform.system() == "Linux":
    
    print("We're in Linux")
    os.chdir("Change to the directory/location where the file/folder is")
    cwd = "Location of specified Directory" 

if cwd == "The directory/location from where the python script is being executed": #This is to make sure the script doesn't auto delete itself and any other files
    exit()

elif cwd == "Location of specified Directory" or cwd == "Location of specified Directory":
    lst = []
    for file in os.listdir():
        lst.append(file)

    if len(lst) > 0:
        for file in os.listdir():
            os.remove(file)
    else:
        print("Folder is empty.")

else:
    print("Unspecified Working Directory, abort!!")
    exit()
