import random

class RandomAgent:
    def __init__(self):
        self.actions = ['w', 's', 'a', 'd'] 

    def select_action(self):
        return random.choice(self.actions)