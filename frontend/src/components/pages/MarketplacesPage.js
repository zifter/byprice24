import React, {useEffect} from 'react';
import {
  Row, Col, Image,
  Text, Div,
} from 'atomize';
import PropTypes from 'prop-types';
import './MarketplacesPage.css';
import {useDispatch, useSelector} from 'react-redux';
import {getMarketPlaces} from '../../redux/marketPlaceReducer';

const Marketplace = ({market}) => {
  return (
    <Div
      border="0.3px solid"
      borderColor="gray400"
      rounded="sm"
      w="18rem"
      h='7rem'
      hoverShadow="3"
      className="marketplace-item"
      pos='relative'>
      <Image
        src={market.logo_url}
        w="3rem"
        maxH="3rem"
        m={{t: '0.5rem'}}
      />

      <a href={`${market.domain}`}>
        <Text
          textSize='paragraph'
          textAlign='left'
          w='80%'
          textWeight='600'
          m={{l: '1rem'}}
          textColor='black'>
          {market.domain}
        </Text>
      </a>
      <Div
        pos='absolute'
        bottom='0'>

        <Text
          textSize='paragraph'
          textAlign='left'
          w='100%'
          textWeight='400'
          textTransform="capitalize"
          textColor='gray900'
        >
          {market.description}
        </Text>
      </Div>
    </Div>
  );
};
Marketplace.propTypes = {
  market: PropTypes.shape({
    domain: PropTypes.string.isRequired,
    description: PropTypes.string,
    logo_url: PropTypes.string.isRequired,
  }),
};

const Marketplaces = () => {
  const listOfMarketplace = useSelector((state)=>state.market.marketPlaces);
  return (
    <Row w="100%"
      m={{l: '140px', t: '40px', r: '80px', b: '40px'}}
    >
      {
        listOfMarketplace.map((market, i) =>
          <Col size={{xs: 12, lg: 4}}
            key={market.domain}
            maxH="7rem"
          >
            <Marketplace market={market}/>

          </Col>)
      }
    </Row>
  );
};

const MarketplaceTab = () => {
  const isLoading = useSelector((state) => state.app.isLoading);
  const dispatch = useDispatch();
  const hook = () => {
    dispatch(getMarketPlaces());
  };
  useEffect(hook, []);
  return (<>
    {isLoading &&
      <Text
        tag="h1"
        textSize="heading"
        textAlign={{xs: 'center'}}>
          Загрузка...
      </Text>
    }
    <Row minH="83vh">
      <Marketplaces />
    </Row>
  </>
  );
};

export default MarketplaceTab;
