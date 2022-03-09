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
import DisclaimerPage from './components/pages/DisclaimerPage';
import Contacts from './components/pages/Contacts';

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
          pos="absolute"
          bg="info600"
          maxW={{xs: 'auto', md: '100vw'}}
          h="4rem"
        >
          <HeaderBar/>
        </Container>

        <Container
          d="flex"
          p="0"
          flexDir="column"
          justify="space-between"
          pos="absolute"
          top="4rem"
          bottom="0rem"
          textAlign="center"
          maxW={{xs: 'auto', md: '100vw'}}
        >
          <Routes>
            <Route exact path="/" element={<Index />} />
            <Route exact path="/search" element={<SearchResult />} />
            <Route exact path="/contacts" element={<Contacts />} />
            <Route exact path="/products/:id" element={<ProductPage />}/>
            <Route exact path="/404" element={<NotFound />}/>
            <Route path="*" element={<Navigate replace to="/404" />} />
            <Route exact path="/disclaimer" element={<DisclaimerPage />} />
          </Routes>
          <Container
            align="flex-end"
            bg="gray200"
            p="0"
            h="3rem"
            maxW={{md: '100vw'}}
            textAlign="center"
          >
            <Footer/>
          </Container>
        </Container>
      </ThemeProvider>
    </BrowserRouter>
  );
}

export default App;
