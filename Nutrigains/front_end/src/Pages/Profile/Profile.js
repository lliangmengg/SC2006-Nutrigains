import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './Profile.css';
import axios from 'axios';
import Navbar from '../NavBar/navBar';

const Profile = () => {
  const [userData, setUserData] = useState({
    email: '',
    fullName: '',
    dob: '',
    gender: '',
    weight: '',
    height: '',
    goal: '',
    activity: ''
  });

  const [isEditable, setIsEditable] = useState(false);
  const [message, setMessage] = useState('');
  const navigate = useNavigate();

  const handleSignOut = () => {
    // Remove email from sessionStorage
    sessionStorage.removeItem("email");

    // Navigate to the home page
    navigate("/");
  };

  useEffect(() => {
    const fetchUserProfile = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/profilehandler/getprofile', {
          params: { email: sessionStorage.getItem("email") }
        });
        setUserData(response.data);
        console.log(response.data);
      } catch (error) {
        console.error('There was an error fetching the data!', error);
      }
    };

    fetchUserProfile();
  }, []);

  const handleChange = (event) => {
    const { name, value } = event.target;
    setUserData(prevState => ({
      ...prevState,
      [name]: value
    }));
    setMessage(''); // Clear messages on input change
  };

  const handleEdit = () => {
    setIsEditable(true);
    setMessage('');
  };

  const handleSave = async () => {
    // Check if any field is empty
    if (Object.values(userData).some(value => value === '')) {
      setMessage('All fields must be filled out.');
      return;
    }
    console.log(Object.values(userData))

    try {

      // Implement your save logic here, sending data to the backend
      await axios.get('http://127.0.0.1:5000/profilehandler/updateprofile', {params : {
        "email": userData.email,
        "full_name": userData.fullName,
        "dob": userData.dob,
        "height": userData.height,
        "weight": userData.weight,
        "goal": userData.goal,
        "gender": userData.gender,
        "activity_level": userData.activity
      }});
      setIsEditable(false);
      setMessage('Profile updated successfully!');
    } catch (error) {
      setMessage('Failed to update profile.');
      console.error('There was an error saving the data!', error);
    }
  };

  return (
    <>
      <Navbar/>
      <div className="profile-container">
        <form className="profile-form">
          <label htmlFor="email">Email (not editable):</label>
          <input type="email" id="email" name="email" value={userData.email} disabled />

          <label htmlFor="fullname">Full Name:</label>
          <input type="text" id="fullname" name="fullname" value={userData.fullName} onChange={handleChange} disabled={!isEditable} />

          <label htmlFor="dob">Date of Birth:</label>
          <input type="date" id="dob" name="dob" value={userData.dob} onChange={handleChange} disabled={!isEditable} />

          <label htmlFor="gender">Gender:</label>
          <select id="gender" name="gender" value={userData.gender} onChange={handleChange} disabled={!isEditable}>
            <option value="">Select</option>
            <option value="male">Male</option>
            <option value="female">Female</option>
          </select>

          <label htmlFor="weight">Current Weight:</label>
          <input type="text" id="weight" name="weight" value={userData.weight} onChange={handleChange} disabled={!isEditable} />

          <label htmlFor="height">Height:</label>
          <input type="text" id="height" name="height" value={userData.height} onChange={handleChange} disabled={!isEditable} />

          <label htmlFor="goal">Goal:</label>
          <select id="goal" name="goal" value={userData.goal} onChange={handleChange} disabled={!isEditable}>
            <option value="">Select</option>
            <option value="reduce_fat">Reduce Fat</option>
            <option value="gain_muscle">Gain Muscle</option>
            <option value="maintain_weight">Maintain Weight</option>
          </select>

          <label htmlFor="activity">Activity Level:</label>
          <select id="activity" name="activity_level" value={userData.activity_level} onChange={handleChange} disabled={!isEditable}>
            <option value="">Select</option>
            <option value="lightly_active">Lightly Active</option>
            <option value="moderately_active">Moderately Active</option>
            <option value="very_active">Very Active</option>
          </select>

          <button type="button" id="edit-btn" onClick={handleEdit} disabled={isEditable}>Edit</button>
          <button type="button" id="save-btn" onClick={handleSave} disabled={!isEditable}>Save Changes</button>
        </form>

        <button id="sign-out-btn" onClick={handleSignOut}>Sign Out</button>
      </div>
    </>
  );
};

export default Profile;
