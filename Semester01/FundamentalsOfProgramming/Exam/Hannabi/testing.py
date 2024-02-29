import unittest
from Repository import Repository
from Controller import Controller

class TestControllerMethods(unittest.TestCase):
    def setUp(self):
        self.repo = Repository() 
        self.controller = Controller(self.repo)

    def test_feed_population_sufficient_grain(self):
        #Test feeding the population with sufficient grain
        initial_state = self.repo.get_state()
        units_to_feed = initial_state['grain'] // 2  #Use half of available grain
        self.controller.feed_population(units_to_feed)
        updated_state = self.repo.get_state()
        self.assertTrue(updated_state['grain'] == initial_state['grain'] - units_to_feed)
        self.assertTrue(self.controller.get_starved() == 0)

    def test_feed_population_insufficient_grain(self):
        #Test feeding the population with more grain than available should raise Exception
        initial_state = self.repo.get_state()
        units_to_feed = initial_state['grain'] + 1  #Use more grain than available
        with self.assertRaises(Exception):
            self.controller.feed_population(units_to_feed)



def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestControllerMethods)
    unittest.TextTestRunner().run(suite)
