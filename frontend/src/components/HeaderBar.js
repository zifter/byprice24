import React from 'react';
import SearchBar from './elements/SearchBar.js';
import {Container} from 'atomize';

const HeaderBar = () => {
  return (
    <Container
      pos="relative"
      maxW={{xs: 'auto', md: '60vw'}}
      top="0.75rem"
    >
      <SearchBar/>
    </Container>
  );
};

export default HeaderBar;
