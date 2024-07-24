import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import './chatbot.css';
import MealCard from '../MealCard/MealCard';
import axios from 'axios'
import Navbar from '../NavBar/navBar';

const Chatbot = () => {
    const [messages, setMessages] = useState(JSON.parse(sessionStorage.getItem("chatbotMessages")) || []);
    const [input, setInput] = useState('');
    const [chatHistory, setChatHistory] = useState([]); // To store chat history in the desired format
    const [isLoading, setIsLoading] = useState(false);

    useEffect(() => {
        sessionStorage.setItem("chatbotMessages", JSON.stringify(messages));
    }, [messages]);

    const handleInputChange = (event) => {
        setInput(event.target.value);
    };

    const handleSend = () => {
        if (input.trim()) {
            setMessages([...messages, { text: input, sender: 'user' }]);
            // Update chatHistory with the user's message
            setChatHistory([...chatHistory, { parts: {text: input}, role: "user" }]);
            setInput('');
            getBotResponse(input);
        }
    };

    const getBotResponse = async (userInput) => {
      setIsLoading(true);
      try {
          const response = await axios.get('http://127.0.0.1:5000/chatbot/getresponse', {
              params: {
                  "history": JSON.stringify(chatHistory),  // Send chatHistory as a JSON string
                  "message": userInput  // Send the current message
              }
          });
          const jsonResponse = response.data;

          setMessages(messages => [...messages, {
              text: jsonResponse.TextResponse,
              sender: 'bot',
              meals: jsonResponse.MealResponse
          }]);
          console.log(response.data)
          const botText = jsonResponse.MealResponse && jsonResponse.MealResponse.length > 0 ? 
                          jsonResponse.hiddenTextResponse : jsonResponse.TextResponse;
          
          setChatHistory(chatHistory => [...chatHistory, { parts: {text: botText}, role: "model" }]);
      } catch (error) {
          console.error('There was an error fetching the response!', error);
      } finally {
          setIsLoading(false);
      }
  };

    const handleClearChat = () => {
      setMessages([]);
      setChatHistory([]); // Clear chat history along with messages
    };

    return (
        <>
            <Navbar/>
            <div className="container">
                <div className="chat-container">
                    <div className="chat-window">
                        <div className="chat-header">
                            Chatbot
                            <button className="clear-chat-button" onClick={handleClearChat} disabled={isLoading}>Clear Chat</button>
                        </div>
                        <div className="chat-body">
                        {messages.map((message, index) => (
                            <div key={index} className={`chat-message ${message.sender}-message`}>
                                <p>{message.text}</p>
                                {message.sender === 'bot' && message.meals && (
                                    <div className="meal-responses">
                                        {message.meals.map((meal, idx) => (
                                            <MealCard key={idx} meal={meal} />
                                        ))}
                                    </div>
                                )}
                            </div>
                        ))}
                        </div>
                        <div className="chat-input">
                            <input
                                type="text"
                                placeholder="Type a message..."
                                value={input}
                                onChange={handleInputChange}
                            ></input>
                            <button onClick={handleSend} disabled={isLoading}>Send</button>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
};

export default Chatbot;
