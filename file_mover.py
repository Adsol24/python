import os

src = input("input the source file you would like to move: ")
destination = input("input the directory you would like to move the file to: ")

try:
    if os.path.exists(destination):
        print("the file is already here")
    else:
        os.replace(src, destination)
        print("the file has been moved")
except FileNotFoundError:
    print(src + "was not found")