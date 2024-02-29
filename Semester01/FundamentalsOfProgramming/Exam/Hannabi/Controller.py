from Repository import Repository
import random

class Controller:
    def __init__(self, repo):
        self.repo = repo
        self.land_price = random.randint(15, 25)
        self.harvest = 0
        self.rats_ate = 0
        self.starved = 0
        self.immigrants = 0
        self.harvested_grain = 0
        self.starved = 0
        self.illegal_immigrants = 0

    def buy_sell_land(self, acres_to_buy_sell):
        """
        Precondition: acres_to_buy_sell can be positive (buying land) or negative (selling land).
        Postcondition: Adjusts acres and grain in the state based on the transaction.
        Exception: Raises an exception if trying to buy more land than grain can afford or sell more land than owned 
        """
        
        state = self.repo.get_state()
        if acres_to_buy_sell > 0 and state['grain'] < acres_to_buy_sell * self.land_price:
            raise Exception("Not enough grain to buy land.")
        if acres_to_buy_sell < 0 and abs(acres_to_buy_sell) > state['acres']:
            raise Exception("You cannot sell more land than you own.")
        state['acres'] += acres_to_buy_sell
        state['grain'] -= acres_to_buy_sell * self.land_price
        self.repo.update_state(**state)

    def feed_population(self, units_to_feed):
        """
        Precondition: units_to_feed must be a non-negative integer.
        Postcondition: Deducts units_to_feed from grain, calculates starved population, may adjust population based on starvation or add illegal_immigrants if no one starved.
        Exception: Raises an exception if units_to_feed exceeds available grain or if more than half the population starves (game over condition). 
        """
        
        state = self.repo.get_state()
        if units_to_feed > state['grain']:
            raise Exception("Not enough grain to feed the population.")
        state['grain'] -= units_to_feed
        self.starved = state['population'] - (units_to_feed // 20)
        if self.starved > 0:
            state['population'] -= self.starved
            if self.starved >= (state['population'] // 2):
                raise Exception("Game over: Too many people starved.")
        else:
            self.illegal_immigrants = random.randint(0, 10)
            state['population'] += self.illegal_immigrants
        self.repo.update_state(**state)

    def plant_grain(self, acres_to_plant):
        """
        Precondition: acres_to_plant must be a non-negative integer.
        Postcondition: Calculates the harvest based on random yield and adjusts grain.
        Exception: Raises an exception if attempting to plant more acres than owned, more than the population can support, or using more grain than available. 
        """
        state = self.repo.get_state()
        self.harvest = random.randint(1, 6)
        harvested_grain = self.harvest * acres_to_plant
        state['grain'] += harvested_grain
        self.repo.update_state(**state)
        #Store the amount of grain harvested for reporting
        self.harvested_grain = harvested_grain
        
        if acres_to_plant > state['acres']:
            raise Exception("You cannot plant more acres than you own.")
        if acres_to_plant > state['population'] * 10:
            raise Exception("You don’t have enough people to plant that many acres.")
        if acres_to_plant > state['grain']:
            raise Exception("You don’t have enough grain to plant that many acres.")
        self.harvest = random.randint(1, 6)
        state['grain'] += self.harvest * acres_to_plant
        self.repo.update_state(**state)

    def get_harvested_grain(self):
        #Return the amount of grain harvested
        return self.harvested_grain
    
    def check_for_rats(self):
        state = self.repo.get_state()
        if random.random() < 0.2:  # 20% chance of rats
            self.rats_ate = int(state['grain'] * 0.1)  # Rats eat 10% of grain
            state['grain'] -= self.rats_ate
        self.repo.update_state(**state)

    def manage_year(self, acres_to_buy_sell, units_to_feed, acres_to_plant):
        """
        Orchestrates the year's operations by calling the other methods in order: 
        buy_sell_land, feed_population, plant_grain, check_for_rats, and end_of_year 
        """
        
        self.buy_sell_land(acres_to_buy_sell)
        self.feed_population(units_to_feed)
        self.plant_grain(acres_to_plant)
        self.check_for_rats()
        self.end_of_year()

    def end_of_year(self):
        """
        Postcondition: Increments the year, updates the land price for the next year. 
        """
        
        state = self.repo.get_state()
        state['year'] += 1
        self.land_price = random.randint(15, 25)  #Update land price for next year
        self.repo.update_state(**state)

    def is_game_over(self):
        """
        Return: True if the game-ending condition is met (more than half the population starved), otherwise False. 
        """
        
        return self.starved >= (self.repo.get_state()['population'] // 2)

    def get_land_price(self):
        return self.land_price

    def get_harvest(self):
        return self.harvest

    def get_rats_ate(self):
        return self.rats_ate

    def get_starved(self):
        return self.starved

    def get_illegal_immigrants(self):
        return self.illegal_immigrants