import React from 'react';
import './home.css'; // Make sure this path is correct
import {Link} from 'react-router-dom'
import { User } from '../../User'; // import user
import Navbar from '../NavBar/navBar.js'

const HomePage = () => {
  return (
    <>
      <Navbar />
      <div className="hero">
        <div className="hero-content">
          <h1>Welcome to Your Personalized Meal Planner!</h1>
          <p>Get personalized meal recommendations and track your nutrition easily.</p>
        </div>
      </div>

      <div className="features">
        <div className="feature">
          <div className="feature-content">
            <h2>NutriGains Chatbot</h2>
            <p>Get customized meal suggestions based on your preferences and dietary needs</p>
          </div>
        </div>
        <div className="feature">
          <div className="feature-content">
            <h2>Detailed Nutritional Information using Nutrition Tracking</h2>
            <p>Explore detailed nutritional information for each meal</p>
          </div>
        </div>
        <div className="feature">
          <div className="feature-content">
            <h2>Features Galore</h2>
            <p>Use Add to Favourites, History or Browse features to your advantage!!</p>
          </div>
        </div>
      </div>
    </>
  );
};

export default HomePage;
