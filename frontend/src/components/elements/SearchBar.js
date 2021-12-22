import React from 'react';
import {useState} from 'react';
import {useNavigate} from 'react-router-dom';
import {
  Button,
} from 'atomize';


const SearchBar = () => {
  const [query, setQuery] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    e.stopPropagation();
    navigate({
      pathname: '/search',
      search: `?q=${query}`,
    });
  };

  const handleOnChange = (e) => {
    setQuery(e.target.value);
  };


  return (
    <div>
      <div className="form-row">

        <form name="searchform" className="search-form" onSubmit={handleSubmit}>
          <input
            type="text"
            autoFocus
            placeholder="Что будете искать?"
            onChange={handleOnChange}
            className="ui-autocomplete-input"
            autoComplete="off"/>

          <Button bg="info700" type="submit">
          Искать
          </Button>
        </form>
      </div>
    </div>
  );
};

export default SearchBar;
