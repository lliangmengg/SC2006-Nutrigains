from sqlalchemy import Column, Date, DECIMAL, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from User import User

Base = declarative_base()

class NutritionHistory(Base):
    __tablename__ = 'NutritionHistory'
    user_email = Column(String(255), ForeignKey(User.email), primary_key=True)
    date = Column(Date, primary_key=True)
    calories = Column(DECIMAL(10, 2))
    carbs = Column(DECIMAL(10, 2))
    proteins = Column(DECIMAL(10, 2))
    fats = Column(DECIMAL(10, 2))

    def __init__(self, user_email, date, calories, carbs, proteins, fats):
        self.user_email = user_email
        self.date = date
        self.calories = calories
        self.carbs = carbs
        self.proteins = proteins
        self.fats = fats
