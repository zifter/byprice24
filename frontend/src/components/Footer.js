import React from 'react';
import {Text, Container,
  Col, Row, Anchor} from 'atomize';


const Footer = () => {
  return (
    <Container
      pos="relative"
      h="100%"
      bottom="0">
      <Row>

        <Col size={2}>
          <Text
            textSize="body"
            pos="relative"
            p="0"
            textAlign="center">
            2021 by zifter

          </Text>
        </Col>
        <Col size={5}>
          <Anchor
            href="/disclaimer"
            d="block"
            m={{b: '1rem'}}
          >
            <Text
              textSize="body"
              pos="relative"
              p="0"
              textAlign="left"
              textColor="black">
              Правовая информация.
            </Text>
          </Anchor>
        </Col>
        <Col>
          <Anchor
            href="/contacts"
            d="block"
            m={{b: '1rem'}}
          >
            <Text
              textSize="body"
              pos="relative"
              p="0"
              textAlign="left"
              textColor="black">
              Свяжитесь с нами:
              контакты
            </Text>
          </Anchor>
        </Col>
      </Row>

    </Container>
  );
};

export default Footer;
