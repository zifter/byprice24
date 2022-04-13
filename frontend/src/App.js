import React, {useEffect, useState} from 'react';
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
  const [searchInModalWindow, setSearchInModalWindow] = useState([]);
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
          bg="info600"
          maxW={{xs: 'auto', md: '100vw'}}
          className="app-header"
        >
          <HeaderBar searchInModalWindow={searchInModalWindow}
            setSearchInModalWindow={setSearchInModalWindow}/>
        </Container>

        <Container
          className={searchInModalWindow.length ?
              'app-main' : 'app-main_active'}
          maxW={{xs: 'auto', md: '100vw'}}
          onClick={()=>{
            setSearchInModalWindow([]);
          }}
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
            className="app-footer"
            bg="gray200"
            maxW={{xs: 'auto', md: '100vw'}}
          >
            <Footer/>
          </Container>
        </Container>
      </ThemeProvider>
    </BrowserRouter>
  );
}

export default App;
