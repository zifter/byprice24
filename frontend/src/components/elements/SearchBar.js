import React, {useState} from 'react';
import {useLocation, useNavigate} from 'react-router-dom';
import {
  Button,
  Input,
  Icon,
  Div,
  Container,
} from 'atomize';
import axios from 'axios';
import PropTypes from 'prop-types';
import Modal from './Modal';

const SearchBar = ({searchInModalWindow, setSearchInModalWindow}) => {
  const search = useLocation().search;
  const initialQuery = new URLSearchParams(search).get('q');
  const [query, setQuery] = useState(initialQuery);
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setSearchInModalWindow([]);
    if (query) {
      navigate({
        pathname: '/search',
        search: `?q=${query}`,
      });
    }
  };

  const handleOnChange = (e) => {
    setQuery(e.target.value);
    const url = '/api/v1/search-autocomplete/products?query=' + query;

    axios
        .get(url)
        .then((response) => {
          console.log('got', response.data);
          setSearchInModalWindow([]);
          setSearchInModalWindow(response.data);
        }).catch(function(error) {
          setSearchInModalWindow([]);
          console.log(error);
        }).finally(function(error) {
        });
  };

  return (
    <Container
      m={{l: {xl: '70px', xs: '0'}}}
      pos="relative"
      p="0"
      h="3rem">
      <form
        name="searchform"
        className="search-form"

        onSubmit={handleSubmit}>
        <Input
          id="input-search"
          placeholder="Искать"
          value={query}
          autocomplete="off"
          onClick={handleOnChange}
          onChange={handleOnChange}
          suffix={
            <Button
              pos="absolute"
              bg="warning600"
              hoverBg="warning700"
              w="3rem"
              top="0"
              right="0"
              rounded={{r: 'md'}}
            >
              <Icon
                name="Search"
                size="20px"
                color="white"
                cursor="pointer"
              />
            </Button>
          }
        />

        <Div pos="absolute"
          top="3rem"
          h="100%"
          w="100%"
          rounded="md"
          bottom="0rem">
          <Modal searchInModalWindow={searchInModalWindow}
            setSearchInModalWindow={setSearchInModalWindow}/>
        </Div></form>
    </Container>
  );
};

SearchBar.propTypes = {
  searchInModalWindow: PropTypes.array,
  setSearchInModalWindow: PropTypes.function,
};

export default SearchBar;
