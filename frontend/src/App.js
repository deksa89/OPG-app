import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import WelcomePage from './opg-pages/WelcomePage';
import Login from './opg-pages/Login';
import Register from './opg-pages/Register';

import { useState, useEffect } from 'react';

function App() {
  // useEffect(() => {
  //   console.log(process.env.REACT_APP_API_URL)
  // }, [])


  return (
    <Router>
      <Routes>
        <Route path="/" element={<WelcomePage />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </Router>
  );
}

export default App;