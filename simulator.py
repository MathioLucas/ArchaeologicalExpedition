
import random
import time

class Expedition:
    def __init__(self, era, location, budget):
        self.era = era
        self.location = location
        self.budget = budget
        self.team = []
        self.equipment = []
        self.supplies = 100  # Represents percentage
        self.time_remaining = 100  # Represents days
        self.artifacts = []
        self.reputation = 0

   
