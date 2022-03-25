import React from 'react';
import './ProductPage.css';
import {useParams} from 'react-router';
import {useEffect, useState} from 'react';
import axios from 'axios';
import ProductBody from './elements/ProductBody.js';
import ProductTabs from './elements/product_tab/ProductTabs';
import {
  Text, Container,
} from 'atomize';

const recentlyViewedLocalStorageHandler = (id) => {
  const recentlyViewed = JSON.parse(localStorage.getItem('recentlyViewed'));
  if (!recentlyViewed) {
    localStorage.setItem('recentlyViewed',
        JSON.stringify({'products': [{'id': id}]}));
  } else {
    const products = recentlyViewed['products'];
    const found = products.some((el) => id === el['id']);
    if (found) {
      const index = products.findIndex((item) => item.id === id);
      products.splice(index, 1);
      products.unshift({'id': id});

      localStorage.setItem('recentlyViewed',
          JSON.stringify(recentlyViewed));
    } else {
      products.unshift({'id': id});
      if (products.length > 4) {
        products.pop();
      }
      localStorage.setItem('recentlyViewed',
          JSON.stringify(recentlyViewed));
    }
  }
};

const ProductPage = () => {
  const [productData, setProductData] = useState(Object);
  const [isLoading, setIsLoading] = useState(false);

  const {id} = useParams();
  console.log('id', id);
  console.log('productData', productData);

  recentlyViewedLocalStorageHandler(id);

  const hook = () => {
    const url = '/api/v1/products/' + id;
    console.log('request', url);

    axios
        .get(url)
        .then((response) => {
          console.log('got', response.data);
          setProductData(response.data);
        }).catch(function(error) {
          console.log(error);
        }).finally(function(error) {
          setIsLoading(true);
        });
  };

  useEffect(hook, [id]);

  return (
    <Container>
      {!isLoading &&
            <Text
              tag="h1"
              textSize="heading"
              textAlign={{xs: 'center'}}>
              Загрузка...
            </Text>
      }

      {Object.keys(productData).length ?
      <ProductBody productData={productData} /> : null
      }
      {Object.keys(productData).length ?
      <ProductTabs productData={productData}/> : null
      }
    </Container>
  );
};

export default ProductPage;
