import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_of_guesses: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_guess(guess)
        Checks if the letter is in the word.
    ask_for_input()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

        print(self.word_guessed)
        
    def check_guess(self, guess):
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        guess: str
            The letter to be checked
        '''
        guess = guess.lower()
        if guess in self.word:  # Reduces number of letters to be guessed by 1 if guess is correct
            print(f"Good guess! '{guess}' is in the word.")
            for index in range(len(self.word)):
                if self.word[index] == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
        
        else:   # Reduces number of lives by 1 if guess is incorrect
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_guess method.
        '''
        while True:
            guess = input("Guess a letter.\n")
            guess = guess.lower()
            if len(guess)!=1 or guess.isalpha()==False: # Rejects guess if it is not a single letter
                print("Invalid letter. Please enter a single alphabetical character.")
            
            elif guess in self.list_of_guesses: # Rejects guess if it has already been guessed
                print("You already tried that letter!")
            
            else: # Checks whether guess is correct and adds it to list of guesses
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print(f"Letters guessed: {self.list_of_guesses}")
                print(self.word_guessed)
                break

def play_game(word_list):
    '''
    This function is used to run and play the hangman game
    
    Args:
    ----
    word_list: str
        The list of words the computer can choose from
    '''
    game = Hangman(word_list, num_lives=5)
    while True:
        if game.num_lives == 0:
            print(f"YOU LOST! The word was '{game.word}'.")
            break
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_lives!=0 and game.num_letters==0:
            print("CONGRATULATIONS. You won the game!")
            break

if __name__ == "__main__":
    fruits = ["apple", "banana", "strawberry", "watermelon", "pineapple", "passionfruit", "guava", "papaya"]
    play_game(fruits)