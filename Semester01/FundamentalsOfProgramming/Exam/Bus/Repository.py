class Repository:
    def __init__(self):
        self.routes = {}
        self.buses = {}

    def load_data(self):
        #Load routes
        with open("buses.txt", "r") as f:
            for line in f:
                bus_id, route_code, model, times_used = line.strip().split(",")
                self.buses[bus_id] = {"route_code": route_code, "model": model, "times_used": int(times_used)}
                if route_code in self.routes:
                    self.routes[route_code]["buses"].append(bus_id)

        #Load buses
        with open("buses.txt", "r") as f:
            for line in f:
                bus_id, route_code, model, times_used = line.strip().split(",")
                if route_code in self.routes:
                    self.routes[route_code]["buses"].append((bus_id, model, times_used))

    def save_buses(self):
        with open("buses.txt", "w") as f:
            for bus_id, details in self.buses.items():
                line = f"{bus_id},{details['route_code']},{details['model']},{details['times_used']}\n"
                f.write(line)

    def increase_usage(self, bus_id, route_code):
        if bus_id in self.buses and self.buses[bus_id]["route_code"] == route_code:
            self.buses[bus_id]["times_used"] += 1
            self.save_buses()  #Save changes after increasing usage
            return True
        return False
    
    def get_buses_by_kilometers(self):
        pass