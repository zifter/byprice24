import React from 'react';
import {
  Container,
  Text,
} from 'atomize';


const NotFound = () => {
  return (
    <Container minH="83vh">
      <Text
        tag="h1"
        textSize="heading"
        m={{b: '4rem', t: '1rem'}}
        textAlign={{xs: 'center', lg: 'left'}}>
          Не найдено ¯\_(ツ)_/¯
      </Text>
    </Container>
  );
};

export default NotFound;
