import random
print("guess the dice game")
user_input = (int(input("input your guess: ")))

Dice = random.randint(1,6)
print("a " + str(Dice), "was rolled")

if user_input == Dice:
    print("you are correct")
else:
    print("you are incorrect")
    