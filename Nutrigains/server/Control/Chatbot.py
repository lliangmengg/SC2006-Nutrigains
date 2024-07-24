import sys
import os
import json
from datetime import datetime

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Boundary_dir = os.path.join(parent_dir, 'Boundary')
sys.path.append(Boundary_dir)
Entity_dir = os.path.join(parent_dir, 'Entity')
sys.path.append(Entity_dir)

from GAIHandler import GAIHandler
from MealBrowser import MealBrowser
class Chatbot:
    def __init__(self, history):
        self.history = history
    def extractFilters(self, message):
        gaiHandler = GAIHandler([])
        print(self.history, file = sys.stdout)
        context = ""
        context += """
            historical context between user and app: 
"""
        context += json.dumps(self.history)
        context += "\nThis is a query made by a user in an app: "+ message
        API_context = """
                This API is designed for searching recipes based on various parameters. The available parameters and their descriptions are as follows:

                - `query` (string): The meal that the user has requested (e.g., "pasta").
                - `cuisine` (string): The cuisine(s) of the recipes. One or more, comma-separated (interpreted as 'OR'). Supported cuisines include African, Asian, American, British, Cajun, Caribbean, Chinese, Eastern European, European, French, German, Greek, Indian, Irish, Italian, Japanese, Jewish, Korean, Latin American, Mediterranean, Mexican, Middle Eastern, Nordic, Southern, Spanish, Thai, and Vietnamese.
                - `excludeCuisine` (string): The cuisine(s) the recipes must not match. One or more, comma-separated (interpreted as 'AND').
                - `diet` (string): The diet(s) for which the recipes must be suitable. Multiple diets can be specified with a comma for 'AND' connection or a pipe '|' for 'OR' connection. Supported diets include Gluten Free, Ketogenic, Vegetarian, Lacto-Vegetarian, Ovo-Vegetarian, Vegan, Pescetarian, Paleo, Primal, Low FODMAP, and Whole30.
                - `intolerances` (string): A comma-separated list of intolerances. Supported intolerances include Dairy, Egg, Gluten, Grain, Peanut, Seafood, Sesame, Shellfish, Soy, Sulfite, Tree Nut, and Wheat.
                - `equipment` (string): The equipment required, multiple values interpreted as 'or'.
                - `includeIngredients` (string): A comma-separated list of ingredients that should/must be used in the recipes.
                - `excludeIngredients` (string): A comma-separated list of ingredients or ingredient types that the recipes must not contain.
                - `type` (string): The type of recipe. Supported types include main course, side dish, dessert, appetizer, salad, bread, breakfast, soup, beverage, sauce, marinade, fingerfood, snack, and drink.
                - `titleMatch` (string): Text that must be found in the title of the recipes.
                - `maxReadyTime` (integer): The maximum time in minutes it should take to prepare and cook the recipe.
                - minCarbs`, `maxCarbs`, `minProtein`, `maxProtein`, `minCalories`, `maxCalories`, `minFat`, `maxFat` (integer)
                - `offset` (integer): The number of results to skip (between 0 and 900).
                - `number` (integer): The number of expected results (between 1 and 100).

                When querying this API, users can specify any combination of these parameters to filter and find recipes that match their preferences and dietary requirements.
                """
        context += API_context
        context += """
            based on the parameters about the API and based on the user query, output a python dictionary which contains key value pairs corresponding to the API filters. (also remember to see the context of this chat to extract more filters if needed)
        """
        context += """
            I want your output to just be a single line and no spaces. Just in this form { ....(your key-value pairs go here).... }.
        """
        response = gaiHandler.getResponse(context)
        API_filters = json.loads(response)
        return API_filters
    def retrieveMeals(self, filters):
        meals =  MealBrowser.searchResults(filters, 5)
        return meals
    def isMealRecommendationsRequired(self, message):
        gaiHandler = GAIHandler(self.history)
        context = """
            From this user query determine if the user is asking for meal recommendations from our app or not. Say 1 if yes or 0 otherwise.
        """
        context += "User query: "+message
        response = gaiHandler.getResponse(context)
        if response == "1": return True
        else: return False
    def isRelated(self, message):
        gaiHandler = GAIHandler([])
        context = """
            This is a user query to a nutrition app that provides meal recommendations to users and other nutrition suggestions via a chatbot. Determine if this user query is relevant to the app or not. Say 1 if yes or 0 if no.
        """
        context += "User query: " + message
        response = gaiHandler.getResponse(context)
        if response == "1": return True
        else: return False
    def mainChatbotLogic(self, message):
        gaiHandler = GAIHandler(self.history)
        TextResponse = None
        MealResponse = None
        # find if the query is relevant or not
        if not self.isRelated(message):
            TextResponse = "This query is not relavant"
        else:
        # find if the user requires meal suggestions or not
            if self.isMealRecommendationsRequired(message):
        # if yes, then generate the initial text based on that history
                extractedFilters = self.extractFilters(message)
                MealResponse = self.retrieveMeals(extractedFilters)
                # generate initial text:
                TextResponse = "These are your recommended meals:"
        # if no, then generate response as usual 
            else:
                context = """
                    provide the answer to this user query in a paragraph format, with no headers or bold, and propper indentation: 
                """
                context += message
                TextResponse = gaiHandler.getResponse(context)
        responseDict = {}
        if MealResponse != None:
            MealResponseJson = [meal.jsonify() for meal in MealResponse]
        else:
            MealResponseJson = []
        responseDict["TextResponse"] = TextResponse
        responseDict["MealResponse"] = MealResponseJson
        responseDict["hiddenTextResponse"] = extractedFilters if MealResponseJson else None
        return responseDict
    
