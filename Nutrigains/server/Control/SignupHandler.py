from flask import Flask, request, jsonify, render_template
import  sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from FitnessCalculator import FitnessCalculator

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Boundary_dir = os.path.join(parent_dir, 'Boundary')
Entity_dir = os.path.join(parent_dir, 'Entity')
sys.path.append(Boundary_dir)
sys.path.append(Entity_dir)

from DatabaseCRUDOperator import DatabaseCRUDOperator
from User import User
app = Flask(__name__)

class SignupHandler:
    db_operator = DatabaseCRUDOperator()
    @staticmethod
    def isExistingEmail(email):
       # Query the User table to check if the email already exists
       existing_user = SignupHandler.db_operator.read(User , email = email)
       if existing_user: return True
       return False
    
    @staticmethod
    def storeNewUser(user):
        user_to_store = User(user.email, user.full_name, user.password, user.dob, user.height, user.weight, user.goal, user.gender, user.activity_level)
        user_to_update = User(user.email, user.full_name, user.password, user.dob, user.height, user.weight, user.goal, user.gender, user.activity_level)
        SignupHandler.db_operator.create(user_to_store)
        fitnessCalculator = FitnessCalculator(user_to_update)
        kwargs = fitnessCalculator.calculate_goal_attributes()
        SignupHandler.db_operator.update(User, {"email": user.email}, kwargs)
        return True