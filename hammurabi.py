import random

class Hammurabi:
    def __init__(self):
        self.rand = random.Random()

    def main(self):
        self.playGame()

    def playGame(self):
        # declare local variables here: grain, population, etc.
        # statements go after the declarations
        #define the starting game state
        population = 100
        bushels = 2800
        acres_owned = 1000
        land_value = 19

    # other methods go here

if __name__ == "__main__":
    hammurabi = Hammurabi()
    hammurabi.main()
       