from game.chute import chute
from game.words import word_list
from game.words import words


class _Jumper:

    def __init__(self):
        self.win = False
        self.lose = False

        self.correct_word = word_list
        self.show_word = list(len(self.correct_word) * '_')

        self.attempt = ""
        self.attempts_amount = 4

    def _attempt_letter(self, letter):
        for i in range(0, len(self.correct_word)):
            letter = self.correct_word[i]

            if self.attempt == letter:
                self.show_word[i] = self.attempt

    def _play_game(self):
        # Loop to get player letter and play game
        while not self.win and self.attempts_amount > 0:
            self.show_word()

            self.attempt = input('Guess a letter: ')
            self.attempt = self.attempt.upper()

            if self.attempt == self.correct_word:
                self.win = True
                self.show_word = self.correct_word
                
            if len(self.attempt) == 1 and self.attempt in self.correct_word:
                self.win = self._attempt_letter(self.attempt, self.correct_word)
            else:
                self.attempts_amount -= 1

            # Prints if guess is right
            if self.win:
                print(f"Correct! You guessed {self.correct_word}\n")
            else:
                print("Sorry, that's not correct\n")

            # Prints if guess is wrong
            if self.attempts_amount == 0:
                self.lose = True
            if self.lose:
                print(chute[4])
                print("You lose")
                print(self.correct_word)
