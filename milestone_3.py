import random

def get_possible_words():
    """
    Return a list of possible words to guess.
    """
    return ["apple", "banana", "orange", "mango", "grape"]

def is_valid_guess(guess):
    """
    Check if the user's guess is a single alphabetical character.
    
    :param guess: The user's raw input string
    :return: True if valid (one letter and alphabetic), otherwise False
    """
    return len(guess) == 1 and guess.isalpha()

def prompt_for_guess():
    """
    Continuously ask the user for a valid guess.
    Return the guess once it's valid.
    """
    while True:
        guess = input("Enter a single letter: ")
        if is_valid_guess(guess):
            return guess.lower()  # convert to lowercase in one place
        else:
            print("Invalid letter. Please enter a single alphabetical character.")

def check_guess_in_word(guess, secret_word):
    """
    Check if 'guess' is contained in 'secret_word', and print a message.
    
    :param guess: A single lowercase letter
    :param secret_word: The randomly chosen word
    """
    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def play_hangman():
    """
    Main function to run a single guess cycle of the Hangman game.
    """
    word_list = get_possible_words()
    secret_word = random.choice(word_list)
    
    # Debug: Uncomment if you want to see the word
    # print("DEBUG - Secret word:", secret_word)
    
    # Get a valid guess from the user
    guess = prompt_for_guess()
    
    # Check whether the guess is in the secret word
    check_guess_in_word(guess, secret_word)

if __name__ == "__main__":
    play_hangman()
