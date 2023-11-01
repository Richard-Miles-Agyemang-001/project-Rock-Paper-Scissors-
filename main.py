import random

print('TEST')

a = 1000
b = 100
if a == b:
    print('success')
else:
    print('//////''error////')


user_action = input("Enter your choice(rock,paper,scissors): ")
possible_actions = ["rock", "paper", "scissor"]
computer_action = random.choice(possible_actions)
print(f"\n your choice is {user_action}, computer chose {computer_action}")


# if __name__ == '__main__':
#     app.run(debug=True)


