import React, { useState, useEffect } from 'react';
import axios from 'axios';

function WelcomePage() {
  const [welcomeMessage, setWelcomeMessage] = useState('');

  useEffect(() => {
    axios.get('http://localhost:8000/')
      .then(response => {
        //console.log("response: ", response);
        setWelcomeMessage(response.data.message);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  const handleLoginClick = () => {
    console.log("Login button clicked");
  };

  const handleRegisterClick = () => {
    console.log("Register button clicked");
  };

  return (
    <div>
      <h1>Welcome!</h1>
      <p>{welcomeMessage}</p>
      <button onClick={handleLoginClick}>Login</button>
      <button onClick={handleRegisterClick}>Register</button>
    </div>
  );
}

export default WelcomePage;
