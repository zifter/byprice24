import React from 'react';
import PropTypes from 'prop-types';
import {Link} from 'react-router-dom';
import {
  Div, Row,
  Text, Col, Image,
} from 'atomize';

const SearchProductResult = ({product}) => {
  return (
    <Div
      p={{t: '1rem', b: '1rem'}}
      hoverBg="gray200">
      <Link to={`/products/${product.id}`}
        href="https://www.google.com"
        target="_blank">
        <Row align={'center'}>
          <Col size={{lg: 1, xs: 3}}>
            <Image
              src={product.preview_url}
              h="2.5rem"
              w="2.5rem"
            />
          </Col>
          <Col size={{lg: 9, xs: 4}}>
            <Text
              textSize="paragraph"
              textAlign='left'
              textColor="black"
              textWeight={600}>
              { product.name }
            </Text>
          </Col>
          <Col size={{lg: 2, xs: 5}}>
            <Text
              textSize="paragraph"
              textColor="black"
              textAlign={'right'}
              textWeight="700">
              <span className="span-from-price">От </span>
              { product.min_offer.price } {' '}
              { product.min_offer.price_currency}
            </Text>

          </Col>

        </Row>
      </Link>
    </Div>
  );
};

SearchProductResult.propTypes = {
  product: PropTypes.shape({
    id: PropTypes.string.isRequired,
    name: PropTypes.string.isRequired,
    preview_url: PropTypes.string.isRequired,
    min_offer: PropTypes.shape({
      price: PropTypes.string.isRequired,
      price_currency: PropTypes.string.innerHtml},
    ),
  }),
};

export default SearchProductResult;
