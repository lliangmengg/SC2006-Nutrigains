import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import './favourites.css'; // Make sure to import your CSS file
import axios from "axios";
import MealCard from "../MealCard/MealCard";
import Navbar from '../NavBar/navBar.js'

const Favourites = () => {
    const [meals, setMeals] = useState([]); // This will hold an array of meals
  
    useEffect(() => {
      const fetchMeals = async () => {
        try {
          const response = await axios.get('http://127.0.0.1:5000/favourites/getfavourites', {
            params: { 'email': sessionStorage.getItem("email") }
          });
          setMeals(response.data.result); // Storing the array of meals directly
        } catch (error) {
          console.error('There was an error fetching the meals!', error);
        }
      };
  
      fetchMeals();
    }, []); // The empty array ensures this effect only runs once when the component mounts
    
    const deleteMeal = async (meal_id) => {
      try {
          const response = await axios.delete('http://127.0.0.1:5000/favourites/deletefavourite',{
          params: { 'email': sessionStorage.getItem("email"), 'meal_id': meal_id }
        });
        setMeals(currentMeals => currentMeals.filter(meal => meal.mealId !== meal_id));
      } catch (error) {
        console.error('Error deleting the meal:', error);
      }
    };
    return (
      <>
      <Navbar />
        <div className="meal-history">
          {meals.length > 0 ? (
            meals.map((meal, index) => (
              <div key={index} className="meal-entry">
                <MealCard meal={meal} />
                <button onClick={() => deleteMeal(meal.mealId)} className="delete-button">
                  Delete
                </button>
              </div>
            ))
          ) : (
            <p>No favourite meals to display.</p>
          )}
        </div>
      </>
    );
  };

export default Favourites;

