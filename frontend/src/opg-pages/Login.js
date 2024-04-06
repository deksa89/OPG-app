import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

function Login() {
  const [useremail, setUseremail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    console.log('Attempting to login with:', useremail, password);

    axios.post('/login', { useremail, password })
      .then((response) => {
        console.log('Login successful', response.data);
        navigate('/product_list');
      })
      .catch((error) => {
        console.error('Login failed', error);
      });
  };

  const containerStyle = {
    maxWidth: '400px',
    margin: '50px auto',
    padding: '20px',
    boxShadow: '0 4px 8px rgba(0,0,0,0.1)',
    borderRadius: '5px'
  };

  const formStyle = {
    display: 'flex',
    flexDirection: 'column',
    gap: '15px',
  };

  const labelStyle = {
    marginBottom: '5px',
    fontWeight: 'bold'
  };

  const inputStyle = {
    padding: '10px',
    fontSize: '16px',
    marginLeft: '10px',
    border: '1px solid #ddd',
    borderRadius: '4px'
  };

  const buttonStyle = {
    padding: '10px 20px',
    fontSize: '18px',
    backgroundColor: '#007bff',
    color: 'white',
    border: 'none',
    borderRadius: '5px',
    cursor: 'pointer'
  };

  return (
    <div style={containerStyle}>
      <h2>Login</h2>
      <form onSubmit={handleLogin} style={formStyle}>
        <div>
          <label htmlFor="useremail" style={labelStyle}>Email adresa:</label>
          <input
            type="text"
            id="useremail"
            value={useremail}
            onChange={(e) => setUseremail(e.target.value)}
            style={inputStyle}
          />
        </div>
        <div>
          <label htmlFor="password" style={labelStyle}>Lozinka:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            style={inputStyle}
          />
        </div>
        <button type="submit" style={buttonStyle}>Login</button>
      </form>
    </div>
  );
}

export default Login;