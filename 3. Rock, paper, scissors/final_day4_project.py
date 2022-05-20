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

position=[rock, paper, scissors]

your_choose=input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if your_choose == "0":
    print(rock)
elif your_choose == "1":
    print(paper)
elif your_choose == "2":
    print(scissors)

print("Computer chose: \n")
computer=random.randint(0,2)
#print(computer)
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
elif computer == 2:
    print(scissors)

if your_choose == "0" and computer == 2:
    print("You win!")
elif your_choose == "2" and computer == 0:
    print("Computer wins!")
elif your_choose == "2" and computer == 1:
    print("You win!")
elif your_choose == "1" and computer == 2:
    print("Computer wins!")
elif your_choose == "1" and computer == 0:
    print("You win!")
elif your_choose == "0" and computer == 1:
    print("Computer wins!")
elif (your_choose == "0" and computer == 0) or (your_choose == "1" and computer == 1) or (your_choose == "2" and computer == 2):
    print("Draw!")
else:
    print("You typed an invalid number, you lose!")
