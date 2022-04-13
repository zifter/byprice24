import React from 'react';
import PriceTab from './tabs/PriceTab';
import PropTypes from 'prop-types';
import {
  Div,
  Container,
} from 'atomize';


const ProductTabs = ({productData}) => {
  return (
    <Container>
      <Div>
        <PriceTab productData={productData} />
      </Div>

    </Container>
  );
};
ProductTabs.propTypes = {
  productData: PropTypes.shape({
    id: PropTypes.number.isRequired,
    name: PropTypes.string.isRequired,
    description: PropTypes.string.isRequired,
    preview_url: PropTypes.string.isRequired,
    product_pages: PropTypes.arrayOf(PropTypes.shape({
      marketplace: PropTypes.array.isRequired,
      url: PropTypes.string.isRequired,
      product_states: PropTypes.array.isRequired,
    })).isRequired,
  }),
};

export default ProductTabs;
