import logo from './logo.svg';
import './App.css';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import HomePage from './Pages/Home/home';
import Chatbot from './Pages/chatbot/chatbot';
import Profile from './Pages/Profile/Profile';
import History from './Pages/History/History';
import ForgotPassword from './Pages/ForgotPassword/ForgotPassword';
import NutritionTracking from './Pages/NutritionTracking/nutritionTracking';
import SignUp from './Pages/Signup/signup';
import Login from './Pages/Login/login';
import Favourites from './Pages/favourites/favourites';
import MealInfo from './Pages/MealInfo/MealInfo';
import Browse from './Pages/Browse/Browse';
function App() {
  return (
      <Router>
        <Routes>
          <Route exact path="/" element={<HomePage />} />
          <Route exact path="/home" element={<HomePage />} />
          <Route path="/mealinfo" element={<MealInfo />} />
          <Route path="/chatbot" element={<Chatbot />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/history" element={<History />} />
          <Route path="/forgotpassword" element={<ForgotPassword />} />
          <Route path="/login" element={<Login />} />
          <Route path="/nutritiontracking" element={<NutritionTracking />} />
          <Route path="/signup" element={<SignUp />} />
          <Route path="/favourites" element={<Favourites />} />
          <Route path="/browse" element={<Browse />} />
        </Routes>
      </Router>
  );
}

export default App;
