from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from Meal import Meal
from User import User

Base = declarative_base()

class Favourites(Base):
    __tablename__ = 'Favourites'
    user_email = Column(String(255), ForeignKey(User.email), primary_key=True)
    meal_id = Column(Integer, ForeignKey(Meal.mealId), primary_key=True)

    def __init__(self, user_email, meal_id):
        self.user_email = user_email
        self.meal_id = meal_id
