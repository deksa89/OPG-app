import React, { useState, useEffect } from 'react';
import axios from 'axios';

function ListProducts() {
  const [data, setData] = useState([]);
  const apiUrl = 'http://localhost:8000/api/list_products/';

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(apiUrl, {
            withCredentials: true,
        });
        console.log("response: ", response)
        setData(response.data); 
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      {data.map((item) => (
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

export default ListProducts;
