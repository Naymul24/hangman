import random

word_list = ['apple', 'banana', 'mangos', 'lychee', 'orange']

word = random.choice(word_list)

class Hangman:
    """
    The Hangman class keeps track of the word to be guessed, the player's progress, lives remaining, and guessed letters.

    Attributes:
    - word (str): The word to be guessed.
    - word_guessed (list): A list of the number of letters in the word denoted with an underscore until a correct letter is guessed
    - num_letters (int): The number of unique letters in the word that have not been guessed yet.
    - num_lives (int): The number of lives the player has.
    - word_list (list): A list of the 5 fruits
    - list_of_guesses (list): A list of the letters that have already been tried.
    """
    def __init__(self, word_list, num_lives=5):
        """
        Initialises a new Hangman game instance.

        All attributes have been initialised.
        """
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        Checks if the guessed letter is in the word and updates the word_guessed variable.

        - Argument is guess and returns nothing
        - guess is ensured to be lower case when executing the if statement
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for letters in range(len(self.word)):
                if self.word[letters] == guess:
                    self.word_guessed[letters] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """
        Asks the player to enter a single letter, checks the input, and processes the guess.

        - No Arguments and Returns
        """
        while True:
            guess = input("enter a single letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

Hangman(word_list).ask_for_input()
