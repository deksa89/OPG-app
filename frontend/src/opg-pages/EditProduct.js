import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';
import '../style/product_detail.css';

function EditProduct() {
  const { status_id } = useParams();
  const navigate = useNavigate();
  const [product, setProduct] = useState({
    category: '',
    name: '',
    detail: '',
  });

  useEffect(() => {
    const fetchProductData = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/api/get_product/${status_id}`, {
            withCredentials: true,
          });
        setProduct(response.data);
      } catch (error) {
        console.error('Error fetching product data:', error);
      }
    };

    fetchProductData();
  }, [status_id]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setProduct({
      ...product,
      [name]: value,
    });
  };

  const handleSave = async () => {
    try {
      await axios.put(`http://localhost:8000/api/update_product/${status_id}`, product, {
        withCredentials: true,
      });
      alert("Product updated successfully!");
      navigate(`/list_products`);
    } catch (error) {
      console.error('Error updating product:', error);
    }
  };

  return (
    <div className="container">
      {product ? (
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
            <button className="cancel-button" onClick={() => navigate(`/list_products`)}>Cancel</button>
          </div>
        </div>
      ) : (
        <p>Loading product data...</p>
      )}
    </div>
  );
}

export default EditProduct;
