const initialState = {
  isLoading: false,
  error: null,
  isModalActive: false,
};
const SET_LOADER_STATUS = 'SET_LOADER_STATUS';
const SET_ERROR = 'SET_ERROR';
const SET_MODAL = 'SET_MODAL';

export const appReducer = (state = initialState, action) => {
  switch (action.type) {
    case SET_LOADER_STATUS:
      return {...state, isLoading: action.status};
    case SET_ERROR:
      return {...state, error: action.error};
    case SET_MODAL:
      return {...state, isModalActive: action.isModalActive};
    default:
      return state;
  }
};


export const setLoaderStatus = (status) =>({
  type: SET_LOADER_STATUS,
  status,
});

export const setError = (error) => ({
  type: SET_ERROR,
  error,
});

export const setModal = (isModalActive) => ({
  type: SET_MODAL,
  isModalActive,
});
