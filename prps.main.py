#intoducing project rock-paper-scissors
import random

while True:
user_action = input ("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper","scissors"]
computer _action = random.choice (possible _actions)
print (f" \nYou chose{user_action}, computer chose {computer _action}. In")

if user action == computer_ action:
print (f"Both players selected {user _action}. It's a tie!")
elif user action == "rock":
if computer action ==
"scissors"
print ("Rock smashes scissors! You win!")
else:
print ("Paper covers rock! You lose.")
elif user action == "paper" :
if computer action == "rock":
print ("Paper covers rock! You win!")
else:
print("scissors cuts papper! You lose.")
elif user_action ==
"scissors":
if computer action == "paper":
print ("Scissors cuts paper! You win!")
else:
print ("Rock smashes scissors! You lose.")
play_again = input ("Play again? (y/n): ")
if play_again.lower != "y":
break