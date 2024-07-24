import os
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Boundary_dir = os.path.join(parent_dir, 'Boundary')
sys.path.append(Boundary_dir)

from NutritionAPIHandler import NutritionAPIHandler

class MealBrowser:
    @staticmethod
    def searchResults(filters, number = 10):
        filters["number"] = number
        nutritionAPIHandler = NutritionAPIHandler()
        return nutritionAPIHandler.GETMeals(filters)