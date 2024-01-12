# Hangman
## Introduction
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

In order to play the game, the user types in a letter as a guess, and the computer tells them whether the guess is right or wrong, adding the letter to the corresponding location in the word if right, and causing the user to lose a life if wrong.

This project aims to put into practice basics of python programming, as well as principles of Object Oriented Programming (OOP) and good code documentation. I have learnt how to use git and GitHub to track changes and progress, and consolidated my previous understanding and experience with python.

This project is made with python 3.11.4.

## Program Functionality & Usage
To play hangman, simply run the final project file (milestone_5.py) directly from the terminal or in an IDE. The 'random' module must be installed.

The program chooses a random word out of a list of words inputted into a function called to play the game, after which it prints a list of underscores symbolising blank spaces where letters should go in the word. It then asks the user to input a letter, which should be a single alphabetic character. If this isn't the case, the program lets the user know that the input is not valid and asks them to try again. If the input is valid, it then checks whether the letter is found within the word. If it is, the list of underscores is altered and the letter replaces the underscore at the place where it should be in the chosen word. If not, the user loses a life.

The game ends either when the player loses all of their lives (by default this is set to 5) in which case the game is lost, or if there are lives remaining and all the letters in the word are found, the game is won.

## License Information
MIT License

Copyright (c) 2023 Rakin Chowdhury

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
