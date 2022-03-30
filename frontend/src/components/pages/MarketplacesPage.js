import React, {useEffect, useState} from 'react';
import {
  Row, Col, Image,
  Text, Div,
} from 'atomize';
import {Link} from 'react-router-dom';
import axios from 'axios';
import PropTypes from 'prop-types';

const Marketplace = ({market}) => {
  return (
    <Div
      border="0.3px solid"
      borderColor="gray400"
      rounded="sm"
      w="12rem"
      h='5rem'
      hoverShadow="3"
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
            w='80%'
            textWeight='400'
            m={{l: '1rem'}}
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

const Marketplaces = ({listOfMarketplace}) => {
  return (
    <Row w="10rem">
      {
          listOfMarketplace.map((market, i) =>
          <Col size={{xs: 12, lg: 12}}
            key={market.domain}
          >
            <Marketplace market={market}/>

          </Col>)
      }
    </Row>
  );
};
Marketplaces.propTypes = {
    listOfMarketplace: PropTypes.array,
};

const MarketplaceTab = () => {
  const [listOfMarketplace, setListOfMarketplace] = useState([]);
  //
  // const recentlyViewed =
  //     JSON.parse(localStorage.getItem('recentlyViewed'));
  //
  // const listIds = [];
  // if (recentlyViewed) {
  //   for (let el = 0; el < recentlyViewed['products'].length; el ++) {
  //     listIds.push(recentlyViewed['products'][el]['id']);
  //   }
  // }

  const hook = () => {
    const url = '/api/v1/marketplaces';

    axios
        .get(url)
        .then((response) => {
          console.log('got', response.data);
            setListOfMarketplace(response.data);
        }).catch(function(error) {
          console.log(error);
        });
  };
  useEffect(hook, []);
  return (
    <Row minH="83vh">
      <Row m={{b: '1rem'}}>
        <Text
          textSize='title'
          m={{t: '2rem', l: '0.5rem'}}>
            Магазины
        </Text>
      </Row>
      <Marketplaces
        listOfMarketplace={listOfMarketplace}/>
    </Row>
  );
};

export default MarketplaceTab;
