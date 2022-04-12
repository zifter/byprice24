import React from 'react';
import SearchBar from './elements/SearchBar.js';
import {
  Container,
  Image,
  Row,
  Col,
  Text,
  Anchor,
} from 'atomize';
import findPrice from './elements/find-price-gold.png';

const HeaderBar = () => {
  return (
    <Container
      pos="relative"
      maxW={{xs: 'auto', md: '60vw'}}
      top="0.75rem"
      m={{l: {xs: '0', lg: '50px', sm: '30px', xl: '70px'}, r: '20px'}}
      p={{l: {xs: '0', sm: '10px'}}}
    >
      <Row>
        <Col size={1} >
          <Anchor
            href="/"
          >
            <Image
              src={findPrice}
              w={{xl: '4rem', xs: '2rem'}}
              m={{t: {xl: '-6px', xs: '6px'}, l: '0px'}}
            />
          </Anchor>
        </Col>
        <Col size={3} >
          <Anchor
            href="/"
          >
            <Text textSize={{xs: 'paragraph', xl: 'heading'}}
              textWeight={'700'}
              textColor="black"
              m={{l: '20px', t: {xs: '5px', xl: '0'}}}
            >
          Findprice.by
            </Text>
          </Anchor>
        </Col>

        <Col size={8}>
          <SearchBar />
        </Col>
      </Row>
    </Container>
  );
};

export default HeaderBar;
