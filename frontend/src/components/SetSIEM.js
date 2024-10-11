// frontend/src/components/SetSIEM.js

import React, { useState } from 'react';
import axios from 'axios';

const SetSIEM = () => {
  const [tool, setTool] = useState('');
  const [link, setLink] = useState('');
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  const handleSetSIEM = () => {
    if (!tool || !link) {
      setError('Both tool name and link are required.');
      setMessage('');
      return;
    }

    axios.post('http://localhost:5000/siem', { tool, link })
      .then(response => {
        setMessage(response.data.message);
        setError('');
        setTool('');
        setLink('');
      })
      .catch(err => {
        setError('Error setting SIEM tool.');
        setMessage('');
        console.error(err);
      });
  };

  return (
    <div className="feature-container">
      <h2>Set SIEM Tool</h2>
      <div>
        <label>Tool Name:</label>
        <input
          type="text"
          value={tool}
          onChange={(e) => setTool(e.target.value)}
          placeholder="e.g., Splunk"
        />
      </div>
      <div>
        <label>Tool Link:</label>
        <input
          type="text"
          value={link}
          onChange={(e) => setLink(e.target.value)}
          placeholder="e.g., https://www.splunk.com/"
        />
      </div>
      <button onClick={handleSetSIEM}>Set SIEM Tool</button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {message && <p style={{ color: 'green' }}>{message}</p>}
    </div>
  );
};

export default SetSIEM;
