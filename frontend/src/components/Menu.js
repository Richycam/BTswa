// frontend/src/components/Menu.js

import React from 'react';
import { NavLink } from 'react-router-dom';
import './Menu.css';

const Menu = () => {
  return (
    <nav className="menu">
      <h2>Blue Team Swiss Army Knife</h2>
      <ul>
        <li>
          <NavLink exact to="/" activeClassName="active">
            Home
          </NavLink>
        </li>
        <li>
          <NavLink to="/siem-link" activeClassName="active">
            SIEM Link
          </NavLink>
        </li>
        <li>
          <NavLink to="/siem-docs" activeClassName="active">
            SIEM Documentation
          </NavLink>
        </li>
        <li>
          <NavLink to="/set-siem" activeClassName="active">
            Set SIEM Tool
          </NavLink>
        </li>
        <li>
          <NavLink to="/nmap" activeClassName="active">
            Run Nmap
          </NavLink>
        </li>
        <li>
          <NavLink to="/tcpdump" activeClassName="active">
            Run TCPDump
          </NavLink>
        </li>
        <li>
          <NavLink to="/worldmap" activeClassName="active">
            World Map
          </NavLink>
        </li>
        <li>
          <NavLink to="/check-password" activeClassName="active">
            Check Password
          </NavLink>
        </li>
      </ul>
    </nav>
  );
};

export default Menu;
