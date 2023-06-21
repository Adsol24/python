path = input("copy and paste the path of the file here: ")
try:
    with open('name of file path') as file:
        print(file.read())

        print(file.closed)

except FileNotFoundError:
    print("this file was not found")

