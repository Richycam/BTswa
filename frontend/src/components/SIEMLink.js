// src/components/SIEMLink.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';

const SIEMLink = () => {
  const [link, setLink] = useState('');
  const [error, setError] = useState('');

  useEffect(() => {
    axios.get('http://localhost:5000/siem/link')
      .then(response => {
        setLink(response.data.link);
      })
      .catch(err => {
        setError('Error fetching SIEM link.');
        console.error(err);
      });
  }, []);

  return (
    <div className="feature-container">
      <h2>SIEM Tool Link</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {link ? <a href={link} target="_blank" rel="noopener noreferrer">{link}</a> : <p>Loading...</p>}
    </div>
  );
};

export default SIEMLink;
