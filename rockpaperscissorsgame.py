import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_img = [rock, paper,scissors]

usr_input = int(input("What do you choose? Type 0 for 'rock', type 1 for 'paper', type 2 for 'scissors'\n"))
print(game_img[usr_input])
comp_input = random.randint(0,2)
print(f"Computer choice: {comp_input}")
print(game_img[comp_input])

if usr_input >= 3 and usr_input < 0:
    print("Invalid number, Try again")
elif usr_input == 0 and comp_input == 2:
    print("You Won!!")
elif usr_input == 2 and comp_input == 0:
    print("You Lose!!")
elif comp_input > usr_input:
    print("you lose!!")
elif comp_input > usr_input:
    print("you Win!!")
elif comp_input == usr_input:
    print("Its draw!!, try again")

