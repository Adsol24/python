import random

choices = ["rock", "paper", "scissors"]

user_input = None
while user_input not in choices:
    user_input = input("type rock paper or scissors: ").lower()

comp = random.choice(choices)

print("you picked: " + user_input)
print("computer picks: " + comp)

if comp == "rock" and user_input == "paper":
    print("you win")
if comp == "paper" and user_input == "rock":
    print("you lose")
if comp == "scissors" and user_input == "paper":
    print("you lose")
if comp == "paper" and user_input == "scissors":
    print("you win")
if comp == "rock" and user_input == "scissors":
    print("you lose")
if comp == "scissors" and user_input == "rock":
    print("you win")
if comp == user_input:
    print("it is a draw")



