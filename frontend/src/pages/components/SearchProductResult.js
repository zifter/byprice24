import React from 'react';
import PropTypes from 'prop-types';
import {Link} from 'react-router-dom';

const SearchProductResult = (product) => {
  return (
    <div>
      <Link to={`/products/${product.id}`}>{ product.name }</Link>
    </div>
  );
};

SearchProductResult.propTypes = {
  id: PropTypes.string.isRequired,
  name: PropTypes.string.isRequired,
};

export default SearchProductResult;
