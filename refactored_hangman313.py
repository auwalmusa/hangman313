import random

class Hangman:
    """
    A class to manage the Hangman game logic.
    """

    def __init__(self, possible_words, lives=5):
        """
        Initialize the Hangman game with a list of possible words and a set number of lives.

        :param possible_words: A list of words from which one is randomly chosen as the secret word.
        :param lives: The maximum number of incorrect guesses allowed (default: 5).
        """
        self.possible_words = possible_words
        self.lives = lives

        # Pick the secret word
        self.secret_word = random.choice(self.possible_words)

        # A list of underscores for each character in the secret word
        self.revealed_word = ["_" for _ in self.secret_word]

        # Count how many unique letters remain to be guessed
        self.remaining_letters = len(set(self.secret_word))

        # Track the letters guessed so far (in lowercase)
        self.guessed_letters = []

        # Debug line (comment out or remove in production)
        # print(f"DEBUG: Secret word = {self.secret_word}")

    def prompt_for_guess(self):
        """
        Prompt and validate user input for a single alphabetical character.
        
        :return: A valid new guess as a lowercase string, or None if invalid or already guessed.
        """
        guess = input("Enter a single letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter one alphabetical character.")
            return None
        if guess in self.guessed_letters:
            print("You already tried that letter!")
            return None

        return guess

    def check_guess(self, guess):
        """
        Check the guess against the secret word, update the revealed_word, 
        reduce lives if incorrect, and print feedback.

        :param guess: A single, valid lowercase letter that wasn't guessed previously.
        """
        # Record the guess
        self.guessed_letters.append(guess)

        if guess in self.secret_word:
            print(f"Good guess! '{guess}' is in the word.")
            # Reveal all instances of guess
            for idx, letter in enumerate(self.secret_word):
                if letter == guess:
                    self.revealed_word[idx] = guess

            # One less unique letter to find
            self.remaining_letters -= 1
        else:
            self.lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"Lives remaining: {self.lives}")

    def play_turn(self):
        """
        Manage a single turn by prompting for a guess and processing it. 
        :return: True if a valid guess was processed, False otherwise.
        """
        guess = self.prompt_for_guess()
        if guess is None:
            return False  # The user input was invalid or repeated
        self.check_guess(guess)
        return True

    def is_solved(self):
        """
        Check if all unique letters have been guessed.
        """
        return self.remaining_letters == 0

    def is_alive(self):
        """
        Check if the player still has lives left.
        """
        return self.lives > 0

    def __repr__(self):
        """
        Developer-friendly string representation for debugging.
        """
        return (
            f"Hangman(secret_word='{self.secret_word}', lives={self.lives}, "
            f"revealed_word={self.revealed_word}, remaining_letters={self.remaining_letters}, "
            f"guessed_letters={self.guessed_letters})"
        )

def play_game(word_list, lives=5):
    """
    Orchestrate the entire Hangman game loop, using the Hangman class.
    
    :param word_list: A list of words to pick from.
    :param lives: Number of lives to allow. Default is 5.
    """
    game = Hangman(word_list, lives)

    print("Welcome to Hangman!")
    while game.is_alive() and not game.is_solved():
        # Show progress
        print("Current word:", " ".join(game.revealed_word))
        
        valid_turn = game.play_turn()
        # If the turn wasn't valid, skip losing a life or revealing anything
        if not valid_turn:
            continue

    # Final outcome
    if not game.is_alive():
        print(f"You lost! The word was: {game.secret_word}")
    else:
        print(f"Congratulations, you guessed the word: {''.join(game.revealed_word)}!")

# For direct testing
if __name__ == "__main__":
    words = ["apple", "pears", "watermelon", "orange", "banana"]
