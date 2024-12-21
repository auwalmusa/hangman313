import random

def create_word_list():
    """
    Returns a list of possible words.
    """
    return ["apple", "pears", "watermelon", "orange", "banana"]

def check_guess(guess, word):
    """
    Converts the guess to lowercase and checks if it is in 'word'.
    Prints an appropriate message.
    """
    guess = guess.lower()  # Convert the guess to lowercase
    
    if guess in word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def ask_for_input(word):
    """
    Continuously asks the user for a valid single-letter guess.
    Once a valid guess is entered, calls check_guess() to see if it is in 'word'.
    """
    while True:
        guess = input("Enter a single letter: ")
        
        # Check if guess is a single alphabetical character
        if len(guess) == 1 and guess.isalpha():
            check_guess(guess, word)  # Pass guess and word to check_guess()
            break  # After one valid guess, we break. 
                   # Later, you can expand the logic for multiple rounds.
        else:
            print("Invalid letter. Please enter a single alphabetical character.")

def main():
    # 1. Create a list of words
    word_list = create_word_list()
    
    # 2. Choose one random word
    word = random.choice(word_list)
    
    # (Optional) Print the chosen word for debugging
    print("SECRET WORD (for testing):", word)
    
    # 3. Call ask_for_input() to prompt the user, then check the guess
    ask_for_input(word)

# Standard Python practice to call main() if this file is run directly
if __name__ == "__main__":
    main()
