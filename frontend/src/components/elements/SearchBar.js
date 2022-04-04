import React, {useState} from 'react';
import Modal from './Modal';
import {useDispatch} from 'react-redux';
import {setModal} from '../../redux/appReducer';
import {useLocation, useNavigate} from 'react-router-dom';
import {getAutoCompleteSearch} from '../../redux/productsReducer';
import {
  Button,
  Input,
  Icon,
  Div,
  Container,
} from 'atomize';

const SearchBar = () => {
  const search = useLocation().search;
  const initialQuery = new URLSearchParams(search).get('q');
  const [query, setQuery] = useState(initialQuery);
  const navigate = useNavigate();
  const dispatch = useDispatch();

  const handleSubmit = (e) => {
    e.preventDefault();
    e.stopPropagation();
    dispatch(setModal(false));
    if (query) {
      navigate({
        pathname: '/search',
        search: `?q=${query}`,
      });
    }
  };

  const handleOnChange = (e) => {
    setQuery(e.target.value);
    dispatch(getAutoCompleteSearch(query));
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
          <Modal />
        </Div></form>
    </Container>
  );
};

export default SearchBar;
