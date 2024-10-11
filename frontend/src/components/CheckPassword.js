// src/components/CheckPassword.js

import React, { useState } from 'react';
import axios from 'axios';

const CheckPassword = () => {
  const [password, setPassword] = useState('');
  const [wordlist, setWordlist] = useState('');
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  const handleCheck = () => {
    if (!password || !wordlist) {
      setError('Please enter both password and wordlist.');
      return;
    }

    setError('');
    setMessage('Checking password...');

    axios.post('http://localhost:5000/check_password', { password, wordlist })
      .then(response => {
        setMessage(response.data.message);
      })
      .catch(err => {
        setError('Error checking password.');
        setMessage('');
        console.error(err);
      });
  };

  return (
    <div className="feature-container">
      <h2>Check Password</h2>
      <div>
        <label>Password:</label>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Enter password"
        />
      </div>
      <div>
        <label>Wordlist:</label>
        <textarea
          value={wordlist}
          onChange={(e) => setWordlist(e.target.value)}
          placeholder="Enter wordlist, one word per line"
          rows="10"
          cols="50"
        ></textarea>
      </div>
      <button onClick={handleCheck}>Check Password</button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {message && <p>{message}</p>}
    </div>
  );
};

export default CheckPassword;
