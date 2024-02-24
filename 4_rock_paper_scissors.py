import random
import time

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("Welcome to Rock, Paper, Scissors!")

def play_game():
    random.seed(time.time())
    while True:
        choice = input("What do you choose? (rock/paper/scissors)\n").lower()
        if choice == "rock":
            choice = 0
            break
        elif choice == "paper":
            choice = 1
            break
        elif choice == "scissors":
            choice = 2
            break
        else:
            print("Please choose one of the following: (rock/paper/scissors)")

    computer_choice = random.randint(0,2)

    win = "Congratulations! You win!!"
    lose = "Bummer deal brah, you lost."
    tie = "You chose the same as the computer, you tie."
    print("Ready?")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("GO!")
    time.sleep(.5)
    if choice == 0:
        print(Rock)
    elif choice == 1:
        print(Paper)
    elif choice == 2:
        print(Scissors)
    print("VS")
    if computer_choice == 0:
        print(Rock)
    elif computer_choice == 1:
        print(Paper)
    elif computer_choice == 2:
        print(Scissors)

    if choice == 0 and computer_choice == 0:
        print(tie)
    elif choice == 0 and computer_choice == 1:
        print(lose)
    elif choice == 0 and computer_choice == 2:
        print(win)
    elif choice == 1 and computer_choice == 0:
        print(win)
    elif choice == 1 and computer_choice == 1:
        print(tie)
    elif choice == 1 and computer_choice == 2:
        print(lose)
    elif choice == 2 and computer_choice == 0:
        print(lose)
    elif choice == 2 and computer_choice == 1:
        print(win)
    elif choice == 2 and computer_choice == 2:
        print(tie)

while True:
    play_game()
    play_again = input("Do you want to play again? (type 'yes' to play again, or anything else to close this window)\n").lower()
    if play_again != "yes":
        print("Thank you for playing! This window will close in a few seconds")
        time.sleep(3)
        break
