import React from 'react';
import Index from './Index';
import Footer from '../Footer';
import NotFound from './NotFound';
import Contacts from './Contacts';
import ProductPage from './ProductPage';
import SearchResult from './SearchResult';
import DisclaimerPage from './DisclaimerPage';
import MarketplaceTab from './MarketplacesPage';
import {setModal} from '../../redux/appReducer';
import {useDispatch, useSelector} from 'react-redux';
import {Navigate, Route, Routes} from 'react-router-dom';
import {
  Container,
} from 'atomize';

function MainPage() {
  const isModalActive = useSelector((state)=>state.app.isModalActive);
  const dispatch = useDispatch();
  const handleOnClick = () => {
    dispatch(setModal(false));
  };
  return (
    <Container
      className={isModalActive ?
      'app-main' : 'app-main_active'}
      maxW={{xs: 'auto', md: '100vw'}}
      onClick={handleOnClick}
    >
      <Routes>
        <Route exact path="/" element={<Index />} />
        <Route exact path="/search" element={<SearchResult />} />
        <Route exact path="/contacts" element={<Contacts />} />
        <Route exact path="/products/:id" element={<ProductPage />}/>
        <Route exact path="/404" element={<NotFound />}/>
        <Route path="*" element={<Navigate replace to="/404" />} />
        <Route exact path="/disclaimer" element={<DisclaimerPage />} />
        <Route exact path="/marketplace" element={<MarketplaceTab />} />
      </Routes>
      <Container
        className="app-footer"
        bg="gray200"
        maxW={{xs: 'auto', md: '100vw'}}
      >
        <Footer/>
      </Container>
    </Container>
  );
}

export default MainPage;
