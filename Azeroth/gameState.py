import torch

class GameState():
    def __init__(self):
        self.direction = 0
        self.length = 4
        self.width = 72
        self.height = 72