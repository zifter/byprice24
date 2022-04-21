import axios from 'axios';

const instance = axios.create({
  baseURL: '/api/v1/',
});

export const api = {
  searchProducts(query, page, ordering) {
    const url = 'search/products?query=' + query +
      '&page=' + page +'&ordering=' + ordering;
    return instance.get(url);
  },
  searchCurrentProduct(id) {
    const url = 'products/' + id;
    return instance.get(url);
  },
  searchRecentlyViewedProducts(id) {
    const url = 'products?id=' + id.join('&id=');
    return instance.get(url);
  },
  autoCompleteSearchProducts(query) {
    const url = 'search-autocomplete/products?query=' + query;
    return instance.get(url);
  },
  getMarketPlaces() {
    const url = 'marketplaces';
    return instance.get(url);
  },
  searchPopularProducts() {
    const url = 'popular-products';
    return instance.get(url);
  },
};


