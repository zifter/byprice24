import React from 'react';
import PropTypes from 'prop-types';
import {useEffect, useState} from 'react';
import {useLocation} from 'react-router-dom';
import axios from 'axios';
import SearchProductResult from './elements/SearchProductResult.js';
import {
  Div,
  Text,
} from 'atomize';


const ResultBody = ({searchResult}) => {
  return (
    <ul>
      {
        searchResult.map((item, i) =>
          <li key={item.id}>
            {
              <SearchProductResult product={item}/>
            }
          </li>)
      }
    </ul>
  );
};

ResultBody.propTypes = {
  searchResult: PropTypes.array,
};


const ResultIsEmpty = ( ) => {
  return (
    <Text
      tag="h1"
      textSize="display1"
      textAlign='center'>
      ¯\_(ツ)_/¯
    </Text>
  );
};


const SearchResult = () => {
  const [searchResult, setSearchResult] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const search = useLocation().search;
  const query = new URLSearchParams(search).get('q');

  const hook = () => {
    const url = '/api/v1/search/products?query=' + query;
    console.log('request', url);

    axios
        .get(url)
        .then((response) => {
          console.log('got', response.data);
          setSearchResult(response.data.results);
        }).catch(function(error) {
          console.log(error);
        }).finally(function(error) {
          setIsLoading(true);
        });
  };

  useEffect(hook, [query]);

  return (
    <Div>
      <Text
        tag="h1"
        textSize="display1"
        m={{b: '4rem', t: '1rem'}}
        textAlign={{xs: 'center', lg: 'left'}}>
          Результаты поиска для &quot;{query}&quot;
      </Text>

      {!isLoading &&
            <Text
              tag="h1"
              textSize="heading"
              textAlign={{xs: 'center'}}>
              Загрузка...
            </Text>
      }
      {searchResult.length > 0 ?
        <ResultBody searchResult={searchResult} /> :
        <ResultIsEmpty />
      }

    </Div>
  );
};

export default SearchResult;
