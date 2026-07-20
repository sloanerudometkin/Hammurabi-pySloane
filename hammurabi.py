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
#ask how many acres to buy next
            if acres_to_buy == 0:
                acres_to_sell = self.askHowManyAcresToSell(acres_owned)
                if acres_to_sell == -1:
                    print("\nYou have abonded your kingdom! Shame on you! It will fall into chaos...")
                    return
                bushels += acres_to_sell * land_value
                acres_owned -= acres_to_sell
    #next, ask how much grain to feed: call that method
            bushels_fed = self.askHowMuchGrainToFeedPeople(bushels)
            if bushels_fed == -1:
                print("\nYou have abonded your kingdom! Shame on you! It will fall into chaos...")
                return
            bushels -= bushels_fed

    #next call, the acres to plant method
            acres_planted = self.askHowManyAcresToPlant(acres_owned, population, bushels)
            if acres_planted == -1:
                print("\nYou have abandoned your kingdom! Shame on you! It will fall into chaos...")
                return
            
        #deduct the cost of seed

            bushels -= acres_planted * 2

        #determination (event) methods called in the core game loop
        #1 check for plague
            plague_deaths = self.plagueDeaths(population)
            population -= plague_deaths

            if plague_deaths > 0:
                print(f"\nA terrible plague has struck! {plague_deaths} people have died!")

        #2. starvation

            starved_last_year = self.starvationDeaths(population, bushels_fed)
            population -= starved_last_year




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
    
    def askHowMuchGrainToFeedPeople(self, bushels):
        while True:
            try:
                user_input = input(" O Great Hammurabi, how much grain are you going to feed your people? (or type 'quit' to exit): ").strip().lower()
                if user_input == 'quit':
                    return -1
                
                fed = int(user_input)
                if fed < 0:
                    print("Surely you silly jest! You cannot feed them a negative amouunt of grain!")
                elif fed > bushels:
                    print(f"Poor you... we only have {bushels} bushels in storage!") 
                else:
                    return fed
            except ValueError:
                print("Please enter a valid whole number or 'quit'.")

    def askHowManyAcresToPlant(self, acresOwned, population, bushels):
        while True:
            try:
                user_input = input("O Great Hammurabi, how many acres do you want to plant with grain? (or type 'quit' to exit): ").strip().lower()
                if user_input == 'quit':
                    return -1
                
                planted = int(user_input)
                if planted < 0:
                    print("Oh you jest! You can't plant a negative amount of land!")
                elif planted > acresOwned:
                    print(f"O Not-so-great Hammurabi... we only own {acresOwned} acres!")
                elif planted > population * 10:
                    print(f"Oh silly Hammurabi... our population of {population} can only farm {population * 10} acres!")
                elif planted * 2 > bushels:
                    print("Oh silly Hammurabi, we only have {bushels} bushels of seed left!")
                else:
                    return planted
            except ValueError:
                print("Please enter a valid whole number or 'quit'.")

    #DETERMINATION METHODS
    def plagueDeaths(self, population):
        if self.rand.randint(1, 100) <= 15: #self.rand initialized in __init__ using random
            return population // 2
        return 0
    
    def starvationDeaths(self, population, bushelsFedToPeople)
        #calculate how many people starve based on grain fed and each person needs 20 bushels to survive
        people_fed = bushelsFedToPeople // 20
        if people_fed < population:
            return population - people_fed
        return 0
    

    # other methods go here

if __name__ == "__main__":
    hammurabi = Hammurabi()
    hammurabi.main()
       