import React from 'react';
import { useNavigate } from 'react-router-dom';
import './MealCard.css'; // Create and import a separate CSS file for the MealCard component

function MealCard({ meal }) {

    const navigate = useNavigate();
    const navigateToMealInfo = () => {
        navigate('/mealinfo',{state:{meal}}); 
    };
    return (
        <div className="meal" onClick={navigateToMealInfoalInfo}>
            <div>
                <img src={meal.img_url} alt={meal.mealName} />
                <h3>{meal.mealName}</h3>
                <p>Calories: {meal.calories}</p>
                <p>Proteins: {meal.proteins}g</p>
                <p>Carbs: {meal.carbs}g</p>
                <p>Fats: {meal.fats}g</p>
            </div>
        </div>
    );
}

export default MealCard;