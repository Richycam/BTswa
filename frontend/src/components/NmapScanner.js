// src/components/NmapScanner.js

import React, { useState } from 'react';
import axios from 'axios';

const NmapScanner = () => {
  const [ip, setIp] = useState('');
  const [scanType, setScanType] = useState('simple');
  const [output, setOutput] = useState('');
  const [error, setError] = useState('');

  const handleScan = () => {
    if (!ip) {
      setError('Please enter an IP address.');
      return;
    }

    setError('');
    setOutput('Scanning...');

    axios.post('http://localhost:5000/nmap', { ip, scan_type: scanType })
      .then(response => {
        setOutput(response.data.output);
      })
      .catch(err => {
        setError('Error running Nmap scan.');
        setOutput('');
        console.error(err);
      });
  };

  return (
    <div className="feature-container">
      <h2>Nmap Scanner</h2>
      <div>
        <label>IP Address:</label>
        <input
          type="text"
          value={ip}
          onChange={(e) => setIp(e.target.value)}
          placeholder="e.g., 192.168.1.1"
        />
      </div>
      <div>
        <label>Scan Type:</label>
        <select value={scanType} onChange={(e) => setScanType(e.target.value)}>
          <option value="simple">Simple Scan</option>
          <option value="version">Version Detection</option>
        </select>
      </div>
      <button onClick={handleScan}>Run Scan</button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {output && <pre>{output}</pre>}
    </div>
  );
};

export default NmapScanner;
