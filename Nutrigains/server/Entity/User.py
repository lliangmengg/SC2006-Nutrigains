from sqlalchemy import Column, Integer, String, Date, Float, DECIMAL
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'
    email = Column(String, primary_key=True)
    full_name = Column(String)
    password = Column(String)
    dob = Column(Date)
    height = Column(Float)
    weight = Column(Float)
    goal = Column(String)
    gender = Column(String)
    activity_level = Column(String)
    cals = Column(DECIMAL(10, 2))
    carbs = Column(DECIMAL(10, 2))
    protein = Column(DECIMAL(10, 2))
    fats = Column(DECIMAL(10, 2))


    def __init__(self, email, full_name, password, dob, height, weight, goal, gender, activity_level):
        self.email = email
        self.full_name = full_name
        self.password = password
        self.dob = dob
        self.height = height
        self.weight = weight
        self.activity_level = activity_level
        self.goal = goal
        self.gender = gender