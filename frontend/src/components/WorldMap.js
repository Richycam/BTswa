// src/components/WorldMap.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';

const WorldMap = () => {
  const [map, setMap] = useState('');
  const [error, setError] = useState('');

  useEffect(() => {
    axios.get('http://localhost:5000/worldmap')
      .then(response => {
        setMap(response.data.map);
      })
      .catch(err => {
        setError('Error fetching world map.');
        console.error(err);
      });
  }, []);

  return (
    <div className="feature-container">
      <h2>World Map</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {map ? <pre>{map}</pre> : <p>Loading...</p>}
    </div>
  );
};

export default WorldMap;
