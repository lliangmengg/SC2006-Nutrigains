# SC2006-Nutrigains
This repository is a copy of the NTU SC2006 Software Engineering Group Project: Nutrigains.

## Introduction
Nutrigains is an innovative meal recommendation and nutrition management web application. It integrates external recipe databases and APIs like Spoonacular and Gemini to offer diverse meal options and accurate nutritional insights. Nutrigains empowers users with a comprehensive set of features, including chatbot-assisted meal recommendations, nutrition tracking and user account management.

## How to Run the Project
1. **Run the Client Server:**
   ```bash
   cd client
   npm i
   npm start
   
2. **Database Setup**
   - create a new database on MySql workbench
   - In DatabaseCRUDOperator.py, locate the following line:
     ```python
     self.db_url = "mysql+pymysql://<username>:<password>@localhost:3306/nutrigains"
   - Replace <username> with your MySQL username and <password> with your MySQL password.
   
3. **Run the Backend Server:**
   ```bash
   cd server
   python server.py

## Project Structure
```
└── 📁Nutrigains
    └── 📁front_end
        └── 📁public
        └── 📁src
            └── 📁Pages
                └── 📁Browse
                    └── Browse.css
                    └── Browse.js
                └── 📁chatbot
                    └── chatbot.css
                    └── chatbot.js
                └── 📁favourites
                    └── favourites.css
                    └── favourites.js
                └── 📁ForgotPassword
                    └── ForgotPassword.css
                    └── ForgotPassword.js
                └── 📁History
                    └── History.css
                    └── History.js
                └── 📁Home
                    └── home.css
                    └── home.js
                └── 📁Login
                    └── login.css
                    └── login.js
                └── 📁MealCard
                    └── MealCard.css
                    └── MealCard.js
                └── 📁MealInfo
                    └── MealInfo.css
                    └── MealInfo.js
                └── 📁NavBar
                    └── navBar.css
                    └── navBar.js
                └── 📁NutritionTracking
                    └── nutritionTracking.css
                    └── nutritionTracking.js
                └── 📁Profile
                    └── Profile.css
                    └── Profile.js
                └── 📁Signup
                    └── signup.css
                    └── signup.js
            └── App.css
            └── App.js
            └── App.test.js
            └── index.css
            └── index.js
            └── logo.png
            └── logo.svg
            └── reportWebVitals.js
            └── setupTests.js
            └── User.js
        └── .gitignore
        └── package-lock.json
        └── package.json
        └── README.md
    └── 📁server
        └── 📁Boundary
            └── 📁__pycache__
            └── DatabaseCRUDOperator.py
            └── GAIHandler.py
            └── NutritionAPIHandler.py
            └── testing.dart
        └── 📁Control
            └── 📁__pycache__
            └── Chatbot.py
            └── FavouritesController.py
            └── FitnessCalculator.py
            └── LoginHandler.py
            └── MealBrowser.py
            └── MealTrackingController.py
            └── OTPHandler.py
            └── ProfileHandler.py
            └── SignupHandler.py
        └── 📁Entity
            └── 📁__pycache__
            └── Favourites.py
            └── Meal.py
            └── MealHistory.py
            └── NutritionHistory.py
            └── Otp.py
            └── User.py
        └── .gitignore
        └── README.md
        └── server.py
    └── database_backup.sql
    └── package-lock.json
    └── package.json
```
## Language & Tools

### Frontend Development:
- ![React](https://img.icons8.com/color/48/000000/react-native.png) **React**
- ![HTML](https://img.icons8.com/color/48/000000/html-5.png) **HTML**
- ![CSS](https://img.icons8.com/color/48/000000/css3.png) **CSS**

### Backend Development:
- ![Python](https://img.icons8.com/color/48/000000/python.png) **Python**
- ![Flask](https://img.icons8.com/color/48/000000/flask.png) **Flask**

### Database:
- ![MySQL](https://img.icons8.com/color/48/000000/mysql-logo.png) **MySQL**
- ![SQLAlchemy](https://img.icons8.com/color/48/000000/sql.png) **SQLAlchemy**

## Limitations
- **Demo Purpose:** The project serves primarily as a learning tool and may not be production-ready.

