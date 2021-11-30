import React from 'react';
import { useEffect } from 'react'
import { useLocation } from "react-router-dom";
import axios from "axios";

const Search = () => {
    const search = useLocation().search;
    const q = new URLSearchParams(search).get('q');

    useEffect(() => {
        let url = process.env.REACT_APP_BACKEND_HOST + '/api/v1/search/products?query=' + q
        console.log('request', url)
        axios
          .get(url)
          .then(response => {
            console.log('promise fulfilled')
      })
    }, [q])

    return (
        <div>
            Show results for - {q}
        </div>
    );
}

export default Search;
