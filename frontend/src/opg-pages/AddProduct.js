import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import '../style/product_detail.css';

function AddProduct() {
  const navigate = useNavigate();
  const [product, setProduct] = useState({
    category: '',
    name: '',
    detail: '',
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setProduct({
      ...product,
      [name]: value,
    });
  };

  const handleSave = async () => {
    try {
      await axios.post('http://localhost:8000/api/add_product/', product, {
        withCredentials: true,
      });
      alert("Product added successfully!");
      navigate('/list_products');
    } catch (error) {
      console.error('Error adding product:', error);
    }
  };

  return (
    <div className="container">
      <div className="prod-info">
        <div className="prod-field">
          <label className="prod-label" htmlFor="category">Category</label>
          <input
            className="prod-input"
            type="text"
            id="category"
            name="category"
            value={product.category}
            onChange={handleInputChange}
          />
        </div>
        <div className="prod-field">
          <label className="prod-label" htmlFor="name">Name</label>
          <input
            className="prod-input"
            type="text"
            id="name"
            name="name"
            value={product.name}
            onChange={handleInputChange}
          />
        </div>
        <div className="prod-field">
          <label className="prod-label" htmlFor="detail">Detail</label>
          <textarea
            className="prod-input"
            id="detail"
            name="detail"
            value={product.detail}
            onChange={handleInputChange}
          />
        </div>
        <div className="buttons">
          <button className="save-button" onClick={handleSave}>Save</button>
          <button className="cancel-button" onClick={() => navigate('/list_products')}>Cancel</button>
        </div>
      </div>
    </div>
  );
}

export default AddProduct;
