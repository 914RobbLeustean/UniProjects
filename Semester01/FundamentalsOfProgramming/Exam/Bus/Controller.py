class Controller:
    def __init__(self, repository):
        self.repository = repository

    def get_buses_for_route(self, route_code):
        """
        Retrieves buses associated with a specific route code 
        from the repository. If the route code exists within the repository's routes data structure, 
        it returns the list of buses for that route. Otherwise, it returns None. 
        """
        
        if route_code in self.repository.routes:
            return self.repository.routes[route_code]["buses"]
        else:
            return None
        
    def increase_bus_usage(self, bus_id, route_code):
        """
        Attempts to increase the usage count for a specific bus on a specified route. 
        It calls the increase_usage method of the repository.
        If the operation is successful (the bus ID and route code are valid),
        it returns a success message. Otherwise, it returns an error message indicating invalid inputs. 
        """
        
        if self.repository.increase_bus_usage(bus_id, route_code):
            return "Bus usage increased successfully."
        else:
            return "Invalid bus ID or route code."

    def get_buses_by_kilometers(self):
        pass