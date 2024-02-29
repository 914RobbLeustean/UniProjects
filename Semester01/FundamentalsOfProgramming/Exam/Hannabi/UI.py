import random
from Controller import Controller
from Repository import Repository
from testing import run_tests

class UI:
    def __init__(self, controller):
        self.controller = controller

    def display_menu(self):
        print("1. Play Game")
        print("2. Run Tests")
        print("3. Exit")
    
    def display_status(self):
        state = self.controller.repo.get_state()
        year = state['year']
        starved = self.controller.get_starved()
        illegal_immigrants = self.controller.get_illegal_immigrants()
        population = state['population']
        acres = state['acres']
        grain = state['grain']
        land_price = self.controller.get_land_price()
        harvest = self.controller.get_harvested_grain()
        rats_ate = self.controller.get_rats_ate()
            
        print(f"\nYear {year} report:")
        print(f"- {starved} people starved.")
        print(f"- {illegal_immigrants} people came to the city.")
        print(f"- Population: {population}")
        print(f"- City owns {acres} acres of land.")
        print(f"- Harvest was {harvest // acres if acres > 0 else 0} units per acre.")
        print(f"- Rats ate {rats_ate} units.")
        print(f"- Land price is {land_price} units per acre.")
        print(f"- Grain stocks: {grain} units.")


    def ask_for_decision(self):
        print("\nDecide your policy for the year:")
        acres_to_buy_sell = int(input("Acres to buy/sell (+/-): "))
        units_to_feed_population = int(input("Units to feed the population: "))
        acres_to_plant = int(input("Acres to plant with grain: "))
        return acres_to_buy_sell, units_to_feed_population, acres_to_plant

    def play_game(self):
        try:
            for _ in range(5): 
                self.display_status()
                decision = self.ask_for_decision()
                self.controller.manage_year(*decision)

                if self.controller.is_game_over():
                    print("Half of your population has starved. You have been thrown out of office!")
                    return

            # Final status
            self.display_status()
            if self.controller.repo.get_state()['population'] > 100 and self.controller.repo.get_state()['acres'] > 1000:
                print("Congratulations, mighty Hammurabi! You have led your people to prosperity!")
            else:
                print("You have survived, but your leadership has not brought prosperity to Sumeria.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.play_game()
            elif choice == '2':
                run_tests() 
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    repo = Repository()
    controller = Controller(repo)
    ui = UI(controller)
    ui.run()
