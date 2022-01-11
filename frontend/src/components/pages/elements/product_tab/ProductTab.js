import React from 'react';
import PriceTab from './tabs/PriceTab';
import PropTypes from 'prop-types';
import {
  Div, Row, Col,
  Container, Text,
} from 'atomize';

const ProductTab = ({productData}) => {
  console.log(productData.product_pages[0].marketplace);
  return (
    <Container>
      <Div bg='rgb(228, 239, 244)' rounded='xl'>
        <Row >
          <Col size={12} d={'flex'} justify={'center'}>
            <ul className="nav">
              <li>
                <Text textSize={'paragraph'}>
                Цена
                </Text>
              </li>
            </ul>
          </Col>
        </Row>
      </Div>
      <Div>
        <PriceTab productData={productData} />
      </Div>

    </Container>
  );
};
ProductTab.propTypes = {
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

export default ProductTab;
