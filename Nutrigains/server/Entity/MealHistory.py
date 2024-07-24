from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from User import User
from Meal import Meal

Base = declarative_base()

class MealHistory(Base):
    __tablename__ = 'MealHistory'
    user_email = Column(String, ForeignKey(User.email), primary_key=True)
    date_time = Column(DateTime, primary_key=True)
    meal_id = Column(Integer, ForeignKey(Meal.mealId))

    def __init__(self, user_email, date_time, meal_id):
        self.user_email = user_email
        self.date_time = date_time
        self.meal_id = meal_id