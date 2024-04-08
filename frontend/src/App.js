import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import WelcomePage from './opg-pages/WelcomePage';
import Login from './opg-pages/Login';
import Register from './opg-pages/Register';
import ListProducts from './opg-pages/ProductList';


function App() {

  return (
    <Router>
      <Routes>
        <Route path="/" element={<WelcomePage />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/list_products" element={<ListProducts />} />
      </Routes>
    </Router>
  );
}

export default App;