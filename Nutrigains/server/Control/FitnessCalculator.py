import sys
import os
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Entity_dir = os.path.join(parent_dir, 'Entity')
sys.path.append(Entity_dir)

from User import User
from datetime import date

# For the calculation weight is in kg and height is in cm, will have to put that in frontend
class FitnessCalculator:
    def __init__(self, user: User):
        self.user = user

    def calculate_age(self):
        today = date.today()
        age = today.year - self.user.dob.year - ((today.month, today.day) < (self.user.dob.month, self.user.dob.day))
        return age

    def calculate_bmr(self):
        age = self.calculate_age()
        if self.user.gender.lower() == 'female':
            bmr = 655 + (9.6 * self.user.weight) + (1.8 * self.user.height) - (4.7 * age)
        else: 
            bmr = 66 + (13.7 * self.user.weight) + (5 * self.user.height) - (6.8 * age)
        return bmr

    def calculate_calories_needed(self):
        bmr = self.calculate_bmr()
        if self.user.activity_level == 'lightly active':
            calories_needed = bmr * 1.375
        elif self.user.activity_level == 'moderately active':
            calories_needed = bmr * 1.55
        elif self.user.activity_level == 'very active':
            calories_needed = bmr * 1.725
        else:
            calories_needed = bmr
        return calories_needed
    
    def calculate_goal_attributes(self):
        cals = self.calculate_calories_needed()
        carbs = cals/8 ##carbs in gram
        protein = cals/20 ##protein in gram
        fats = cals * 0.3 /9 ##fats in gram
        return {
            "cals": cals,
            "carbs": carbs,
            "protein": protein,
            "fats": fats
        }



