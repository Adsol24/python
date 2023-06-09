numbers = input("Enter a series of numbers: ").split()

# Convert the list of strings to a list of integers
numbers = [int(num) for num in numbers]

maximum = max(numbers)
minimum = min(numbers)

print("Maximum number:", maximum)
print("Minimum number:", minimum)

