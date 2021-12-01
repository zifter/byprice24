import React from 'react';
import './App.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import SearchBar from './pages/components/SearchBar.js';
import Home from './pages/Home.js';
import Search from './pages/Search.js';
import Product from './pages/Product.js';

function App() {
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
