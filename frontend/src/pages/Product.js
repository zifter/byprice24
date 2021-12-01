import React from 'react';
import {useParams} from 'react-router';
import {useEffect} from 'react';
import axios from 'axios';

const Product = () => {
  const {id} = useParams();
  console.log('id', id);
  useEffect(() => {
    console.log('effect');
    axios
        .get('https://reqbin.com/echo')
        .then((response) => {
          console.log('promise fulfilled');
        });
  }, []);

  return (
    <div>
            Product - {id}
    </div>
  );
};

export default Product;
