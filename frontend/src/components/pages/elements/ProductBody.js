import React from 'react';
import PropTypes from 'prop-types';

import {
  Div,
  Text,
  Image,
  Row,
  Col,
} from 'atomize';

const ProductBody = ({productData}) => {
  return (
    <Div p={{t: '1rem'}}>
      <Row>
        <Col size={3}>
          <Image
            src={productData.preview_url}
            h="100"
            w="100"
          />
        </Col>
        <Col size={4}>
          <Div p={{t: '2rem'}}>
            <Text
              tag="h1"
              textSize={'title'}
              textAlign='left'>
              { productData.name }
            </Text>
            <Text p={{t: '1rem'}}
              tag='h2'
              textSize={'paragraph'}
              textAlign='left'>
              Доступен в { productData.product_pages.length } магазинах
            </Text>
          </Div>
        </Col>
      </Row>

    </Div>
  );
};

ProductBody.propTypes = {
  productData: PropTypes.shape({
    id: PropTypes.number.isRequired,
    name: PropTypes.string.isRequired,
    description: PropTypes.string.isRequired,
    preview_url: PropTypes.string.isRequired,
    product_pages: PropTypes.array.isRequired,
  }),
};

export default ProductBody;
