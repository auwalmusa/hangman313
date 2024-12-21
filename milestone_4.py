import random

class Hangman:
    """
    A class representing the Hangman game.
    
    Attributes:
        word_list (list[str]): A list of possible words to pick from.
        num_lives (int): How many incorrect guesses a player can make before losing.
        word (str): The randomly chosen word from word_list.
        word_guessed (list[str]): A list showing which letters are guessed. 
                                  Underscores for unguessed letters.
        num_letters (int): Number of UNIQUE letters in 'word' that haven't been guessed yet.
        list_of_guesses (list[str]): All letters the player has already guessed.
    """

    def __init__(self, word_list, num_lives=5):
        """
        Initialize the Hangman game with the provided list of words and number of lives.

        :param word_list: A list of possible words from which one is chosen randomly.
        :param num_lives: The number of lives (wrong guesses) allowed (default is 5).
        """
        self.word_list = word_list
        self.num_lives = num_lives

        # Randomly select a word from the list
        self.word = random.choice(self.word_list)

        # Represent unguessed letters in the word with underscores
        self.word_guessed = ["_" for _ in self.word]

        # The count of unique letters in the word
        self.num_letters = len(set(self.word))

        # Keep track of the letters guessed so far (in lowercase)
        self.list_of_guesses = []

        # (Optional) Debugging print to reveal the chosen word
        # print(f"DEBUG: The secret word is '{self.word}'")

    def check_guess(self, guess):
        """
        Check if 'guess' is in 'self.word' and update game state accordingly.
        
        Task 3 Recap:
        - If the guess is in 'word', replace the relevant underscores in 'word_guessed'.
        
        Task 4:
        - If the guess is NOT in 'word', reduce 'num_lives' by 1 and print the required messages.

        :param guess: The letter the user guessed.
        """
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            # Reveal each occurrence of the guessed letter
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            # Decrement the count of unique letters
            self.num_letters -= 1
        else:
            # Task 4: The guess is incorrect
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} live(s) left.")

    def ask_for_input(self):
        """
        Continuously ask the user for a single alphabetical character until we get a new valid guess.
        
        - If invalid (not one letter or not alpha), prompt again.
        - If already guessed, inform the player.
        - Else, record the guess and call check_guess().
        """
        while True:
            guess = input("Enter a single letter: ")

            # Validate the guess
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess.lower() in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess.lower())
                self.check_guess(guess)
                break  # Stop asking after processing one valid guess

    def __repr__(self):
        """
        Developer-friendly representation of the Hangman object for debugging.
        """
        return (
            f"Hangman(word='{self.word}', num_lives={self.num_lives}, "
            f"word_guessed={self.word_guessed}, num_letters={self.num_letters}, "
            f"list_of_guesses={self.list_of_guesses})"
        )

# Optional: Quick test if you run this file directly
if __name__ == "__main__":
    sample_words = ["apple", "pears", "watermelon", "orange", "banana"]
    game = Hangman(sample_words, num_lives=3)
    
    while game.num_lives > 0 and game.num_letters > 0:
        game.ask_for_input()
        if game.num_letters == 0:
            print(f"Congratulations! You guessed all letters of '{''.join(game.word_guessed)}'.")
            break
        elif game.num_lives == 0:
            print(f"You ran out of lives! The word was '{game.word}'.")
            break

    print("Game Over!")
    print("DEBUG:", game)
