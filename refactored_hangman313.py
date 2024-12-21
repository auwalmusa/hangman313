import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has

    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        # Select a random word from the word list
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for _ in self.word]  # Initialize word_guessed with underscores
        self.num_letters = len(set(self.word))  # Count unique letters in the word
        self.num_lives = num_lives
        self.list_letters = []  # Initialize an empty list for guessed letters

        # Print initialization messages
        print(f"The mystery word has {len(self.word)} characters.")
        print(f"{' '.join(self.word_guessed)}")

    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.
        '''
        letter = letter.lower()
        if letter in self.word:
            print(f"Good guess! {letter} is in the word.")
            for index, char in enumerate(self.word):
                if char == letter:
                    self.word_guessed[index] = letter
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {letter} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        print(' '.join(self.word_guessed))

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        while True:
            letter = input("Guess a letter: ").lower()
            if len(letter) != 1 or not letter.isalpha():
                print("Please, enter just one character.")
            elif letter in self.list_letters:
                print(f"{letter} was already tried.")
            else:
                self.list_letters.append(letter)
                self.check_letter(letter)
                break


def play_game(word_list):
    '''
    The main function to play the Hangman game.
    Iteratively asks the user for a letter until the user guesses the word or runs out of lives.
    '''
    game = Hangman(word_list, num_lives=5)

    while True:
        if game.num_lives == 0:
            print(f"You lost! The word was {game.word}.")
            break
        elif game.num_letters == 0:
            print("Congratulations! You won!")
            break
        else:
            game.ask_letter()


if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
