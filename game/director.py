from game.jumper import _Jumper
from game.terminal import Terminal
from game.words import word_list

class Director:

    def __init__(self):
        self.continue_playing = True
        self.terminal = Terminal()
        self.jumper = _Jumper()
        self.words = word_list

    def _start_game(self):
        while self.continue_playing:
            self.get_inputs()
            self.get_updates()

    def get_inputs(self):
        self.words

    def get_updates(self):
        self.jumper._play_game()

