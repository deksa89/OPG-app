import React, { useState, useEffect } from 'react';
import axios from 'axios';

function ListProducts() {
  const [prodData, setProdData] = useState([]);
  const [userData, setUserData] = useState([]);
  const productUrl = 'http://localhost:8000/api/list_products/';
  const userUrl = 'http://localhost:8000/api/auth/';

  useEffect(() => {
    const fetchProdData = async () => {
      try {
        const response = await axios.get(productUrl, {
            withCredentials: true,
        });
        console.log("response: ", response)
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
          console.log("response: ", response)
          setUserData(response.data); 
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      };

    fetchUserData();
    fetchProdData();
  }, []);

  return (
    <div>
    {userData.map((user) => (
        
    ))}

      {prodData.map((item) => (
          <div key={item.id}>
            <h1>{item.farm.naziv_opg}</h1>
          <p>{item.name}</p>
          <p>{item.category}</p>
          <p>{item.detail}</p>
        </div>
      ))}
    </div>
  );
}

export default ListProducts;  //NASTAVITI OVO RADITI DA ISPISES IME VLASNIKA OPG-a NA list_product STRANICU I SVE PROIZVODE KOJE IMA NA STRANICI
