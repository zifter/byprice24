import React, {useEffect} from 'react';
import './App.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import Header from './components/Header.js';
import Footer from './components/Footer.js';
import Index from './components/pages/Index.js';
import SearchResult from './components/pages/SearchResult.js';
import ProductDetails from './components/pages/ProductDetails.js';
import ReactGA from 'react-ga';
import {
  ThemeProvider,
  DefaultTheme,
  StyleReset,
} from 'atomize';


function App() {
  useEffect(() => {
    ReactGA.initialize('G-R18TXE65QV',
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
        <ThemeProvider theme={DefaultTheme}>
          <StyleReset />
          <Header/>
          <Routes>
            <Route path="/" element={<Index />} />
            <Route path="/search" element={<SearchResult />} />
            <Route path="/products/:id" element={<ProductDetails />}/>
          </Routes>
          <Footer/>
        </ThemeProvider>
      </BrowserRouter>
    </div>
  );
}

export default App;
