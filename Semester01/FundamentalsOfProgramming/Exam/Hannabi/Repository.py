import random

class Repository:
    def __init__(self):
        self.population = 100
        self.acres = 1000
        self.grain = 2800
        self.year = 1

    def get_state(self):
        return {
            'population': self.population,
            'acres': self.acres,
            'grain': self.grain,
            'year': self.year
        }

    def update_state(self, population, acres, grain, year):
        self.population = population
        self.acres = acres
        self.grain = grain
        self.year = year
