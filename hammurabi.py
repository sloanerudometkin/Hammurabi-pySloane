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
        #each year we have to print out summaries:
        starved_last_year = 0
        immigrants_last_year = 5
        harvested_last_year = 3000
        yield_per_acre = 3
        rats_eaten_last_year = 200

        #core game loop
        for year in range(1, 11):
            print(" Welcome to Year {year})")

    #print summary
    def printSummary(self, year, starved, immigrants, population, harvest, yield_per_acre, rats_eaten, acres_owned, land_value, bushels):
        print("\nO great Hammurabi!")
        print(f"You are in year {year} of your ten year rule.")
        print(f"Last year {starved} people starved to death.")
        print(f"Last year {immigrants} people entered the kingdom.")
        print(f"The population is now {population}.")
        print(f"We harvested {harvest} bushels at {yield_per_acre} bushels per acre.")
        print(f"Rats destroyed {rats_eaten} bushels and left {bushels} bushels in storage.")
        print(f"The city owns {acres_owned} acres of land.")
        print(f"Right now, land is worth {land_value} bushels per acre.")
    

    # other methods go here

if __name__ == "__main__":
    hammurabi = Hammurabi()
    hammurabi.main()
       