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

const ProductPage = () => {
  const [productData, setProductData] = useState(Object);
  const [isLoading, setIsLoading] = useState(false);

  const {id} = useParams();
  console.log('id', id);
  console.log('productData', productData);

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

      {Object.keys(productData).length &&
      <ProductBody productData={productData} />
      }
      {Object.keys(productData).length &&
      <ProductTabs productData={productData}/>
      }
    </Container>
  );
};

export default ProductPage;
