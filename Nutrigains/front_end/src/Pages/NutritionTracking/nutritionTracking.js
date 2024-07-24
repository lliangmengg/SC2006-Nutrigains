import React, { useState, useEffect } from 'react';
import './nutritionTracking.css';
import axios from "axios";
import MealCard from "../MealCard/MealCard";
import Navbar from '../NavBar/navBar';

function NutritionTracking() {
    const [currentValues, setCurrentValues] = useState({
        Calories: 0,
        Carbohydrates: 0,
        Fats: 0,
        Proteins: 0
    });
    const [goalValues, setGoalValues] = useState({
        Calories: 2000,
        Carbohydrates: 300,
        Fats: 70,
        Proteins: 160
    });

    const [meals, setMeals] = useState([]); 

    useEffect(() => {
        // Fetch goal values
        const fetchGoals = async () => {
            try {
            const response = await axios.get('http://127.0.0.1:5000/mealtracking/getgoalattributes', {
                params: { 'email': sessionStorage.getItem("email") }
            });
            setGoalValues({
                Calories: response.data.cals,
                Carbohydrates: response.data.carbs,
                Fats: response.data.fats,
                Proteins: response.data.protein
            }); // Storing the array of meals directly
            } catch (error) {
            console.error('There was an error data!', error);
            }
        };

        const fetchCurrentDayData = async () => {
            try {
            const response = await axios.get('http://127.0.0.1:5000/mealtracking/currentdaynutrition', {
                params: { 'email': sessionStorage.getItem("email") }
            });
            setCurrentValues({
                Calories: response.data.calories,
                Carbohydrates: response.data.carbs,
                Fats: response.data.fats,
                Proteins: response.data.protein
            }); // Storing the array of meals directly
            } catch (error) {
            console.error('There was an error data!', error);
            }
        };

        const fetchTodaysMeals = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:5000/mealtracking/currentdaymeals', {
                    params: { 'email': sessionStorage.getItem("email") }
                });
                // Store the entire meal object, including meal details and date
                setMeals(response.data.result.map(item => ({ ...item.meal, date_time: item.date_time })));
            } catch (error) {
                console.error('There was an error fetching today\'s meals!', error);
            }
        };
        
        

        fetchGoals();
        fetchCurrentDayData();
        fetchTodaysMeals();
        console.log(meals)
    }, []);
    const calculateWidth = (value, goal) => {
        const ratio = value / goal;
        const basePercentage = 75; // Marker position
        return Math.min(100, basePercentage + (ratio * basePercentage - basePercentage));
    };
    const deleteMeal = async (mealToDelete) => {
        try {
            console.log(meals);
            const response = await axios.delete('http://127.0.0.1:5000/mealtracking/deletefromtracking', {
                params: { 'email': sessionStorage.getItem("email"), 'meal': JSON.stringify(mealToDelete)}
            });
            // Filter out the meal using both ID and date to uniquely identify it
            setMeals(currentMeals => currentMeals.filter(meal => meal.mealId !== mealToDelete.mealId || meal.date_time !== mealToDelete.date_time));
            
            // Subtract the nutritional values from currentValues
            setCurrentValues(current => ({
                Calories: current.Calories - mealToDelete.calories,
                Carbohydrates: current.Carbohydrates - mealToDelete.carbs,
                Fats: current.Fats - mealToDelete.fats,
                Proteins: current.Proteins - mealToDelete.proteins,
            }));
        } catch (error) {
            console.error('Error deleting the meal:', error);
        }
    };
    
    


    return (
        <div>
           <Navbar/>

            <div className="nutrition-tracking">
                <div className="daily-intake">
                    <h2>Current Day Intake</h2>
                    <div className="progress-bars">
                        {Object.entries(currentValues).map(([key, value]) => {
                            const goal = goalValues[key];
                            const progressPercent = calculateWidth(value, goal);
                            return (
                                <div className="progress-bar" key={key}>
                                    <div className="label">{key}</div>
                                    <div className="progress">
                                        <div className="progress-value" style={{ width: `${progressPercent}%` }}></div>
                                        <div className="goal-marker" style={{ left: '75%' }}></div>
                                    </div>
                                    <div className="value">{`${value} / ${goal} ${key === 'Calories' ? 'kcal' : 'g'}`}</div>
                                </div>
                            );
                        })}
                    </div>
                    <div className="todays-meals">
            <h2>Today's Meals</h2>
            {meals.length > 0 ? (
                meals.map((meal, index) => (
                    <div key={index} className="meal-entry">
                        <MealCard meal={meal} />
                        <button onClick={() => deleteMeal(meal)} className="delete-button">
                            Delete
                        </button>
                    </div>
                ))
            ) : (
                <p>No meals for today.</p>
            )}
            </div>
                </div>        
            </div>
        </div>
    );
}

export default NutritionTracking;

