import {api} from './api';
import {setError, setLoaderStatus} from './appReducer';

const SET_SEARCH_PRODUCTS = 'SET_SEARCH_PRODUCTS';
const SET_CURRENT_PRODUCT = 'SET_CURRENT_PRODUCT';
const SET_RECENTLY_VIEWED_PRODUCT = 'SET_RECENTLY_VIEWED_PRODUCT';

const initialState = {
  count: 0,
  next_page: 0,
  previous_page: 0,
  results:
    [
      {
        id: 0,
        name: '',
        category: '',
        marketplaces_count_instock: 0,
        description: '',
        preview_url: '',
        min_offer: {
          price: '0',
          price_currency: '0',
        },

        product_pages:
          [
            {
              marketplace: {
                domain: '',
                logo_url: '',
                description: '',
              },
              description: '',
              domain: '',
              logo_url: '',
              name: '',
              product_states: {
                created: '',
                price: '',
                price_currency: '',
                rating: 0,
              },
              availability: '',
              created: '',
              price: '',
              price_currency: '',
              rating: 0,
              review_count: 0,
              url: '',
            },
          ],
      },
    ],
  recentlyViewedProducts:
    [
      {
        id: 0,
        name: '',
        category: '',
        preview_url: '',
        min_offer: {
          price: '0',
          price_currency: '0',
        },
      },
    ],
};

export const productsReducer = (state = initialState, action) => {
  switch (action.type) {
    case SET_SEARCH_PRODUCTS: {
      return {...state, ...action.data};
    }
    case SET_CURRENT_PRODUCT: {
      if (state.results[0].id === 0) {
        return {...state, results: [action.data]};
      }
      if (action.data.id === 0) return initialState;
      const copyResults =
        state.results.map((item)=>(item.id === action.data.id ?
                {...item, id: action.data.id,
                  category: action.data.category,
                  description: action.data.description,
                  name: action.data.name,
                  preview_url: action.data.preview_url,
                  product_pages: action.data.product_pages} :
                item));
      return {...state, results: copyResults};
    }
    case SET_RECENTLY_VIEWED_PRODUCT: {
      return {...state, recentlyViewedProducts: action.data};
    }
    default:
      return state;
  }
};

export const setProductsAC = (data) => ({
  type: SET_SEARCH_PRODUCTS,
  data,
});
export const setCurrentProductsAC = (data) => ({
  type: SET_CURRENT_PRODUCT,
  data,
});
export const setRecentlyViewedProductsAC = (data) => ({
  type: SET_RECENTLY_VIEWED_PRODUCT,
  data,
});

export const getSearchProducts = (query, page, ordering) => async (dispatch)=> {
  try {
    dispatch(setLoaderStatus(true));
    const res = await api.searchProducts(query, page, ordering);
    dispatch(setProductsAC(res.data));
  } catch (error) {
    console.log(error);
    dispatch(setError(error));
  } finally {
    dispatch(setLoaderStatus(false));
  }
};

export const getCurrentProduct = (id) => async (dispatch)=> {
  try {
    dispatch(setLoaderStatus(true));
    const res = await api.searchCurrentProduct(id);
    dispatch(setCurrentProductsAC(res.data));
  } catch (error) {
    console.log(error);
    dispatch(setError(error));
  } finally {
    dispatch(setLoaderStatus(false));
  }
};

export const getRecentlyViewedProducts = (id) => async (dispatch)=> {
  try {
    dispatch(setLoaderStatus(true));
    dispatch(setCurrentProductsAC({id: 0}));
    const res = await api.searchRecentlyViewedProducts(id);
    dispatch(setRecentlyViewedProductsAC(res.data));
  } catch (error) {
    console.log(error);
    dispatch(setError(error));
  } finally {
    dispatch(setLoaderStatus(false));
  }
};
