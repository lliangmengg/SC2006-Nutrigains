from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Meal(Base):
    __tablename__ = 'Meals'
    mealId = Column(Integer, primary_key=True)
    mealName = Column(String)
    calories = Column(Float)
    carbs = Column(Float)
    proteins = Column(Float)
    fats = Column(Float)
    ingredients = Column(Text)
    recipeInstructions = Column(Text)
    img_url = Column(String)

    def __init__(self, mealID, mealName, calories, carbs, proteins, fats, ingredients, recipeInstructions, img_url):
        self.mealId = mealID
        self.mealName = mealName
        self.calories = calories
        self.carbs = carbs
        self.proteins = proteins
        self.fats = fats
        self.ingredients = ingredients
        self.recipeInstructions = recipeInstructions
        self.img_url = img_url
    
    def jsonify(self):
        mealDict = {}
        mealDict["mealId"] = self.mealId
        mealDict["mealName"] = self.mealName
        mealDict["calories"] = self.calories
        mealDict["carbs"] = self.carbs
        mealDict["proteins"] = self.proteins
        mealDict["fats"] = self.fats
        mealDict["ingredients"] = self.ingredients
        mealDict["recipeInstructions"] = self.recipeInstructions
        mealDict["img_url"] = self.img_url
        return mealDict
