import React from 'react';
import {useEffect, useState} from 'react';
import {useLocation} from 'react-router-dom';
import axios from 'axios';
import SearchProductResult from './components/SearchProductResult.js';

const Search = () => {
  const [searchResult, setSearchResult] = useState([]);
  const [isLoaded, setIsLoaded] = useState(false);

  const search = useLocation().search;
  const query = new URLSearchParams(search).get('q');

  const hook = () => {
    const url = '/api/v1/search/products?query=' + query;
    console.log('request', url);

    axios
        .get(url)
        .then((response) => {
          console.log('got', response.data);
          setIsLoaded(true);
          setSearchResult(response.data.results);
        });
  };

  useEffect(hook, [query]);

  return (
    <div>
            Show results for - {query}
      {!isLoaded && <div>Загрузка...</div>}


      <h1>Result</h1>
      <ul>
        {
          searchResult.map((result) =>
            <li key={result.id}>
              {
                <SearchProductResult product={result}/>
              }
            </li>)
        }
      </ul>
    </div>
  );
};

export default Search;
