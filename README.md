# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

This project is made with python 3.11.4.

In order to play the game, the user types in a letter as a guess, and the computer tells them whether the guess is right or wrong, adding the letter to the corresponding location in the word if right, and causing the user to lose a life if wrong.

miletone_2.py defines a list of possible words and randomly selects one of them. It then asks the user to input a letter as a guess and checks whether the input is valid, i.e. whether the input is a single alphabetical character.

milestone_3.py builds on the functionality of milestone_2.py. After asking for user input to guess a letter and making sure that it's a valid guess, it then checks whether the inputted letter is in the selected word.

milestone_4.py utilises OOP to create a Hangman class containing attributes relaating to aspects of the game such as the chosen word from the word list, the number of lives the user has left, and a list of unique letters guessed. Two methods are defined: one which checks that the letter that the user guesses is contained within the chosen word, and another which asks the user for input, ensures that the guess is valid and calls the check_guess() method.