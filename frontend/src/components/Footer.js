import React from 'react';
import {Text, Container} from 'atomize';

const Footer = () => {
  return (
    <Container
      pos="relative"
      h="100%"
      bottom="0">
      <Text
        textSize="body"
        pos="relative"
        p="0"
        textAlign="center">
        2021 by zifter
      </Text>
    </Container>
  );
};

export default Footer;
