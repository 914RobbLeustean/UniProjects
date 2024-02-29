import unittest
from Controller import Controller

#Mock Repository class for testing
class MockRepository:
    def __init__(self):
        #Initialize mock data
        self.buses = {"1": {"route_code": "1", "times_used": 5}}
        self.routes = {"1": {"length": 100, "buses": ["1"]}}

    def get_buses_for_route(self, route_code):
        #method to get buses for a route
        if route_code in self.routes:
            return self.routes[route_code]["buses"]
        else:
            return None

    def increase_bus_usage(self, bus_id, route_code):
        #method to increase bus usage   
        if bus_id in self.buses and route_code == self.buses[bus_id]["route_code"]:
            self.buses[bus_id]["times_used"] += 1
            return True
        else:
            return False

#Testing module using unittest
class TestController(unittest.TestCase):
    def setUp(self):
        #Setup with a mock repository
        self.repository = MockRepository()
        self.controller = Controller(self.repository)

    def test_get_buses_for_route_valid(self):
        buses = self.controller.get_buses_for_route("1")
        self.assertIsNotNone(buses)  #Check that the result is not None
        self.assertIn("1", buses)  #Check that bus "1" is in the result

    def test_get_buses_for_route_invalid(self):
        buses = self.controller.get_buses_for_route("2")
        self.assertIsNone(buses)  #Route "2" does not exist, expect None

    def test_increase_bus_usage_valid(self):
        message = self.controller.increase_bus_usage("1", "1")
        self.assertEqual("Bus usage increased successfully.", message)

    def test_increase_bus_usage_invalid(self):
        message = self.controller.increase_bus_usage("2", "1")  # Invalid bus ID
        self.assertEqual("Invalid bus ID or route code.", message)
