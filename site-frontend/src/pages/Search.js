import React from 'react';
import { useEffect } from 'react'
import { useLocation } from "react-router-dom";
import axios from "axios";

const Search = () => {
    const search = useLocation().search;
    const q = new URLSearchParams(search).get('q');

    useEffect(() => {
        console.log('effect')
        axios
          .get('https://reqbin.com/echo')
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
