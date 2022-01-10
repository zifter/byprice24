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
    <Div>
      <Text
        textSize="display1"
        textAlign='center'>
        { productData.name }
      </Text>
      <Row>
        <Col>
          <Image
            src={productData.preview_url}
            h="100"
            w="100"
          />
        </Col>
      </Row>
      <Text
        textSize="body"
        textAlign='left'>
        { productData.description }
      </Text>
    </Div>
  );
};

ProductBody.propTypes = {
  productData: PropTypes.shape({
    id: PropTypes.number.isRequired,
    name: PropTypes.string.isRequired,
    description: PropTypes.string.isRequired,
    preview_url: PropTypes.string.isRequired,
  }),
};

export default ProductBody;
