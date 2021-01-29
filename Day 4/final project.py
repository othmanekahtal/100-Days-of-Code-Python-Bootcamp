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
list=[rock,paper,scissors]
choice = int(input("What do you choose? Type 0 for Rock , 1 for paper or 2 for scissors."))
choice_computer = random.randint(0,2)
# my code ⬇️:
# if (choice == 0 and choice_computer ==1) or (choice == 1 and choice_computer == 2) or (choice==2 and choice_computer == 0):
if(choice>2):
    print("You Enter invalid Number, Try again!")
elif (choice < choice_computer) or (choice==2 and choice_computer == 0):
    print(f"You choice : \n{list[choice]}")
    print(f"computer choice : \n{list[choice_computer]}")
    print("You lose")
elif choice==choice_computer:
    print(f"You choice : \n{list[choice]}")
    print(f"computer choice : \n{list[choice_computer]}")
    print("it's a draw")
else:
    print(f"You chose : \n{list[choice]}")
    print(f"computer chose : \n{list[choice_computer]}")
    print("=====result = You win=====")