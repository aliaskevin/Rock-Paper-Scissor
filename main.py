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

import random
game = [rock, paper, scissors]
choice = int(input("what do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
if choice > 2:
    print("You typed a wrong selection")
else:
    print(game[choice])
    pc = random.randint(0,2)
    print(f"\nComputer chose:\n")
    print(game[pc])
    if (choice == 0 and pc == 0) or (choice == 1 and pc == 1) or (choice == 2 and pc == 2):
      print("Draw")
    elif (choice == 0 and pc == 1) or (choice == 1 and pc == 2) or (choice == 2 and pc == 0):
      print("You loose")
    elif (choice == 0 and pc == 2) or (choice == 1 and pc == 0) or (choice == 2 and pc == 1):
      print("You Win")
