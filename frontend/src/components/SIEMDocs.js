// src/components/SIEMDocs.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';

const SIEMDocs = () => {
  const [docs, setDocs] = useState('');
  const [error, setError] = useState('');

  useEffect(() => {
    axios.get('http://localhost:5000/siem/docs')
      .then(response => {
        setDocs(response.data.docs);
      })
      .catch(err => {
        setError('Error fetching SIEM documentation.');
        console.error(err);
      });
  }, []);

  return (
    <div className="feature-container">
      <h2>SIEM Documentation</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {docs ? <a href={docs} target="_blank" rel="noopener noreferrer">{docs}</a> : <p>Loading...</p>}
    </div>
  );
};

export default SIEMDocs;
