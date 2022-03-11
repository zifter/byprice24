import React, {useState} from 'react';
import {useNavigate} from 'react-router-dom';
import {
  Button,
  Input,
  Icon,
  Container,
} from 'atomize';


const SearchBar = () => {
  const [query, setQuery] = useState(sessionStorage.getItem('query'));
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    e.stopPropagation();
    if (query) {
      sessionStorage.setItem('query', query);
      navigate({
        pathname: '/search',
        search: `?q=${query}`,
      });
    }
  };

  const handleOnChange = (e) => {
    setQuery(e.target.value);
  };


  return (
    <Container
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
    </Container>
  );
};

export default SearchBar;
