import random

word_list = ['apple', 'banana', 'mangos', 'lychee', 'orange']

word = random.choice(word_list)


def ask_for_input():
    while True:
        guess = input("Enter a single letter: ")
        
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid input. Please, enter a single alphabetical character.")

guess = ask_for_input()

def check_guess(guess):
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

check_guess(guess)