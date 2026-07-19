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
            self.printSummary(year, starved_last_year, immigrants_last_year, population, harvested_last_year, yield_per_acre, rats_eaten_last_year, acres_owned, land_value, bushels)

            # call 1st input method : buy land
            acres_to_buy = self.askHowManyAcresToBuy(land_value, bushels)
            if acres_to_buy == -1:
                print("\nYou have abandoned your kingdom! Shame on you! It will fall into chaos...")
                return
            #then update game state variables
            bushels -= acres_to_buy * land_value
            acres_owned += acres_to_buy

            if acres_to_buy == 0:
                acres_to_sell = self.askHowManyAcresToSell(acres_owned)
                if acres_to_sell == -1:
                    print("\nYou have abonded your kingdom! Shame on you! It will fall into chaos...")

                bushels += acres_to_sell * land_value
                acres_owned -= acres_to_sell

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

    #INPUT METHODS
    def askHowManyAcresToBuy(self, price, bushels):
        while True:
            try:
                user_input = input("O Great Hammurabi, how many acres of land do you want to buy? (or type 'quit' to exit): ").strip().lower()
                if user_input == 'quit':
                    return -1
                acres = int(input("0 Great Hammurabi, how many acres of land do you want to buy?"))
                if acres < 0:
                    print("Oh you jest! You can't buy a negative amount of land!")
                elif acres * price > bushels:
                    print(f"0 Great Hammurabi, you jest! We only have {bushels} bushels left!")
                else:
                    return acres
            except ValueError:
                print("Please enter a valid whole number.")

    def askHowManyAcresToSell(self, acresOwned):
        while True:
            try:
                user_input = input("O Great Hammurabi, how many acres of land do you want to sell? (or type 'quit' to exit): ").strip().lower()
                if user_input == 'quit':
                    return -1
                acres = int(user_input)
                if acres < 0:
                    print("Well... you can't sell a negative amount of land!")
                elif acres > acresOwned:
                    print(f"O Great Hammurabi, you are such a jest! We only own {acresOwned} acres!")
                else:
                    return acres
            except ValueError:
                print("please enter a valid whole number or 'quit'.")
    

    # other methods go here

if __name__ == "__main__":
    hammurabi = Hammurabi()
    hammurabi.main()
       