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
