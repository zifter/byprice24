import {setError, setLoaderStatus} from './appReducer';
import {api} from './api';

const initialState = {
  marketPlaces:
    [
      {
        description: '',
        domain: '',
        logo_url: '',
      },
    ],
};
const SET_MARKET_PLACES = 'SET_MARKET_PLACES';

export const marketPlaceReducer = (state = initialState, action) => {
  switch (action.type) {
    case SET_MARKET_PLACES:
      return {...state, marketPlaces: action.data};
    default:
      return state;
  }
};

export const setMarketPacesAC = (data) =>({
  type: SET_MARKET_PLACES,
  data,
});

export const getMarketPlaces = () => async (dispatch)=> {
  try {
    dispatch(setLoaderStatus(true));
    const res = await api.getMarketPlaces();
    dispatch(setMarketPacesAC(res.data));
  } catch (error) {
    console.log(error);
    dispatch(setError(error));
  } finally {
    dispatch(setLoaderStatus(false));
  }
};


