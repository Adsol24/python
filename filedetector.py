import os

#file detector
Path = input("input the path of the file: ")

if os.path.exists(Path):
    print("this location exists")
    if os.path.isfile(Path):
        print("this is a file")
    else:
        print("this location doesnt exist")
        


