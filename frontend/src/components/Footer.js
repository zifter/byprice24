import React from 'react';
import {Text, Container,
  Col, Row, Anchor} from 'atomize';


const Footer = () => {
  return (
    <Container
      pos="relative"
      p="0"
      top="0rem"
      bottom="0">
      <Row
        d="flex"
        flexDir="row"
        align="center"
        p="0"
      >
        <Col>
          <Anchor
            href="/disclaimer"
            d="block"
            m={{b: '0rem'}}
          >
            <Text
              textSize="body"
              textAlign="center"
              textColor="black">
              Правовая информация
            </Text>
          </Anchor>
        </Col>
        <Col>
          <Anchor
            href="/contacts"
            d="block"
            m={{b: '0rem'}}
          >
            <Text
              textSize="body"
              textAlign="center"
              textColor="black">

              Kонтакты
            </Text>
          </Anchor>
        </Col></Row>
      <Col>
        <Anchor
          href="/"
        >
          <Text
            textSize="body"
            p="0"
            textAlign="center">
            2022 by zifter

          </Text>
        </Anchor>
      </Col>


    </Container>
  );
};

export default Footer;
