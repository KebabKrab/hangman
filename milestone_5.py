import random

class Hangman:
    '''
    This class is used to represent a game of hangman.
    
    Attributes:
        word_list (list): the list of words the computer can choose from
        num_lives (int): the number of lives the user has remaining
        word (str): the chosen word
        word_guessed (list): list of underscores to be replaced with letters of the word when correctly guessed
        num_letters (int): number of letters left to be guessed in the word
        list_of_guesses (list): list of all letters previously guessed
    '''
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        
    def check_guess(self, guess):
        '''
        This function checks whether the inputted guess is within the chosen word

        Args:
            guess (str): the guess inputted by the user
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
        This function asks the user for input and validates it
        '''
        print(self.word_guessed)
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
                break
                

fruits = ["apple", "banana", "strawberry", "watermelon", "pineapple", "passionfruit", "guava", "papaya"]
    
def play_game(word_list):
    '''
    This function is used to run and play the hangman game
    
    Args:
        word_list (list): the list of words the computer can choose from
    '''
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    while True:
        if game.num_lives == 0:
            print("YOU LOST!")
            break
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_lives!=0 and game.num_letters==0:
            print("CONGRATULATIONS. You won the game!")
            break

play_game(fruits)