import React, {useEffect} from 'react';
import './App.css';
import {
  BrowserRouter,
  Routes,
  Route,
  Navigate,
} from 'react-router-dom';
import HeaderBar from './components/HeaderBar.js';
import Footer from './components/Footer.js';
import Index from './components/pages/Index.js';
import SearchResult from './components/pages/SearchResult.js';
import ProductPage from './components/pages/ProductPage.js';
import NotFound from './components/pages/NotFound.js';

import ReactGA from 'react-ga';
import {
  ThemeProvider,
  StyleReset,
  Container,
} from 'atomize';

const theme = {
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
            <Route exact path="/" element={<Index />} />
            <Route exact path="/search" element={<SearchResult />} />
            <Route exact path="/products/:id" element={<ProductPage />}/>
            <Route exact path="/404" element={<NotFound />}/>
            <Route path="*" element={<Navigate replace to="/404" />} />
          </Routes>
        </Container>

        <Container
          pos="fixed"
          bottom="0"
          bg="gray200"
          h="1.5rem"
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
