import os
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Entity_dir = os.path.join(parent_dir, 'Entity')
sys.path.append(Entity_dir)
Boundary_dir = os.path.join(parent_dir, 'Boundary')
sys.path.append(Boundary_dir)

from Favourites import Favourites
from DatabaseCRUDOperator import DatabaseCRUDOperator
from Meal import Meal

class FavouritesController:
    @staticmethod
    def addFavouriteMeal(user_email, meal):
        dbOperator = DatabaseCRUDOperator()
        read_meal = dbOperator.read(Meal, mealId = meal.mealId)
        if not read_meal:
            meal_to_create = Meal(meal.mealId, meal.mealName, meal.calories, meal.carbs, meal.proteins, meal.fats, meal.ingredients, meal.recipeInstructions, meal.img_url)
            dbOperator.create(meal_to_create)
        favouriteEntry = Favourites(user_email, meal.mealId)
        dbOperator.create(favouriteEntry)
    def deleteFavouriteMeal(user_email, meal_id):
        dbOperator = DatabaseCRUDOperator()
        primary_key_dict = {
            "user_email": user_email,
            "meal_id": meal_id
        }
        dbOperator.delete(Favourites, primary_key_dict)
    def getFavouriteMeals(user_email):
        dbOperator = DatabaseCRUDOperator()
        favouriteList = dbOperator.read(Favourites, user_email = user_email)
        mealList = []
        for favourite in favouriteList:
            meal = dbOperator.read(Meal, mealId = favourite.meal_id)[0]
            mealList.append(meal)
        return mealList