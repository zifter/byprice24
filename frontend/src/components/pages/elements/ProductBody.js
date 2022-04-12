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
        <Col size={{lg: 3, xs: 12}}>
          <Image
            src={productData.preview_url}
            w="14rem"
          />
        </Col>
        <Col size={{lg: 4, xs: 12}}>
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
              textWeight={400}
              textAlign='left'>
              { productData.description }
            </Text>

          </Div>
        </Col>
      </Row>
      <Row>
        <Div p={{t: '2rem',
          l: {lg: '3.5rem'},
          b: {xs: '1rem'}}}>
          <Col size={12}>
            <Text
              tag='h2'
              textSize={'subheader'}
              textAlign={{lg: 'left', xs: 'center'}}>
              Доступен в следующих магазинах:
            </Text>
          </Col>
        </Div>
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
