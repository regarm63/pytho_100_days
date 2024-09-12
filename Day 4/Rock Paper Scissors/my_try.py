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
print("Rock Paper Scissors Game")
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))

if player == 0:
    print(rock)
elif player == 1:
    print(paper)
else:
    print(scissors)

print("Computer chose: \n")

computer_choice = random.randint(0, 2,)

if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

if player >= 3 or player < 0:
    print("You typed an invalid number. You lose!")
elif player == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and player == 2:
    print("You lose!")
elif computer_choice > player:
    print("You lose!")
elif player > computer_choice:
    print("You win!")
elif computer_choice == player:
    print("It's a draw!")

# Another way of doing it using a matrix
# pics = [rock, paper, scissors]
#
# your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#
# if your_choice < 0 or your_choice > 2:
#     print("Don\'t enter numbers out of scope!'")
#     exit()
#
# print(pics[your_choice])
#
# comp_choice = random.randint(0, 2)
# print(f"Computer chose:\n{pics[comp_choice]}")
#
# choice_matrix = [["It\'s a draw", "You lose", "You win"],
#                 ["You win", "It\'s a draw", "You lose"],
#                 ["You lose", "You win", "It\'s a draw"]]
# print(choice_matrix[your_choice][comp_choice])