import {React, useState} from 'react';
import { Link,useNavigate } from 'react-router-dom';
import { isEmail } from 'validator';
import './signup.css'; // Make sure to import your CSS file
import axios from "axios"
import Navbar from '../NavBar/navBar';

function SignUp() {

    const [formData, setFormData] = useState({
        email: '',
        fullName: '',
        dob: '',
        gender: '',
        weight: '',
        height: '',
        goal: '',
        activity_level: '',
        password: '',
        confirmPassword: ''
    });

    const [otp, setOtp] = useState('');
    const [otpSent, setOtpSent] = useState(false);
    const [error, setError] = useState('');
    const [otpError, setOtpError] = useState('');
    const navigate = useNavigate();

    const handleSendOtp = async () => {
        // Check for empty fields in the form data
        for (let key in formData) {
            if (formData[key].trim() === '' && key !== 'confirmPassword') { // Ignore confirmPassword for emptiness check
                setError(`Please fill out the ${key.replace(/_/g, ' ')} field.`);
                return;
            }
        }
      
        // Check if passwords match
        if (formData.password !== formData.confirmPassword) {
            setError("Passwords do not match!");
            return;
        }

        // check if user already exists
        try {
            const response = await axios.get('http://127.0.0.1:5000/signup/isexistingemail', { params: { 'user_email': formData.email } });
            console.log(response.data)
            if (response.data == "True") {
                setError("Account already exists!")
                return;
            }
        } catch (error) {
            console.error('There was an error checking email!', error);
        }
        
        // If all checks pass, send OTP
        setError(''); // Clear any previous errors
        try {
            await axios.get('http://127.0.0.1:5000/otpverification/sendotp', { params: { 'email': formData.email } });
            setOtpSent(true);
        } catch (error) {
            console.error('There was an error sending the OTP!', error);
        }
    };

    const handleVerifyOtpAndRegister = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.get('http://127.0.0.1:5000/otpverification/verifyotp', { params: { 'email': formData.email, 'otp': otp } });
            console.log(response.data)
            if (response.data == "False"){
                // display otp is invalid
                setOtpError("OTP is invalid!");
                return;
            }
        } catch (error) {
            console.error('There was an error verifying the OTP!', error);
        }
        try {
            await axios.get('http://127.0.0.1:5000/signup/storeuser', {params : {
              "email": formData.email,
              "full_name": formData.fullName,
              "password": formData.password,
              "dob": formData.dob,
              "height": formData.height,
              "weight": formData.weight,
              "goal": formData.goal,
              "gender": formData.gender,
              "activity_level": formData.activity_level
            }});
            // navigate to login
            navigate('/login');
          } catch (error) {
            console.error('There was an error saving the data!', error);
          }
    }

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });

        
    };

    return (
        <div>
            <Navbar/>

            <div className="signup-container">
                <h2>Sign-up</h2>
                <form className="signup-form">
                    <label htmlFor="email">Email:</label>
                    <input type="email" id="email" name="email" value={formData.email} onChange={handleChange} />

                    <label htmlFor="fullname">Full Name:</label>
                    <input type="text" id="fullname" name="fullName" value={formData.fullName} onChange={handleChange} />

                    <label htmlFor="dob">Date of Birth:</label>
                    <input type="date" id="dob" name="dob" value={formData.dob} onChange={handleChange} />

                    <label htmlFor="gender">Gender:</label>
                    <select id="gender" name="gender" value={formData.gender} onChange={handleChange}>
                        <option value="">Select</option>
                        <option value="male">Male</option>
                        <option value="female">Female</option>
                        <option value="other">Other</option>
                    </select>

                    <label htmlFor="weight">Current Weight:</label>
                    <input type="text" id="weight" name="weight" value={formData.weight} onChange={handleChange} />

                    <label htmlFor="height">Height:</label>
                    <input type="text" id="height" name="height" value={formData.height} onChange={handleChange} />

                    <label htmlFor="goal">Goal:</label>
                    <select id="goal" name="goal" value={formData.goal} onChange={handleChange}>
                        <option value="">Select</option>
                        <option value="reduce_fat">Reduce Fat</option>
                        <option value="gain_muscle">Gain Muscle</option>
                        <option value="maintain_weight">Maintain Weight</option>
                    </select>

                    <label htmlFor="activity">Activity Level:</label>
                    <select id="activity" name="activity_level" value={formData.activity_level} onChange={handleChange}>
                        <option value="">Select</option>
                        <option value="lightly_active">Lightly Active</option>
                        <option value="moderately_active">Moderately Active</option>
                        <option value="very_active">Very Active</option>
                    </select>

                    <label htmlFor="password">New Password:</label>
                    <input type="password" id="password" name="password" value={formData.password} onChange={handleChange} />

                    <label htmlFor="confirm-password">Confirm Password:</label>
                    <input type="password" id="confirm-password" name="confirmPassword" value={formData.confirmPassword} onChange={handleChange} />

                    <div className="error-message">{error}</div>
                    <button type="button" id="send-otp-btn" onClick={handleSendOtp} >Verify Email</button>
                    <input 
                        type="text" 
                        placeholder="Enter OTP" 
                        value={otp} 
                        onChange={(e) => setOtp(e.target.value)} 
                        disabled={!otpSent} 
                    />
                    <div className="error-message">{otpError}</div>
                    <button type="button" id="register-btn" onClick={handleVerifyOtpAndRegister} disabled={!otpSent}>Register</button>
                </form>
                <Link to="/login" id="back-to-login">Back to Login Page</Link>
            </div>
        </div>
    );
};

export default SignUp;
