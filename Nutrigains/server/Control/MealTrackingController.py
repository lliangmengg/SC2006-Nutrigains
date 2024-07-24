from datetime import datetime, timedelta, date
from collections import defaultdict
import sys
import os
from decimal import Decimal

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Boundary_dir = os.path.join(parent_dir, 'Boundary')
Entity_dir = os.path.join(parent_dir, "Entity")
sys.path.append(Boundary_dir)
sys.path.append(Entity_dir)

from DatabaseCRUDOperator import DatabaseCRUDOperator
from MealHistory import MealHistory
from NutritionHistory import NutritionHistory
from Meal import Meal
from User import User


class MealTrackingController:
    @staticmethod
    def addMealToTracking(user_email, meal):
        dbOperator = DatabaseCRUDOperator()
        # add to meals
        try:
            meal_to_create = Meal(meal.mealId, meal.mealName, meal.calories, meal.carbs, meal.proteins, meal.fats, meal.ingredients, meal.recipeInstructions, meal.img_url)
            dbOperator.create(meal_to_create)
        except:
            pass
        # add to meal history
        mealHistoryEntry = MealHistory(user_email, datetime.now(), meal.mealId)
        dbOperator.create(mealHistoryEntry)
        # update nutrition history
        # check if today's values exist
        nutritionHistoryEntry = dbOperator.read(NutritionHistory, user_email=user_email, date=date.today())
        if nutritionHistoryEntry:
            nutritionHistoryEntry = nutritionHistoryEntry[0]
            # update its values
            nutritionHistoryEntry.calories += Decimal(meal.calories)
            nutritionHistoryEntry.carbs += Decimal(meal.carbs)
            nutritionHistoryEntry.fats += Decimal(meal.fats)
            nutritionHistoryEntry.proteins += Decimal(meal.proteins)
            primary_key_dict = {
                "user_email": user_email,
                "date": nutritionHistoryEntry.date
            }
            nutrition_dict = {
                "calories": nutritionHistoryEntry.calories,
                "carbs": nutritionHistoryEntry.carbs,
                "proteins": nutritionHistoryEntry.proteins,
                "fats": nutritionHistoryEntry.fats
            }
            dbOperator.update(NutritionHistory, primary_key_dict, nutrition_dict)
        else:
            # create a row
            nutritionHistoryEntry = NutritionHistory(user_email, date.today(), Decimal(meal.calories), Decimal(meal.carbs), Decimal(meal.proteins), Decimal(meal.fats))
            dbOperator.create(nutritionHistoryEntry)

    @staticmethod 
    # you can only delete from the current day
    def deleteMealFromTracking(user_email, meal, meal_date_time):
        dbOperator = DatabaseCRUDOperator()
        # delete from nutrition History
        nutritionHistoryEntry = dbOperator.read(NutritionHistory, user_email = user_email, date = date.today())[0]
        nutritionHistoryEntry.calories -= Decimal(meal.calories)
        nutritionHistoryEntry.carbs -= Decimal(meal.carbs)
        nutritionHistoryEntry.fats -= Decimal(meal.fats)
        nutritionHistoryEntry.proteins -= Decimal(meal.proteins)
        primary_key_dict = {
            "user_email": user_email,
            "date": nutritionHistoryEntry.date
        }
        nutrition_dict = {
            "calories": nutritionHistoryEntry.calories,
            "carbs": nutritionHistoryEntry.carbs,
            "proteins": nutritionHistoryEntry.proteins,
            "fats": nutritionHistoryEntry.fats
        }

        dbOperator.update(NutritionHistory, primary_key_dict, nutrition_dict)
        # delete from meal tracking
        dbOperator.delete(MealHistory, {"user_email": user_email, "date_time": meal_date_time})
    @staticmethod
    def getMonthlyHistory(user_email):
        db_operator = DatabaseCRUDOperator()
        thirty_days_ago = datetime.now() - timedelta(days=30)
        mealHistoryEntries =  db_operator.read(MealHistory, user_email=user_email, date_time={'ge': thirty_days_ago})
        mealTimeMappings = {}
        for entry in mealHistoryEntries:
            mealId = entry.meal_id
            meal = db_operator.read(Meal, mealId = mealId)[0]
            date = entry.date_time.strftime("%Y-%m-%d")
            if date in mealTimeMappings:
                mealTimeMappings[date].append(meal.jsonify())
            else:
                mealTimeMappings[date] = [meal.jsonify()]
        return mealTimeMappings
            

    @staticmethod
    def getCurrentDayNutritionData(user_email):
        db_operator = DatabaseCRUDOperator()
        # get nutrition history of today
        calories = 0
        carbs = 0
        protein = 0
        fats = 0
        nutritionHistoryEntry = db_operator.read(NutritionHistory, date = date.today(), user_email = user_email)
        if nutritionHistoryEntry:
            nutritionHistoryEntry = nutritionHistoryEntry[0]
            calories = float(nutritionHistoryEntry.calories)
            carbs = float(nutritionHistoryEntry.carbs)
            protein = float(nutritionHistoryEntry.proteins)
            fats = float(nutritionHistoryEntry.fats)
        return {
            "calories": calories,
            "carbs": carbs,
            "protein": protein,
            "fats": fats
        }
    
    @staticmethod
    def getMonthlyNutritionData(user_email):
        db_operator = DatabaseCRUDOperator()
        start_date = date.today() - timedelta(days=30)

        # Get all nutrition history entries for the past 30 days
        nutrition_history_entries = db_operator.read(
            NutritionHistory,
            user_email=user_email,
            date={"ge": start_date}
        )

        # Create a dictionary to store the monthly nutrition data
        monthly_nutrition_data = {}

        # Populate the dictionary with data from the database
        for entry in nutrition_history_entries:
            # Assuming each entry has a 'date' attribute and nutrition details
            entry_date = entry.date.strftime('%Y-%m-%d')  # Format date as string if needed
            monthly_nutrition_data[entry_date] = {
                "calories": entry.calories,
                "carbs": entry.carbs,
                "protein": entry.proteins,
                "fats": entry.fats
            }

        return monthly_nutrition_data
    @staticmethod
    def getCurrentDayMeals(user_email):
        dbOperator = DatabaseCRUDOperator()
        today_start = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

        currentDayMealHistory =  dbOperator.read(MealHistory, user_email=user_email, 
                                date_time={'ge': today_start})

        MealList = []
        for entry in currentDayMealHistory:
            mealId = entry.meal_id
            meal = dbOperator.read(Meal, mealId = mealId)[0]
            date_time = entry.date_time.strftime('%Y-%m-%d %H:%M:%S')
            MealList.append({
                "meal" : meal.jsonify(),
                "date_time": date_time
            })
        return MealList
    @staticmethod
    def getGoalAttributes(user_email):
        dbOperator = DatabaseCRUDOperator()
        user = dbOperator.read(User, email = user_email)[0]
        return {
            "cals": float(user.cals),
            "protein": float(user.protein),
            "carbs": float(user.carbs),
            "fats": float(user.fats)
        }