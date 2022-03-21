import React, {useState} from 'react';
import {Link, useLocation, useNavigate} from 'react-router-dom';
import {
  Button,
  Input,
  Icon,
  Div,
  Container,
} from 'atomize';
import axios from 'axios';
import PropTypes from 'prop-types';

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
      h="3rem">
      <form
        name="searchform"
        className="search-form"
        onSubmit={handleSubmit}>
        <Input
          placeholder="Искать"
          value={query}
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
      </form>
      <Div pos="absolute"
        top="3rem"
        bottom="0rem">
        {searchInModalWindow && searchInModalWindow.map((t)=>{
          return (<Div
            key={t.id}
            cursor="pointer"
            hoverTextColor="info700"
            p={{x: '1rem', y: '0.75rem'}}
            // border={{ b: index !== 4 && "1px solid" }}
            bg="gray100"
            borderColor="gray400"
            rounded="lg"
          >
            <Link to={`/products/${t.id}`}
              href="https://www.google.com">{t.name}</Link>
          </Div>);
        })
        }
      </Div>
    </Container>
  );
};

SearchBar.propTypes = {
  searchInModalWindow: PropTypes.array,
  setSearchInModalWindow: PropTypes.function,
};

export default SearchBar;
