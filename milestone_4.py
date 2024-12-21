import random

class Hangman:
    """
    A class representing the Hangman game.
    """

    def __init__(self, word_list, num_lives=5):
        """
        Initialize the Hangman game with the provided word list and number of lives.
        """
        self.word_list = word_list
        self.num_lives = num_lives

        # Pick a random secret word
        self.word = random.choice(self.word_list)

        # Create a list of underscores for each character in the secret word
        self.word_guessed = ["_" for _ in self.word]

        # Count how many UNIQUE letters are in the secret word
        self.num_letters = len(set(self.word))

        # Keep track of every letter guessed so far
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        Convert 'guess' to lowercase, check if it's in 'word', 
        and print an appropriate message.
        """
        guess = guess.lower()  # ensure we handle lowercase only

        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            # (Further logic for updating self.word_guessed 
            # or self.num_letters will come in a later milestone.)
        else:
            print(f"Sorry, '{guess}' is not in the word. Try again.")
            # (You might decrement self.num_lives here, in a future milestone.)

    def ask_for_input(self):
        """
        Continuously ask the user for a single alphabetical letter. 
        - If invalid, print an error.
        - If it's already guessed, print a warning.
        - Otherwise, call check_guess() and append to list_of_guesses.
        """
        while True:
            guess = input("Enter a single letter: ")

            # Check if guess is a single alphabetical character
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please enter a single alphabetical character.")
            # Check if we have guessed this letter before
            elif guess.lower() in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                # We have a new, valid guess → call check_guess
                self.check_guess(guess)
                # Append the guess (in lowercase) to the list_of_guesses
                self.list_of_guesses.append(guess.lower())
                break

    def __repr__(self):
        """
        Developer-friendly string representation for debugging.
        """
        return (
            f"Hangman(word='{self.word}', num_lives={self.num_lives}, "
            f"word_guessed={self.word_guessed}, list_of_guesses={self.list_of_guesses})"
        )

# Optional: test code
if __name__ == "__main__":
    sample_words = ["apple", "banana", "orange", "mango", "grape"]
    game = Hangman(sample_words)
    print("DEBUG:", game)  # Show initial state
    game.ask_for_input()   # Test the new method
    print("DEBUG after guess:", game)
