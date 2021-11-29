import React from 'react';
import { useState } from 'react';
import { useNavigate } from "react-router-dom";


function SearchBar() {
    const [query, setQuery] = useState('')
    let navigate = useNavigate();

    const handleSubmit = e => {
        e.preventDefault();
        e.stopPropagation();
        navigate({
            pathname: '/search',
            search: `?q=${query}`,
            });
    };

    const handleOnChange = e => {
        setQuery(e.target.value)
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
                <button type="submit" className="icon-search">Искать</button>
            </form>
        </div>
    </div>
  );
}

export default SearchBar;
