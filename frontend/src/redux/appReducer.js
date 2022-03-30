const initialState = {
    isLoading: false,
    error: null,
}
const SET_LOADER_STATUS = 'SET_LOADER_STATUS'
const SET_ERROR = 'SET_ERROR'

export const appReducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_LOADER_STATUS:
            return {...state, isLoading: action.status}
        case SET_ERROR:
            return {...state, error: action.error};

        default:
            return state;
    }
}


export const setLoaderStatus = (status) =>{
    return {
        type: SET_LOADER_STATUS,
        status
    }
};

export const setError = (error) => {
    return {
        type: SET_ERROR,
        error
    }
};


