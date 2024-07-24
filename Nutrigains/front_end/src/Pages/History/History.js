import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import './History.css'; 
import axios from "axios"
import MealCard from "../MealCard/MealCard";
import Navbar from '../NavBar/navBar';

const History = () => {
  const [mealsByDate, setMealsByDate] = useState({});

  useEffect(() => {
    const fetchMeals = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/mealtracking/monthlymealhistory', {
          params: { 'email': sessionStorage.getItem("email") }
        });
        setMealsByDate(response.data); // assuming response.data is an object with dates as keys
        console.log(response.data);
      } catch (error) {
        console.error('There was an error fetching the meals!', error);
      }
    };

    fetchMeals();
  }, []); // The empty array ensures this effect only runs once when the component mounts

  return (
    <>
      <Navbar/>
      <div className="meal-history">
        {Object.entries(mealsByDate).reverse().map(([date, meals]) => (
          <div className="day" key={date}>
            <h3>Date: {new Date(date).toLocaleDateString()}</h3>
            <div>
              {meals.length > 0 ? (
                meals.map((meal, index) => (
                  <MealCard key={index} meal={meal} />
                ))
              ) : (
                <p>No meals to display for this day.</p>
              )}
            </div>
          </div>
        ))}
      </div>
    </>
  );
};

export default History;
