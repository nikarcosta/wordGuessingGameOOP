import random

class WordGame:
    def __init__(self, words_file):
        self.words_file = words_file
        self.random_word = ""
        self.secret_word = ""
        self.available_guesses = 0
        self.total_guesses = 0

    def load_words(self):
        with open(self.words_file, 'r') as file:
            words = file.read().splitlines()
        self.random_word = random.choice(words)
        self.available_guesses = len(self.random_word)
        self.secret_word = "*" * self.available_guesses

    def display_welcome_message(self):
        print("====Welcome To Guessing The Word game!====")
        print("Here is the word you have to guess:")
        print(self.secret_word)
        print(f"You have {self.available_guesses} chances to guess the word!")

    def guess_letter(self, letter):
        if letter not in self.random_word:
            print(f"Try again! You have {self.available_guesses - self.total_guesses} chances left.")
        else:
            new_secret_word = list(self.secret_word)
            for idx, alphabet in enumerate(self.random_word):
                if alphabet == letter:
                    new_secret_word[idx] = letter
            self.secret_word = "".join(new_secret_word)
            print(self.secret_word)
            if self.secret_word == self.random_word:
                return True
            print(f"You have {self.available_guesses - self.total_guesses} chances left.")

        return False

    def play_game(self):
        self.load_words()
        self.display_welcome_message()

        while self.total_guesses < self.available_guesses and self.secret_word != self.random_word:
            self.total_guesses += 1
            letter = input("Enter a letter: ")
            if self.guess_letter(letter):
                break

        if self.secret_word == self.random_word and self.total_guesses <= self.available_guesses:
            print("Congrats! You won!")
        else:
            print(f"The correct word was: {self.random_word}. Better luck next time!")

game = WordGame('word_list.txt')
game.play_game()
