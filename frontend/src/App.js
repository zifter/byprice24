import React, {useEffect} from 'react';
import './App.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import HeaderBar from './components/HeaderBar.js';
import Footer from './components/Footer.js';
import Index from './components/pages/Index.js';
import SearchResult from './components/pages/SearchResult.js';
import ProductDetails from './components/pages/ProductDetails.js';
import ReactGA from 'react-ga';
import {
  ThemeProvider,
  DefaultTheme,
  StyleReset,
  Container,
} from 'atomize';

const theme = {
  ...DefaultTheme,
  fontFamily: {
    primary: 'Mulish,Helvetica Neue,Helvetica,Arial,Roboto,sans-serif',
  },
};

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
    <BrowserRouter>
      <ThemeProvider theme={theme}>
        <StyleReset />
        <Container
          pos="fixed"
          bg="info600"
          maxW={{xs: 'auto', md: '100vw'}}
          h="4rem"
        >
          <HeaderBar/>
        </Container>

        <Container
          pos="absolute"
          top="4rem"
          bottom="1rem"
          textAlign="center"
          maxW={{xs: 'auto', md: '100vw'}}
        >
          <Routes>
            <Route path="/" element={<Index />} />
            <Route path="/search" element={<SearchResult />} />
            <Route path="/products/:id" element={<ProductDetails />}/>
          </Routes>
        </Container>

        <Container
          pos="fixed"
          bottom="0"
          bg="gray200"
          h="4rem"
          maxW={{xs: 'auto', md: '100vw'}}
          textAlign="center"
        >
          <Footer/>
        </Container>
      </ThemeProvider>
    </BrowserRouter>
  );
}

export default App;
