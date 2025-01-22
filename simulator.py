
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

    

        
    

   
