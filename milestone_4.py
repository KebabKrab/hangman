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
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            for index in range(len(self.word)):
                if self.word[index] == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        print(self.word_guessed)

    def ask_for_input(self):
        '''
        This function asks the user for input and validates it
        '''
        print(self.list_of_guesses)
        while True:
            guess = input("Guess a letter.\n")
            guess = guess.lower()
            if len(guess)!=1 or guess.isalpha()==False:
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

word_list = ["apple", "banana", "strawberry", "watermelon", "pineapple", "passionfruit", "guava", "papaya"]
game = Hangman(word_list)
game.ask_for_input()
