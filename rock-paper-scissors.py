import day4_31

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

options = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(options[user_choice])

print("Computer chose: ")
computer_choice = random.randint(0, 2)
print(options[computer_choice])

if user_choice == 0 and computer_choice == 0:
    print("It's a draw.")
elif user_choice == 0 and computer_choice == 1:
    print("You lose.")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 1:
    print("It's a draw.")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 1 and computer_choice == 2:
    print("You lose.")
elif user_choice == 2 and computer_choice == 2:
    print("It's a draw.")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose.")
else:
    print("Invalid input! Please start again.")