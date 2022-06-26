from game.jumper import Jumper
from game.words import word_list
from game.terminal import Terminal


class Director:

    def __init__(self):
        self.continue_playing = True
        self.terminal = Terminal()
        self.jumper = Jumper()
        self.words = word_list

    def start_game(self):
        while self.continue_playing:
            self.get_inputs()
            self.get_updates()

    def get_inputs(self):
        self.words

    def get_updates(self):
        self.jumper.play_game()

