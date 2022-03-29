import React from 'react';
import {
  Container,
} from 'atomize';
import RecentlyViewedTab from './elements/RecentlyViewedProducts';


function Index() {
  return (
    <Container
      minH="83vh"

    >
      <RecentlyViewedTab />
    </Container>
  );
}

export default Index;
