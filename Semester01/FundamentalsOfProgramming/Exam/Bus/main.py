from Repository import Repository
from Controller import Controller
from UI import UI
import unittest


def run_tests():
    #loading test modules
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    #adding tests
    from testing import TestController
    suite.addTests(loader.loadTestsFromTestCase(TestController))

    #running the tests
    runner = unittest.TextTestRunner()
    runner.run(suite)

repo = Repository()
repo.load_data()
controller = Controller(repo)
ui = UI(controller)
#ui.run()
run_tests()
