import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import './Browse.css'; // Make sure to import your CSS file
import MealCard from "../MealCard/MealCard";
import axios from "axios";
import Navbar from '../NavBar/navBar.js'

function Browse() {
    const [searchTerm, setSearchTerm] = useState('');
    const [meals, setMeals] = useState(JSON.parse(sessionStorage.getItem("searchMeals")) || []);

    useEffect(() => {
        sessionStorage.setItem("searchMeals", JSON.stringify(meals));
    }, [meals]);

    const handleSearchClick = async () => {
        if (!searchTerm) {
            console.log('Search term is empty.');
            return;
        }
        try {
            const response = await axios.get('http://127.0.0.1:5000/browse', {
                params: { 'query': searchTerm }
            });
            setMeals(response.data.result);
            console.log(response.data.result);
        } catch (error) {
            console.error('There was an error fetching the meals!', error);
        }
    };

    return (
        <div>
            <Navbar />
            <div className="search-bar">
                <input
                    type="text"
                    placeholder="Browse..."
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                />
                <button className="search-button" onClick={handleSearchClick}>Search</button>
            </div>
            <div>
                {meals.length > 0 ? (
                    meals.map((meal, index) => (
                        <MealCard key={index} meal={meal} />
                    ))
                ) : (
                    <div className="no-meals-message">
                    No meals to display. Use the search bar to find meals.
                </div>
                )}
            </div>
        </div>
    );
}

export default Browse;
