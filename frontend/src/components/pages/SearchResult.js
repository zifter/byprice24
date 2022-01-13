import React from 'react';
import PropTypes from 'prop-types';
import {useEffect, useState} from 'react';
import {useLocation} from 'react-router-dom';
import axios from 'axios';
import SearchProductResult from './elements/SearchProductResult.js';
import {
  Container, Div,
  Text, Dropdown, Anchor,
} from 'atomize';
import ReactPaginate from 'react-paginate';

const ResultBody = ({searchResult}) => {
  return (
    <ul>
      {
        searchResult.map((item, i) =>
          <li key={item.id} className="item">
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
      textSize="heading"
      textAlign='center'>
      ¯\_(ツ)_/¯
    </Text>
  );
};

const SearchResultTabs = ({count, searchResult}) => {
  const [activeTab, setActiveTab] = useState('productTab');

  const handleProductTab= () => {
    // update the state to tab1
    setActiveTab('productTab');
  };
  return (
    <Div>
      <div className="tab">
        <button className={activeTab === 'productTab' ?
          'active': 'inactinve'}
        onClick={handleProductTab}>Товары ({count})</button>
      </div>
      <div id="product-tab" className={activeTab === 'productTab' ?
          'tabcontent-expanded': 'tabcontent-collapsed'}>
        {searchResult.length > 0 ?
        <ResultBody searchResult={searchResult} /> :
        <ResultIsEmpty />
        }
      </div>

    </Div>
  );
};

SearchResultTabs.propTypes = {
  count: PropTypes.string.isRequired,
  searchResult: PropTypes.array,
};


const SearchResult = () => {
  const [countResult, setCountResult] = useState(0);
  const [searchResult, setSearchResult] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const search = useLocation().search;
  const query = new URLSearchParams(search).get('q');

  // Pagination
  const [page, setPage] = useState(1);
  const handlePageClick = (e) => {
    const selectedPage = e.selected;
    setPage(selectedPage + 1);
  };
  // Ordering
  const [showOrderingDropdown, setShowOrderingDropdown] = useState(false);
  const [orderingType, setOrderingType] = useState('По умолчанию');

  const handleOrderingByPriceAsc = () => {
    setOrderingType('По цене ↑');
  };
  const handleOrderingByPriceDesc = () => {
    setOrderingType('По цене ↓');
  };

  const handleOrderingDefault = () => {
    setOrderingType('По умолчанию');
  };

  const hook = () => {
    let ordering;
    if (orderingType === 'По цене ↑') {
      ordering = 'price_asc';
    } else if (orderingType === 'По цене ↓') {
      ordering = 'price_desc';
    } else {
      ordering = 'relevance';
    }
    const url = '/api/v1/search/products?query=' + query +
        '&page=' + page +'&ordering=' + ordering;
    console.log('request', url);

    axios
        .get(url)
        .then((response) => {
          console.log('got', response.data);
          setSearchResult(response.data.results);
          setCountResult(response.data.count);
        }).catch(function(error) {
          console.log(error);
        }).finally(function(error) {
          setIsLoading(true);
        });
  };

  useEffect(hook, [query]);
  useEffect(hook, [page]);
  useEffect(hook, [orderingType]);

  return (
    <Container
      h="100%"
    >
      <Text
        tag="h1"
        textSize="heading"
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
      <Div d={'flex'} justify={'right'}>
        <Dropdown
          w="fit-content"
          isOpen={showOrderingDropdown}
          onClick={() =>
            setShowOrderingDropdown( !showOrderingDropdown)
          }
          menu={ <Div p={{x: '1rem', y: '0.5rem'}}>

            <Anchor
              d="block"
              p={{y: '0.25rem'}}
              onClick={handleOrderingDefault}>
        По умолчанию
            </Anchor>
            <Anchor
              d="block"
              p={{y: '0.25rem'}}
              onClick={handleOrderingByPriceDesc}>
        По цене ↓
            </Anchor>
            <Anchor
              d="block"
              p={{y: '0.25rem'}}
              onClick={handleOrderingByPriceAsc}>
        По цене ↑
            </Anchor>
          </Div>}
        >
          {orderingType}
        </Dropdown>
      </Div>
      <SearchResultTabs count={countResult} searchResult={searchResult}/>
      <ReactPaginate
        previousLabel={'<'}
        nextLabel={'>'}
        breakLabel={'...'}
        breakClassName={'break-me'}
        pageCount={Math.ceil(countResult / 20)}
        pageRangeDisplayed={3}
        marginPagesDisplayed={1}
        onPageChange={handlePageClick}
        containerClassName={'pagination'}
        subContainerClassName={'pages pagination'}
        activeClassName={'active'}/>
    </Container>
  );
};

export default SearchResult;
