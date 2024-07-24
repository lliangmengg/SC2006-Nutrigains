import {React, useState} from 'react';
import { Link,useNavigate} from 'react-router-dom';
import './login.css'; 
import axios from "axios"
import Navbar from '../NavBar/navBar.js'

function Login() {

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleLogin = async (event) => {
        event.preventDefault(); 
        setError('');

        try {
            const response = await axios.get('http://127.0.0.1:5000/login', {
                params: { 'email': email, 'password': password }
            });
            // Assuming your API returns a status code of 200 for successful login
            if (response.status === 200) {
                // Navigate to the homepage or dashboard
                sessionStorage.setItem("email", email)
                navigate('/home');
            } else {
                // Set error message from the response if login is not successful
                setError(response.data.message || 'Login failed, please try again.');
            }
        } catch (error) {
            // Set error message from axios error response
            setError(error.response.data.message || 'An error occurred while logging in.');
        }
    };

    return (
        <div>
            <Navbar />
            <div className="login-container">
                <h2>Login</h2>
                <p className="login-access-text">Login to access our Features</p>
                <form className="login-form" onSubmit={handleLogin}>
                    <label htmlFor="email">Email:</label>
                    <input
                        type="email"
                        id="email"
                        name="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                    />

                    <label htmlFor="password">Password:</label>
                    <input
                        type="password"
                        id="password"
                        name="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />
                    {error && <div className="login-error">{error}</div>}
                    <button type="submit" id="login-btn">Login</button>
                </form>
                <Link to="/signup" className="signup-link">Don't Have an Account? Sign-up</Link>
                <Link to="/forgotpassword" id="forgot-password">Forgot/Change Password</Link>
            </div>
        </div>
    );
}

export default Login;
