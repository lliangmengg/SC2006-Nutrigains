import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import './MealInfo.css'; // Using the same CSS file for styling
import axios from "axios"
import Navbar from '../NavBar/navBar';



function MealInfo() {
    const location = useLocation();
    const { meal } = location.state || {};

    const formatListItems = (itemsString) => {
        return itemsString
            .split(';')
            .map(item => item.trim()) // Trim each item
            .filter(item => item) // Filter out empty strings
            .map((item, index) => <li key={index}>{item}</li>); // Map to list items
    };

    const saveToNutritionTracking = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:5000/mealtracking/addtotracking', { 
                params: { 'email': sessionStorage.getItem('email'), 'meal': JSON.stringify(meal) }
            });
            console.log(response.data);
        } catch (error) {
            console.error('Error saving to nutrition tracking:', error);
        }
    };

    const addToFavourites = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:5000//favourites/addfavourite', { 
                params: { 'email': sessionStorage.getItem('email'), 'meal': JSON.stringify(meal) }
            });
            console.log(response.data);
        } catch (error) {
            console.error('Error adding to favourites:', error);
        }
    };



    return (
        <div className="meal-info-container">
           <Navbar/>
            <main className="meal-card">
                {meal && (
                    <>
                        <img src={meal.img_url} alt={meal.mealName} className="meal-image" />
                        <div className="meal-content">
                            <h2 className="meal-name">{meal.mealName}</h2>
                            <div className="meal-attributes">
                                <p>Calories: <input type="text" value={meal.calories + ' kcal'} readOnly /></p>
                                <p>Carbs: <input type="text" value={meal.carbs + ' g'} readOnly /></p>
                                <p>Fats: <input type="text" value={meal.fats + ' g'} readOnly /></p>
                                <p>Protein: <input type="text" value={meal.proteins + ' g'} readOnly /></p>
                                <p>Ingredients:</p>
                                <ul className="ingredients-list">
                                    {formatListItems(meal.ingredients)}
                                </ul>
                                <p>Instructions:</p>
                                <ol className="instructions-list">
                                    {formatListItems(meal.recipeInstructions)}
                                </ol>
                                {/* Additional attributes like Ingredients and Instructions if available in meal object */}
                            </div>
                            <div className="meal-actions">
                            <button onClick={saveToNutritionTracking} className="meal-action-button">
                    Save to Nutrition Tracking
                </button>
                <button onClick={addToFavourites} className="meal-action-button">
                    Add to Favourites
                </button>
                            </div>
                        </div>
                    </>
                )}
            </main>
        </div>
    );
}

export default MealInfo;
