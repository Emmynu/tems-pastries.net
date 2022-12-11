import random
choice=["rock","paper","scissors"]
players_choice=input("enter a guess (rock, paper, scissors): ")
computer_choice=random.choice(choice)
print(f'\nYou chose {players_choice}, computer chose {computer_choice}\n')
if players_choice== "rock" and computer_choice=="rock":
    print("its a tie")
elif players_choice== "rock" and computer_choice== "paper":
    print("paper cover rock.YOU LOSE!")
elif players_choice== "rock" and computer_choice== "scissors":
    print("Rock breaks scissors. YOU WIN!")

if players_choice== "scissors" and computer_choice=="scissors":
    print("its a tie")
elif players_choice== "scissors" and computer_choice== "rock":
    print("rocks breaks scissors.YOU LOSE!")
elif players_choice== "scissors" and computer_choice== "paper":
    print("scissors cuts paper. YOU WIN!")

if players_choice == "paper" and computer_choice == "paper":
    print("its a tie")
elif players_choice== "paper" and computer_choice== "scissors":
    print("scissors cuts paper.YOU LOSE!")
elif players_choice== "paper" and computer_choice== "rock":
    print("paper covers rock. YOU WIN!")

num_1 = float(input("enter a number: "))
operator = input("enter an operator: ")
num_2 = float(input("enter a number: "))
p
if operator== "+":
    print(num_1 + num_2)
elif operator== "*":
    print(num_1 * num_2)
elif operator== "-":
    print(num_1 - num_2)
elif operator== "/":
    print(num_1 / num_2)
elif operator == "**":
        print(num_1 ** num_2)
else:
    print("invalid syntax")

