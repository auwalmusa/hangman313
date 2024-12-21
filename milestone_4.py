import random

class Hangman:
    """
    A class representing the Hangman game.
    """

    def __init__(self, possible_words, lives=5):
        """
        Initialize the Hangman game.
        
        :param possible_words: A list of possible words from which one is randomly chosen.
        :param lives: The number of wrong guesses allowed (default = 5).
        """
        self.possible_words = possible_words
        self.lives = lives

        # Pick a secret word
        self.secret_word = random.choice(self.possible_words)

        # Create a list of underscores for each character
        self.revealed_word = ["_" for _ in self.secret_word]

        # Count how many UNIQUE letters in the secret word
        self.remaining_unique_letters = len(set(self.secret_word))

        # Track all guessed letters (in lowercase)
        self.guessed_letters = []

        # Debug (comment out if desired)
        # print(f"DEBUG: secret_word = {self.secret_word}")

    def prompt_for_guess(self):
        """
        Prompt the user for a single alphabetical character and validate it.
        
        :return: A valid (new) guess as a lowercase string, or None if invalid or repeated.
        """
        guess = input("Enter a single letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please enter a single alphabetical character.")
            return None

        if guess in self.guessed_letters:
            print("You already tried that letter!")
            return None

        return guess

    def check_guess(self, guess):
        """
        Check if 'guess' is in the secret word. Update game state and print messages.
        
        :param guess: A single lowercase letter that has not been guessed before.
        """
        self.guessed_letters.append(guess)

        if guess in self.secret_word:
            print(f"Good guess! '{guess}' is in the word.")
            # Reveal all instances of the guessed letter
            for index, letter in enumerate(self.secret_word):
                if letter == guess:
                    self.revealed_word[index] = guess
            # Decrement the count of unique letters
            self.remaining_unique_letters -= 1
        else:
            # Decrement a life if incorrect
            self.lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.lives} live(s) left.")

    def play_turn(self):
        """
        Play a single turn of the game by asking for a guess and handling the result.
        
        :return: True if a valid guess was made (even if it's wrong), False if input was invalid.
        """
        guess = self.prompt_for_guess()
        if guess is None:
            # Invalid or repeated guess
            return False
        
        self.check_guess(guess)
        return True

    def is_word_guessed(self):
        """
        Check if all unique letters have been discovered.
        
        :return: True if 'remaining_unique_letters' is 0, else False.
        """
        return self.remaining_unique_letters == 0

    def is_out_of_lives(self):
        """
        Check if the player has run out of lives.
        
        :return: True if 'lives' is 0, else False.
        """
        return self.lives == 0

    def __repr__(self):
        """
        Developer-friendly representation for debugging.
        """
        return (
            f"Hangman(secret_word='{self.secret_word}', lives={self.lives}, "
            f"revealed_word={self.revealed_word}, "
            f"remaining_unique_letters={self.remaining_unique_letters}, "
            f"guessed_letters={self.guessed_letters})"
        )

# Example usage / test code
if __name__ == "__main__":
    words = ["apple", "banana", "orange", "mango", "grape"]
    game = Hangman(words, lives=3)

    while not game.is_word_guessed() and not game.is_out_of_lives():
        print("Current progress:", " ".join(game.revealed_word))
        
        # Keep looping until user makes a valid attempt
        valid_turn = game.play_turn()
        if not valid_turn:
            # If turn was invalid, keep trying without reducing a life
            continue

        # If the guess was valid, check conditions
        if game.is_word_guessed():
            print(f"Congratulations! The word was '{''.join(game.revealed_word)}'.")
        elif game.is_out_of_lives():
            print(f"You ran out of lives! The word was '{game.secret_word}'.")

    print("Game Over!")
    print("DEBUG:", game)
