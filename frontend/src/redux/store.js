import {applyMiddleware, combineReducers, createStore} from 'redux';
import thunkMiddleware from 'redux-thunk';
import {productsReducer} from './productsReducer';
import {appReducer} from './appReducer';
import {marketPlaceReducer} from './marketPlaceReducer';

const rootReducer = combineReducers({
  products: productsReducer,
  app: appReducer,
  market: marketPlaceReducer,
});

export const store = createStore(rootReducer, applyMiddleware(thunkMiddleware));

window.store = store;
