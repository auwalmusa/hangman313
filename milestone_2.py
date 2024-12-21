import random

#Step 1:
#Creating a list containing the names of 5 favorite fruits.
my_favourite_fruits = ["apple", "pears", "watermelon", "orange", "banana"]

# step assingin he list of my favourite fruite to variable word_list
word_list = my_favourite_fruits

#step 3; printing out the created list(word_list)
print(word_list)

#step 4: selecting a random word from the list using randon.choice() function
word = random.choice(word_list)

#step 5: printing out the selected random word
print(word)

#task 3
guess = input("Enter a single letter: ")
print("Your guesses letter:", guess)

#task 4
if len(guess) == 1 and guess.isalpha():
    print("Good Guess")
else:
    print("Oops! That is not a valid input")
