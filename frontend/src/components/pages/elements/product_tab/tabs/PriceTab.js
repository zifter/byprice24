import React from 'react';
import PropTypes from 'prop-types';
import {
  Div, Row, Col,
  Container, Image,
  Text, Anchor,
  Button, Icon,
} from 'atomize';

const PriceTab = ({productData}) => {
  return (
    <Container>
      {productData.product_pages.map((productPage) => (
        // eslint-disable-next-line react/jsx-key
        <Row>
          <Col size={12}>
            <Div m={{b: '0.5rem', t: '1rem'}}>

              <button type="button" className="collapsible">

                <Row>
                  <Col size={3}>

                    <Row>
                      <Col size={3}>
                        <Image
                          src={productPage.marketplace.logo_url}
                          w={'3rem'} p={'0.1rem'}
                        />
                      </Col>
                      <Col size={8} d={'flex'} align={'center'}>
                        <Icon name="StarSolid" size="1rem"
                          color={'warning800'}/>
                        <Text textSize={'paragraph'} color={'warning800'}>
                          {productPage.product_states.rating}
                        </Text>
                      </Col>
                    </Row>

                  </Col>

                  <Col size={5} textAlign={'left'}>
                    <Text textSize={'subheader'} textWeight={600}>
                      {productPage.name}
                    </Text>
                  </Col>
                  <Col size={2}>

                    <Row>
                      <Col size={12}>
                        <Div d={'flex'} justify={'right'}>
                          {productPage.product_states.price} {' '}
                          {productPage.product_states.price_currency}
                        </Div>
                      </Col>
                    </Row>

                    <Row>
                      <Col size={12}>
                        <Div d={'flex'} justify={'right'}>
                          <Text textSize={'caption'}>
                            {productPage.product_states.availability ===
                            'Availability.InStock' ?
                                <Icon name="Success" size="15px"
                                  color='success800' m={{t: '0.5rem'}}/> :
                                <Icon name="Close" size="15px"
                                  color='danger800' m={{t: '0.5rem'}}/>
                            }
                          </Text>
                        </Div>
                      </Col>
                    </Row>
                  </Col>


                  <Col size={2}>

                    <Div d={'flex'} justify={'right'}>
                      <Anchor href={productPage.url} target="_blank">
                        <Button
                          prefix={
                            <Icon
                              name="EyeSolid"
                              size="16px"
                              color="white"
                              m={{r: '0.5rem'}}
                            />
                          }
                          bg="warning700"
                          hoverBg="warning800"
                          rounded="circle"
                          p={{r: '1.5rem', l: '1rem'}}
                          shadow="3"
                          hoverShadow="4"
                        >
                      Магазин
                        </Button>
                      </Anchor>
                    </Div>

                  </Col>

                </Row>


              </button>
            </Div>
          </Col>
        </Row>
      ))}
    </Container>
  );
};

PriceTab.propTypes = {
  productData: PropTypes.shape({
    id: PropTypes.number.isRequired,
    name: PropTypes.string.isRequired,
    description: PropTypes.string.isRequired,
    preview_url: PropTypes.string.isRequired,
    product_pages: PropTypes.arrayOf(PropTypes.shape({
      marketplace: PropTypes.shape({
        domain: PropTypes.string.isRequired,
        logo_url: PropTypes.string.isRequired,
        description: PropTypes.string.isRequired,
        name: PropTypes.string.isRequired,
      }),
      url: PropTypes.string.isRequired,
      product_states: PropTypes.shape({
        created: PropTypes.string.isRequired,
        price: PropTypes.string.isRequired,
        price_currency: PropTypes.string.isRequired,
        rating: PropTypes.number,
        review_count: PropTypes.number.isRequired,
        availability: PropTypes.string.isRequired,
      }),
    })).isRequired,
  }),
};
export default PriceTab;
