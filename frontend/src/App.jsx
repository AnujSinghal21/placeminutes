import { useState } from 'react'
import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Home from './components/Home';
import Insights from './components/Insights';

function App() {
  const [godMode, setgodMode] = useState(0);
  
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li><Link to="/"></Link></li>
            <li><Link to="/home">Home</Link></li>
            <li><Link to="/insights">Insights</Link></li>
          </ul>
        </nav>

        <Routes>
          {/* {/* <Route path="/" element={<Home />} /> */}
          <Route path="/" element={<Home godMode/>} />
          <Route path="/home" element={<Home godMode/>} />
          <Route path="/Insights" element={<Insights />} /> 
        </Routes>
      </div>
    </Router>
  )
}

export default App
