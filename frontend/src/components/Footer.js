import React from 'react';
import {Container,
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
            m={{b: '0rem'}}
            textColor="black"
          >

              Правовая информация

          </Anchor>
        </Col>
        <Col>
          <Anchor
            href="/contacts"
            m={{b: '0rem'}}
            textColor="black"
          >

              Kонтакты

          </Anchor>
        </Col></Row>
      <Col>
        <Anchor
          href="/"
          textColor="black"
        >
            2022 by zifter

        </Anchor>
      </Col>


    </Container>
  );
};

export default Footer;
