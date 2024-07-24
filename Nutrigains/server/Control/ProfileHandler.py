import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Boundary_dir = os.path.join(parent_dir, 'Boundary')
Entity_dir = os.path.join(parent_dir, 'Entity')
sys.path.append(Boundary_dir)
sys.path.append(Entity_dir)

from DatabaseCRUDOperator import DatabaseCRUDOperator
from User import User
from FitnessCalculator import FitnessCalculator
class ProfileHandler:
    @staticmethod
    def updateUser(user_email, kwargs):
        dbOperator = DatabaseCRUDOperator()
        primary_key_dict = {"email": user_email}
        dbOperator.update(User, primary_key_dict, kwargs)
        new_user = dbOperator.read(User, email = user_email)[0]
        fitnessCalculator = FitnessCalculator(new_user)
        new_kwargs = fitnessCalculator.calculate_goal_attributes()
        dbOperator.update(User, primary_key_dict, new_kwargs)
    @staticmethod
    def getProfile(user_email):
        dbOperator = DatabaseCRUDOperator()
        user = dbOperator.read(User, email = user_email)[0]
        return {
            "email": user.email,
            "fullName": user.full_name,
            "dob": user.dob.strftime("%Y-%m-%d"),
            "height": user.height,
            "weight": user.weight,
            "goal": user.goal,
            "gender": user.gender,
            "activity_level": user.activity_level
        }
