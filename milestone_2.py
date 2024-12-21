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



import random

def create_word_list():
    """
    Returns a list of words (fruits).
    """
    return ["apple", "pears", "watermelon", "orange", "banana"]

def choose_random_word(word_list):
    """
    Chooses and returns a random word from the given list.
    """
    return random.choice(word_list)

def get_user_guess():
    """
    Prompts the user to input a single letter.
    Returns the guess as a string.
    """
    return input("Enter a single letter: ")

def validate_guess(guess):
    """
    Checks if the guess is a single alphabetical character.
    Returns True if valid; otherwise False.
    """
    return len(guess) == 1 and guess.isalpha()

def main():
    """
    Main function to run the Hangman steps for demonstration.
    """
    # Create the word list
    word_list = create_word_list()
    
    # Choose a random word
    word = choose_random_word(word_list)
    
    # (Optional) Show the word for debugging
    print("Randomly chosen word:", word)
    
    # Get and validate user guess
    guess = get_user_guess()
    
    if validate_guess(guess):
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")

if __name__ == "__main__":
    main()
