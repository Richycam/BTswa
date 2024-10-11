// src/components/Tcpdump.js

import React, { useState } from 'react';
import axios from 'axios';

const Tcpdump = () => {
  const [output, setOutput] = useState('');
  const [error, setError] = useState('');

  const handleTcpdump = () => {
    setError('');
    setOutput('Running TCPDump...');

    axios.get('http://localhost:5000/tcpdump')
      .then(response => {
        setOutput(response.data.output);
      })
      .catch(err => {
        setError('Error running TCPDump.');
        setOutput('');
        console.error(err);
      });
  };

  return (
    <div className="feature-container">
      <h2>TCPDump</h2>
      <button onClick={handleTcpdump}>Run TCPDump</button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {output && <pre>{output}</pre>}
    </div>
  );
};

export default Tcpdump;
