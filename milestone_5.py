
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_" for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} live(s) left.")

    def ask_for_input(self):
        while True:
            guess = input("Enter a single letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess.lower() in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess.lower())
                self.check_guess(guess)
                break

# ----------------------------
# Milestone 5: The play_game function
# ----------------------------

def play_game(word_list):
    """
    A function that runs the entire game logic.
    1. Set num_lives to 5.
    2. Create an instance of Hangman with the given word_list and num_lives.
    3. Continuously check if the user has lives left or if they’ve guessed the word.
    4. Print "You lost!" or "Congratulations! You won the game!" accordingly.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives=num_lives)

    while True:
        # 1. Check if the user is out of lives
        if game.num_lives == 0:
            print("You lost!")
            print(f"The word was: {game.word}")
            break

        # 2. Check if there are still letters left to guess
        if game.num_letters > 0:
            # We continue the game by asking for input
            game.ask_for_input()
        else:
            # 3. If num_letters is 0, the user guessed all letters
            print("Congratulations! You won the game!")
            print(f"The word was: {''.join(game.word_guessed)}")
            break

# Step 2 in the instructions: call play_game with a list of words
if __name__ == "__main__":
    words = ["apple", "pears", "watermelon", "orange", "banana"]
    play_game(words)
