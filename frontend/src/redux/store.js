
import { applyMiddleware, combineReducers, createStore } from 'redux';
import thunkMiddleware from 'redux-thunk';
import {productsReducer} from "./productsReducer";
import {appReducer} from "./appReducer";


const rootReducer = combineReducers({
    // login: loginReducer,
    products: productsReducer,
    // newPassword: newPasswordReducer,
    app: appReducer,
    // cards: cardsReducer,
})

export const store = createStore(rootReducer, applyMiddleware(thunkMiddleware));

window.store = store
