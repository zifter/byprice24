import React from 'react';
import PropTypes from 'prop-types';
import {Link} from 'react-router-dom';
import {
  Div,
  Text,
} from 'atomize';

const SearchProductResult = ({product}) => {
  return (
    <Div>
      <Link to={`/products/${product.id}`}>
        <Text
          textSize="body"
          textAlign='left'>
          { product.name }
        </Text>
      </Link>
    </Div>
  );
};

SearchProductResult.propTypes = {
  product: PropTypes.shape({
    id: PropTypes.string.isRequired,
    name: PropTypes.string.isRequired,
  }),
};

export default SearchProductResult;
