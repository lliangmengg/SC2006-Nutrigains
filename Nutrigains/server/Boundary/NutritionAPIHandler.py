import requests
import os
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Entity_dir = os.path.join(parent_dir, 'Entity')
sys.path.append(Entity_dir)

from Meal import Meal

class NutritionAPIHandler:
    APIKey = "b6a061f149e1487283171ce5de6d2646" 
    complexSeach_url = "https://api.spoonacular.com/recipes/complexSearch"
    ingredientSearch_url = "https://api.spoonacular.com/recipes/"
    def GETMeals(self, params):
        params["apiKey"] = self.APIKey
        params["addRecipeInstructions"] = True
        params["addRecipeNutrition"] = True
        results = requests.get(self.complexSeach_url, params=params).json()
        meal_list = []
        for result in results['results']:
            meal_list.append(self.convertJSONToMeal(result))
        return meal_list

    def convertJSONToMeal(self, mealJson):
        mealId = mealJson['id']
        img_url = mealJson['image']
        mealName = mealJson['title'] 
        nutrients = mealJson['nutrition']['nutrients']
        nutrientCount = 0
        protein = carbs = fats = calories = None
        for nutrient in nutrients:
            if nutrient['name'] == "Calories": 
                calories = nutrient['amount']
                nutrientCount += 1
            elif nutrient['name'] == "Fat":
                fats = nutrient['amount']
                nutrientCount += 1
            elif nutrient['name'] == "Net Carbohydrates":
                carbs = nutrient['amount']
                nutrientCount += 1
            elif nutrient['name'] == "Protein":
                protein = nutrient['amount']
                nutrientCount += 1
            if nutrientCount == 4:
                break
        ingredients = ""
        ingredientsList = mealJson['nutrition']['ingredients']
        for ingredient in ingredientsList:
            ingredients += ingredient['name']+": "+str(ingredient['amount'])+" "+ingredient['unit']+";"
        ingredients = ingredients[:len(ingredients)-1]
        instructions = ""
        steps = mealJson['analyzedInstructions'][0]['steps']
        for step in steps:
            instructions += step['step']+";"
        return Meal(mealId, mealName, calories, carbs, protein, fats, ingredients, instructions, img_url)