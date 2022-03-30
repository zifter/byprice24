import React, {useEffect, useState} from 'react';
import {
  Row, Col, Image,
  Text, Div,
} from 'atomize';
import {Link} from 'react-router-dom';
import axios from 'axios';
import PropTypes from 'prop-types';

const RecentlyViewedProduct = ({product}) => {
  return (
    <Div
      border="0.3px solid"
      borderColor="gray400"
      rounded="sm"
      h='12rem'
      hoverShadow="3"
      pos='relative'>
      <Image
        src={product.preview_url}
        w="5rem"
        maxH="5rem"
        m={{t: '0.5rem'}}
      />
      {
        <Link to={`/products/${product.id}`}>
          <Text
            textSize='paragraph'
            textAlign='left'
            w='80%'
            textWeight='600'
            m={{l: '1rem'}}
            textColor='black'>
            {product.name.slice(0, 40)}
          </Text>
        </Link>

      }
      <Div
        pos='absolute'
        bottom='0'>
        {
          <Text
            textSize='paragraph'
            textAlign='left'
            w='80%'
            textWeight='400'
            m={{l: '1rem'}}
            textTransform="capitalize"
            textColor='gray900'
          >
            {product.category}
          </Text>
        }
        {
          <Text
            textSize='paragraph'
            textAlign='left'
            textWeight='700'
            m={{l: '1rem'}}
          >
            {product.min_offer.price}  {' '}
            {product.min_offer.price_currency}
          </Text>
        }
      </Div>
    </Div>
  );
};
RecentlyViewedProduct.propTypes = {
  product: PropTypes.shape({
    id: PropTypes.number.isRequired,
    name: PropTypes.string.isRequired,
    preview_url: PropTypes.string.isRequired,
    category: PropTypes.string.isRequired,
    min_offer: PropTypes.shape({
      price: PropTypes.number.isRequired,
      price_currency: PropTypes.string.isRequired,
    }),
  }),
};

const RecentlyViewedProducts = ({recentlyViewedProducts}) => {
  return (
    <Row w='100%'>
      {
        recentlyViewedProducts.slice(0, 4).map((product, i) =>
          <Col size={{xs: 12, lg: 3}}
            key={product.id}
          >
            <RecentlyViewedProduct product={product}/>

          </Col>)
      }
    </Row>
  );
};
RecentlyViewedProducts.propTypes = {
  recentlyViewedProducts: PropTypes.array,
};

const RecentlyViewedTab = () => {
  const [recentlyViewedProducts, setRecentlyViewedProducts] = useState([]);

  const recentlyViewed =
      JSON.parse(localStorage.getItem('recentlyViewed'));

  const listIds = [];
  if (recentlyViewed) {
    for (let el = 0; el < recentlyViewed['products'].length; el ++) {
      listIds.push(recentlyViewed['products'][el]['id']);
    }
  }

  const hook = () => {
    const url = '/api/v1/products?id=' + listIds.join('&id=');
    console.log('request', url);

    axios
        .get(url)
        .then((response) => {
          console.log('got', response.data);
          setRecentlyViewedProducts(response.data);
        }).catch(function(error) {
          console.log(error);
        });
  };
  useEffect(hook, listIds);
  return (
    <Row>
      <Row m={{b: '1rem'}}>
        <Text
          textSize='title'
          m={{t: '2rem', l: '0.5rem'}}>
            Недавно просмотренные
        </Text>
      </Row>
      <RecentlyViewedProducts
        recentlyViewedProducts={recentlyViewedProducts}/>
    </Row>
  );
};

export default RecentlyViewedTab;
