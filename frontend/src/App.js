// frontend/src/App.js

import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Banner from './components/Banner';
import Menu from './components/Menu';
import SIEMLink from './components/SIEMLink';
import SIEMDocs from './components/SIEMDocs';
import SetSIEM from './components/SetSIEM';
import NmapScanner from './components/NmapScanner';
import Tcpdump from './components/Tcpdump';
import WorldMap from './components/WorldMap';
import CheckPassword from './components/CheckPassword';
import './App.css'; 

function App() {
  return (
    <Router>
      <div className="App">
        <Banner />
        <Menu />
        <div className="content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/siem-link" element={<SIEMLink />} />
            <Route path="/siem-docs" element={<SIEMDocs />} />
            <Route path="/set-siem" element={<SetSIEM />} />
            <Route path="/nmap" element={<NmapScanner />} />
            <Route path="/tcpdump" element={<Tcpdump />} />
            <Route path="/worldmap" element={<WorldMap />} />
            <Route path="/check-password" element={<CheckPassword />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}


const Home = () => (
  <div className="feature-container">
    <h2>Welcome to Blue Team Swiss Army Knife</h2>
    <p>Select a tool from the menu to get started.</p>
  </div>
);


const NotFound = () => (
  <div className="feature-container">
    <h2>404 - Not Found</h2>
    <p>The page you are looking for does not exist.</p>
  </div>
);

export default App;
