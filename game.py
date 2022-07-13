
import random



print("WELCOME TO ROCK PAPER SCISSORS GAME")


# USER INPUTS

user_choice = input("Please make a selection ('rock', 'paper', 'scissors'): ")
user_choice = user_choice.lower()

# You chose : 'rock'
print("You chose:", user_choice)  # SUFFICIENT!!
print(f"You chose: '{user_choice}' ")


# VALIDATE USER INPUTS

valid_options = ["rock", "paper", "scissors"]

# breakpoint()

# if user_choice in valid_options:
 #   # ALL THE STUFF INDENTED
# else:
 #   print("OOPS INVALID TRY AGAIN")

if user_choice not in valid_options:
    print("OOPS INVALID TRY AGAIN")
    exit()  # quit()






# COMPUTER  CHOICE


# IMPORT RANDOM


computer_choice = random.choice(valid_options)
print("Computer chose:", computer_choice)


# DETERMINE THE WINNER

# adapted from code shared in slack by Bonnie
# https://nyu-tech-2335.slack.com/archives/C5WPFSB52/p1657672686150239

if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("Rock crushes scissors. You win!")
    else:
        print("Paper covers rock. You lose.")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Paper covers rock. You win!")
    else:
        print("Scissors cuts paper. You lose.")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors cuts paper. You win!")
    else:
        print("Rock crushes scissors. You lose.")

# DISPLAY RESULTS
#
#--------------------------------
