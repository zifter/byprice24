import React, {useEffect} from 'react';
import {
  Row, Col, Image,
  Text, Div, Container,
} from 'atomize';
import {Link} from 'react-router-dom';
import PropTypes from 'prop-types';
import {useDispatch, useSelector} from 'react-redux';
import {getPopularProducts} from '../../../../redux/productsReducer';

const PopularProduct = ({product}) => {
  return (
    <Div
      border='0.3px solid'
      borderColor='gray400'
      rounded='sm'
      h='12rem'
      hoverShadow='3'
      pos='relative'>
      <Image
        src={product.preview_url}
        w='5rem'
        maxH='5rem'
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
            textTransform='capitalize'
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
PopularProduct.propTypes = {
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

const PopularProducts = ({popularProducts}) => {
  return (
    <Row w='100%'>
      {
        popularProducts.map((product, i) =>
          <Col size={{xs: 12, lg: 3}}
            key={product.id}
          >
            <PopularProduct product={product}/>

          </Col>)
      }
    </Row>
  );
};
PopularProducts.propTypes = {
  popularProducts: PropTypes.array,
};

const PopularTab = () => {
  const popularProducts = useSelector((state) =>
    state.products.popularProducts);
  const dispatch = useDispatch();

  const hook = () => {
    dispatch(getPopularProducts());
  };
  useEffect(hook, []);
  return (
    <Container
      minH="83vh">
      <Row>
        <Row m={{b: '1rem'}}>
          <Text
            textSize='title'
            m={{t: '2rem', l: '0.5rem'}}>
            Популярные товары
          </Text>
        </Row>
        <PopularProducts
          popularProducts={popularProducts}/>
      </Row>
    </Container>
  );
};

export default PopularTab;
