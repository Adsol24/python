numb = int(input("enter a positive integer: "))

count = 0

for i in range (1,numb + 1):
    if i % 2 == 0:
        count += 1

print("The number of even numbers from 1 to", numb, "is:", count)
