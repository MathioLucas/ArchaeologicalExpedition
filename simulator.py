
import random
import time

class Expedition:
    def __init__(self, era, location, budget):
        self.era = era
        self.location = location
        self.budget = budget
        self.team = []
        self.equipment = []
        self.supplies = 100  
        self.time_remaining = 100  
        self.artifacts = []
        self.reputation = 0
    def allocate_budget(self):
        print(f"\nYour total budget is ${self.budget}. Allocate your funds wisely.")
        team_budget = int(input("Enter amount to spend on hiring your team: $"))
        equipment_budget = int(input("Enter amount to spend on equipment: $"))
        supplies_budget = int(input("Enter amount to spend on supplies: $"))
        misc_budget = self.budget - (team_budget + equipment_budget + supplies_budget)
        print(f"Remaining budget for unforeseen expenses: ${misc_budget}")
        self.hire_team(team_budget)
        self.buy_equipment(equipment_budget)
        self.purchase_supplies(supplies_budget)
    def hire_team(self, budget):
        roles = ['Historian', 'Archaeologist', 'Digger', 'Conservator', 'Guide']
        costs = {'Historian': 5000, 'Archaeologist': 7000, 'Digger': 3000, 'Conservator': 6000, 'Guide': 4000}
        print("\nAvailable team members to hire:")
        for role in roles:
            print(f"{role} - ${costs[role]}")
while budget >= min(costs.values()):
            choice = input("\nEnter the role you want to hire (or 'done' to finish hiring): ")
            if choice in roles:
                if budget >= costs[choice]:
                    self.team.append(choice)
                    budget -= costs[choice]
                    print(f"Hired a {choice}. Remaining budget for team: ${budget}")
                else:
                    print("Insufficient budget for this team member.")
            elif choice.lower() == 'done':
                break
            else:
                print("Invalid choice. Please select from the available roles.")
def buy_equipment(self, budget):
        equipment_list = {'Shovel': 100, 'Brush': 50, 'Screen': 150, 'Camera': 500, 'GPS': 1000}
        print("\nAvailable equipment to buy:")
        for item, cost in equipment_list.items():
            print(f"{item} - ${cost}")

        while budget >= min(equipment_list.values()):
            choice = input("\nEnter the equipment you want to buy (or 'done' to finish purchasing): ")
            if choice in equipment_list:
                if budget >= equipment_list[choice]:
                    self.equipment.append(choice)
                    budget -= equipment_list[choice]
                    print(f"Purchased {choice}. Remaining budget for equipment: ${budget}")
                else:
                    print("Insufficient budget for this equipment.")
            elif choice.lower() == 'done':
                break
            else:
                print("Invalid choice. Please select from the available equipment.")

    def purchase_supplies(self, budget):
        print(f"\nPurchased supplies worth ${budget}. Supplies level is now at {self.supplies}%.")

    def start_expedition(self):
        print("\nStarting your archaeological expedition...")
        for day in range(1, int(self.time_remaining)+1):
            print(f"\nDay {day}:")
            event = random.choice(['good_weather', 'bad_weather', 'find_artifact', 'equipment_failure', 'team_conflict', 'nothing'])
            if event == 'good_weather':
                print("The weather is perfect for digging.")
            elif event == 'bad_weather':
                print("Bad weather has delayed your progress.")
                self.time_remaining -= 1
                self.supplies -= 5
            elif event == 'find_artifact':
                artifact = self.discover_artifact()
                self.artifacts.append(artifact)
                print(f"You have discovered: {artifact}!")
                self.reputation += 10
            elif event == 'equipment_failure':
                if self.equipment:
                    broken_equipment = self.equipment.pop()
                    print(f"Your {broken_equipment} has broken down.")
                else:
                    print("An equipment failure occurred, but you have no equipment left!")
            elif event == 'team_conflict':
                print("There is a conflict among your team members.")
                self.handle_team_conflict()
            else:
                print("The day passes without significant events.")
            self.time_remaining -= 1
            self.supplies -= 2
            if self.supplies <= 0:
                print("You have run out of supplies!")
                break
            if self.time_remaining <= 0:
                print("You have run out of time!")
                break
        self.end_expedition()

    

    

        
    

   
