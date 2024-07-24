import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './navBar.css';

const Navbar = () => {
  const navigate = useNavigate();

  const handleNavigation = (event, path) => {
    // Prevent default link behavior
    event.preventDefault();

    // Check if the userEmail is stored in sessionStorage
    if (sessionStorage.getItem("email")) {
      navigate(path); // User is logged in, proceed to navigate
    } else {
      // User is not logged in, alert them to log in
      alert("You must log in first!");
    }
  };

  return (
    <header>
      <div className="logo">NutriGains</div>
      <nav>
        <ul>
          <li><Link to="/" >Home</Link></li>
          <li><Link to="/chatbot" onClick={(event) => handleNavigation(event, '/chatbot')}>Chatbot</Link></li>
          <li><Link to="/browse" onClick={(event) => handleNavigation(event, '/browse')}>Browse</Link></li>
          <li><Link to="/nutritiontracking" onClick={(event) => handleNavigation(event, '/nutritiontracking')}>Nutrition Tracking</Link></li>
          <li><Link to="/history" onClick={(event) => handleNavigation(event, '/history')}>History</Link></li>
          <li><Link to="/favourites" onClick={(event) => handleNavigation(event, '/favourites')}>Favourites</Link></li>
          <li><Link to="/profile" onClick={(event) => handleNavigation(event, '/profile')}>Profile</Link></li>
          {!sessionStorage.getItem("email") && (
            <>
              <li><Link to="/signup">Signup</Link></li>
              <li><Link to="/login">Login</Link></li>
            </>
          )}
        </ul>
      </nav>
    </header>
  );
};

export default Navbar;



