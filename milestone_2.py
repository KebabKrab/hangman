import random
word_list = ["mango", "pineapple", "apple", "melon", "guava"]
word = random.choice(word_list)

guess = input("Guess a letter\n")
if len(guess)==1 and guess.isalpha()==True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

print(word)