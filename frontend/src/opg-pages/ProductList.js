import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import '../style/product_list.css'

function ListProducts() {
  const [prodData, setProdData] = useState([]);
  const [userData, setUserData] = useState([]);
  const navigate = useNavigate();
  const productUrl = 'http://localhost:8000/api/list_products/';
  const userUrl = 'http://localhost:8000/api/auth/';

  useEffect(() => {
    const fetchProdData = async () => {
      try {
        const response = await axios.get(productUrl, {
            withCredentials: true,
        });
        console.log("responsesss: ", response)
        setProdData(response.data); 
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    const fetchUserData = async () => {
        try {
          const response = await axios.get(userUrl, {
              withCredentials: true,
          });
          console.log("response dolje: ", response)
          setUserData(response.data); 
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      };

    fetchUserData();
    fetchProdData();
  }, []);

  const handleProductClick = (product) => {
    console.log("detalji: ", product)
    navigate(`/get_product/${product.id}`);
  };

  return (
    <div className="container">
      {userData ? (
        <div className="user-info">
          <p className="opg-name">{userData.naziv_opg}</p>
          <p className="user-name">{userData.ime} {userData.prezime}</p>
        </div>
      ) : (
        <p>Loading user data...</p>
      )}

      <div className="products-list">
        {prodData.map((item) => (
          <div key={item.id} className="product-item" onClick={() => handleProductClick(item)}>
            <p className="product-name">{item.name}</p>
            <p className="product-category">{item.category}</p>
            <p className="product-detail">{item.detail}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default ListProducts;
