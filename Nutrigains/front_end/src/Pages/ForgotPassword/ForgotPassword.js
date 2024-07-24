import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './ForgotPassword.css';
import axios from "axios";
import Navbar from '../NavBar/navBar';

const ForgotPassword = () => {
    const [email, setEmail] = useState('');
    const [otpSent, setOtpSent] = useState(false);
    const [otp, setOtp] = useState('');
    const [newPassword, setNewPassword] = useState('');
    const [confirmNewPassword, setConfirmNewPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleSendOtp = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:5000/signup/isexistingemail', { 
              params: { 'user_email': email }
            });
            if (response.data == "False"){
                setError("account doesn't exist!");
                return;
            }
        } catch (error) {
            console.error('Error sending OTP:', error);
        }
        try {
            const response = await axios.get('http://127.0.0.1:5000//otpverification/sendotp', { 
              params: { 'email': email }
            });
            setOtpSent(true); // Enable the OTP message and fields
        } catch (error) {
            console.error('Error sending OTP:', error);
        }
    };

    const handleChangePassword = async (event) => {
        event.preventDefault();
        if (newPassword !== confirmNewPassword) {
            alert("Passwords do not match!");
            return;
        }
        try {
            const response = await axios.get('http://127.0.0.1:5000/otpverification/verifyotp', {
              params: { 'email': email, 'otp': otp }
            });
            if (response.data != "True") {
                alert("OTP doesn't match!")
                return;
            }
            else{
                await axios.get('http://127.0.0.1:5000/profilehandler/updateprofile', {
                    params: {'email': email, 'password': newPassword}
                });
                navigate('/login');
            }
        } catch (error) {
            console.error('Error changing password:', error);
        }
    };

    return (
        <>
            <Navbar/>
            <div className="forgot-password-container">
                <h2>Forgot Password</h2>
                <form className="forgot-password-form" onSubmit={handleChangePassword}>
                    <label htmlFor="email">Enter Email:</label>
                    <input 
                        type="email" 
                        id="email" 
                        name="email" 
                        value={email} 
                        onChange={e => setEmail(e.target.value)} 
                    />
                    <button type="button" id="send-otp-btn" onClick={handleSendOtp}>Send OTP</button>

                    {otpSent && <p className="otp-message">An OTP was sent to your e-mail</p>}
                    {!otpSent && error != '' && <p className="otp-message">{error}</p>}

                    <label htmlFor="otp">OTP:</label>
                    <input 
                        type="text" 
                        id="otp" 
                        name="otp" 
                        value={otp}
                        onChange={e => setOtp(e.target.value)}
                        disabled={!otpSent}
                    />

                    <label htmlFor="new-password">New Password:</label>
                    <input 
                        type="password" 
                        id="new-password" 
                        name="new-password" 
                        value={newPassword}
                        onChange={e => setNewPassword(e.target.value)}
                        disabled={!otpSent}
                    />

                    <label htmlFor="confirm-new-password">Confirm New Password:</label>
                    <input 
                        type="password" 
                        id="confirm-new-password" 
                        name="confirm-new-password" 
                        value={confirmNewPassword}
                        onChange={e => setConfirmNewPassword(e.target.value)}
                        disabled={!otpSent}
                    />

                    <button type="submit" id="change-password-btn" disabled={!otpSent}>Change Password</button>
                </form>

                <Link to="/login" id="back-to-login">Back to Login Page</Link>
            </div>
        </>
    );
};

export default ForgotPassword;
