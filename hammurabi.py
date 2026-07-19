import random

class Hammurabi:
    def __init__(self):
        self.rand = random.Random()

    def main(self):
        self.playGame()

    def playGame(self):
        # INITIAL STATE 
        population = 100
        bushels = 2800
        acres_owned = 1000
        land_value = 19
        
        # to track statistics for summaries
        starved_last_year = 0
        immigrants_last_year = 5
        harvested_last_year = 3000
        yield_per_acre = 3
        rats_eaten_last_year = 200

       