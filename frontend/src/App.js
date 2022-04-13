import React, {useEffect} from 'react';
import './App.css';
import {
  BrowserRouter,
} from 'react-router-dom';
import HeaderBar from './components/HeaderBar.js';
import ReactGA from 'react-ga';
import {
  ThemeProvider,
  StyleReset,
  Container,
} from 'atomize';
import MainPage from './components/pages/MainPage';

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
          bg="info600"
          maxW={{xs: 'auto', md: '100vw'}}
          className="app-header"
        >
          <HeaderBar />
        </Container>
        <MainPage/>
      </ThemeProvider>
    </BrowserRouter>
  );
}

export default App;
