import sys
import os
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
from urllib.parse import unquote
import json

parent_dir = os.path.dirname(os.path.abspath(__file__))
Control_dir = os.path.join(parent_dir, 'Control')
sys.path.append(Control_dir)
Entity_dir = os.path.join(parent_dir, 'Entity')
sys.path.append(Entity_dir)

from LoginHandler import LoginHandler
from MealBrowser import MealBrowser
from SignupHandler import SignupHandler
from User import User
from OTPHandler import Otp_handler
from FavouritesController import FavouritesController
from MealTrackingController import MealTrackingController
from Meal import Meal
from Chatbot import Chatbot
from ProfileHandler import ProfileHandler


app  = Flask(__name__)
CORS(app)

# api routes

#login api routes
@app.route('/login', methods=['GET'])
def login():
    data = request.args.to_dict()
    email = data.get('email')
    password = data.get('password')
    user = LoginHandler.validateAndFetchUser(email, password)
    if user:
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid email or password'}), 401

# browse api routes
@app.route("/browse", methods=['GET'])
def browse():
    data = request.args.to_dict()
    meals = MealBrowser.searchResults(data)
    result = [meal.jsonify() for meal in meals]
    return {"result" : result}

# sign up api routes
@app.route("/signup/isexistingemail", methods=['GET'])
def isExistingUser():
    data = request.args.to_dict()
    user_email = data.get("user_email")
    return str(SignupHandler.isExistingEmail(user_email))

@app.route("/signup/storeuser", methods=['GET'])
def storeUser():
    data = request.args.to_dict()
    user_email = data.get("email")
    full_name = data.get("full_name")
    password = data.get("password")
    dob = datetime.strptime(data.get("dob"), "%Y-%m-%d")
    height = float(data.get("height"))
    weight = float(data.get("weight"))
    goal = data.get("goal")
    gender = data.get("gender")
    activity_level = data.get("activity_level")
    new_user = User(user_email, full_name, password, dob, height, weight, goal, gender, activity_level)
    return str(SignupHandler.storeNewUser(new_user))

# otp verification routes
@app.route("/otpverification/sendotp", methods=['GET'])
def sendOtp():
    data = request.args.to_dict()
    email = data.get("email")
    Otp_handler.email_otp(email)
    return "True"

@app.route("/otpverification/verifyotp", methods=['GET'])
def verifyOtp():
    data = request.args.to_dict()
    otp = int(data.get("otp"))
    email = data.get("email")
    return str(Otp_handler.OTPVerification(email, otp))

# favourites api routes
@app.route("/favourites/getfavourites", methods=['GET'])
def getFavourites():
    data = request.args.to_dict()
    email = data.get("email")
    meals = FavouritesController.getFavouriteMeals(email)
    return {
        "result": [meal.jsonify() for meal in meals]
    }

@app.route("/favourites/addfavourite", methods=['GET'])
def addFavourite():
    data = request.args.to_dict()
    email = data.get("email")
    mealDict = json.loads(data.get("meal"))
    meal = Meal(int(mealDict["mealId"]),mealDict["mealName"], float(mealDict["calories"]), float(mealDict["carbs"]), float(mealDict["proteins"]), float(mealDict["fats"]), mealDict["ingredients"], mealDict["recipeInstructions"], mealDict["img_url"] )
    FavouritesController.addFavouriteMeal(email, meal)
    return "True"

@app.route("/favourites/deletefavourite", methods=['DELETE'])
def deleteFavourite():
    data = request.args.to_dict()
    email = data.get("email")
    meal_id = data.get("meal_id")
    FavouritesController.deleteFavouriteMeal(email, meal_id)
    return "True"

# meal tracking api routes
@app.route("/mealtracking/monthlymealhistory", methods=['GET'])
def monthlyMealHistory():
    data = request.args.to_dict()
    email = unquote(data.get("email"))
    print(email, file = sys.stdout)
    return MealTrackingController.getMonthlyHistory(email)

@app.route("/mealtracking/currentdaymeals", methods=['GET'])
def currentDayMeals():
    data = request.args.to_dict()
    email = data.get("email")
    return {
        "result": MealTrackingController.getCurrentDayMeals(email)
    }

@app.route("/mealtracking/getgoalattributes", methods=['GET'])
def getGoalAttributes():
    data = request.args.to_dict()
    email = data.get("email")
    return MealTrackingController.getGoalAttributes(email)

@app.route("/mealtracking/currentdaynutrition", methods=['GET'])
def currentDayNutritionData():
    data = request.args.to_dict()
    email = data.get("email")
    return MealTrackingController.getCurrentDayNutritionData(email)

@app.route("/mealtracking/monthlynutritiondata", methods=['GET'])
def monthlyNutritionData():
    data = request.args.to_dict()
    email = unquote(data.get("email"))
    return {
        "result": MealTrackingController.getMonthlyNutritionData(email)
    }

@app.route("/mealtracking/addtotracking", methods=['GET'])
def addToTracking():
    data = request.args.to_dict()
    print(data, file = sys.stdout)
    email = data.get("email")
    mealDict = json.loads(data.get("meal"))

    # Extract each attribute from the mealDict
    mealId = mealDict.get("mealId")
    mealName = mealDict.get("mealName")
    calories = mealDict.get("calories")
    carbs = mealDict.get("carbs")
    proteins = mealDict.get("proteins")
    fats = mealDict.get("fats")
    ingredients = mealDict.get("ingredients")
    recipeInstructions = mealDict.get("recipeInstructions")
    img_url = mealDict.get("img_url")

    # Now you can create a Meal instance with these values
    meal = Meal(mealId, mealName, calories, carbs, proteins, fats, ingredients, recipeInstructions, img_url)
    MealTrackingController.addMealToTracking(email, meal)
    return "True"

@app.route("/mealtracking/deletefromtracking", methods=['DELETE'])
def deleteFromTracking():
    data = request.args.to_dict()
    print(data, file = sys.stdout)
    email = data.get("email")
    mealDict = json.loads(data.get("meal"))
    date_time = datetime.strptime(mealDict.get("date_time"), "%Y-%m-%d %H:%M:%S")

    # Extract each attribute from the mealDict
    mealId = mealDict.get("mealId")
    mealName = mealDict.get("mealName")
    calories = mealDict.get("calories")
    carbs = mealDict.get("carbs")
    proteins = mealDict.get("proteins")
    fats = mealDict.get("fats")
    ingredients = mealDict.get("ingredients")
    recipeInstructions = mealDict.get("recipeInstructions")
    img_url = mealDict.get("img_url")

    # Now you can create a Meal instance with these values
    meal = Meal(mealId, mealName, calories, carbs, proteins, fats, ingredients, recipeInstructions, img_url)
    MealTrackingController.deleteMealFromTracking(email, meal, date_time)
    return "True"

# chatbot
@app.route("/chatbot/getresponse", methods=['GET'])
def getChatbotResponse():
    data = request.args.to_dict()
    history = json.loads(data.get("history"))
    print(history, file = sys.stdout)
    message = data.get("message")
    chatbot = Chatbot(history)
    return chatbot.mainChatbotLogic(message)

#profile handler api routes
@app.route("/profilehandler/getprofile", methods=['GET'])
def getProfile():
    data = request.args.to_dict()
    email = data.get("email")
    return ProfileHandler.getProfile(email)

@app.route("/profilehandler/updateprofile", methods = ['GET'])
def updateProfile():
    data = request.args.to_dict()
    print(data, file=sys.stdout) #
    email = data.get("email")
    ProfileHandler.updateUser(email, data)
    return "True"

if __name__ == "__main__":
    app.run(debug = True)


    