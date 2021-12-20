import React, {useEffect} from 'react';
import './App.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import SearchBar from './pages/components/SearchBar.js';
import Home from './pages/Home.js';
import Search from './pages/Search.js';
import Product from './pages/Product.js';
import ReactGA from 'react-ga';

function App() {
  useEffect(() => {
    ReactGA.initialize(process.env.GOOGLE_ANALYTICS_TRACKING_ID,
        {testMode: process.env.NODE_ENV === 'test'});
    // To Report Page View
    ReactGA.pageview(window.location.pathname + window.location.search);
  }, []);

  useEffect(() => {
    console.log(window.location.pathname);
  });
  return (
    <div>
      <BrowserRouter>
        <SearchBar/>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/search" element={<Search />} />
          <Route path="/products/:id" element={<Product />}/>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
