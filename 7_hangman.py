import random
import time
from hangman_accessories import *

print(opening_art)
print("Welcome to hangman!")
def hangman_game():
    # Game start setup
    random.seed(time.time())
    chosen_word = random.choice(word_list).lower()
    chosen_word_length = len(chosen_word)
    lives = -1    
    guessed_letters = []
    
    # Use for debugging as needed
    # print(chosen_word)
    
    # Initialize a list to show the player how many letters the word will be
    displayed_word = ["_"] * chosen_word_length
    print(f"Your word is {chosen_word_length} characters long.")
    print(" ".join(displayed_word))
    
    # Set game as playable until out of lives, then game over
    while ''.join(displayed_word) != chosen_word and lives > len(stages) * -1:
        letter_guess = input("Guess a letter:\n").lower()
        if letter_guess in guessed_letters:
            print(stages[lives])
            print(" ".join(displayed_word))
            print(f"You have already guessed {letter_guess}, please try another letter")
            print(f"Guessed Letters: {guessed_letters_str}")
        else:
            if letter_guess in chosen_word:
                for place in range(chosen_word_length):
                    letter = chosen_word[place]
                    if letter == letter_guess:    
                        displayed_word[place] = letter
                guessed_letters.append(letter_guess)
                guessed_letters_str = ", ".join(guessed_letters)
                print(stages[lives])
                print(f"The letter '{letter_guess}' is in this word, well done.")
                print(f"Guessed Letters: {guessed_letters_str}")
            else:
                lives -= 1
                guessed_letters.append(letter_guess)
                guessed_letters_str = ", ".join(guessed_letters)
                print(stages[lives])
                print(f"The letter '{letter_guess}' is not in this word, please try again.")
                print(f"Guessed Letters: {guessed_letters_str}")
            print(" ".join(displayed_word))
    
    if ''.join(displayed_word) == chosen_word:
        print("WAY TO GO! YOU WIN!")
    else:
        print(f"The word was {chosen_word}.")
        print("You lose, try again.")

play_again = True
while play_again:
    hangman_game()
    response = input("Would you like to play again? (yes/no):\n").lower()
    if response != "yes":
        play_again = False
        print("\nThank you for playing! This window will close in a few seconds. Goodbye.")
        time.sleep(3)