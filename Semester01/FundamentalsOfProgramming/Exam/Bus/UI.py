class UI:
    def __init__(self, controller):
        self.controller = controller

    def display_buses_for_route(self):
        route_code = input("Enter route code: ")
        buses = self.controller.get_buses_for_route(route_code)
        if buses:
            print(f"Buses on route {route_code}:")
            for bus in buses:
                print(f"Bus ID: {bus[0]}, Model: {bus[1]}, Times Used: {bus[2]}")
        else:
            print("No buses found for this route.")

    def increase_usage(self):
        bus_id = input("Enter bus ID: ")
        route_code = input("Enter route code: ")
        message = self.controller.increase_bus_usage(bus_id, route_code)
        print(message)

    def display_buses_by_kilometers(self):
        pass

    
    def run(self):
        while True:
            print("\n1. Display buses for a route")
            print("2. Increase bus usage")
            print("3. Display all buses by kilometers traveled")
            print("4. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.display_buses_for_route()
            elif choice == '2':
                self.increase_usage()
            elif choice == '3':
                self.display_buses_by_kilometers()
            elif choice == '4':
                break
            else:
                print("Invalid option.")
