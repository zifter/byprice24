import React from 'react';
import './ProductPage.css';
import {useParams} from 'react-router';
import {useEffect} from 'react';
import ProductBody from './elements/ProductBody.js';
import ProductTabs from './elements/product_tab/ProductTabs';
import {
  Text, Container,
} from 'atomize';
import {getCurrentProduct} from "../../redux/productsReducer";
import {useDispatch, useSelector} from "react-redux";

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
  const isLoading = useSelector(state => state.app.isLoading)
  const products = useSelector(state => state.products)
  const dispatch = useDispatch();
  const {id} = useParams();
  let productData = products.results.find(item=>item.id === +id)

  if (!productData){
    productData = products.results[0]

  }
  recentlyViewedLocalStorageHandler(id);

  const hook = () => {

    dispatch(getCurrentProduct(id))
  };

  useEffect(hook, [id]);
  return (
    <Container minH="83vh">
      {isLoading &&
            <Text
              tag="h1"
              textSize="heading"
              textAlign={{xs: 'center'}}>
              Загрузка...
            </Text>
      }

      {productData.product_pages &&
        <ProductBody productData={productData}/>
      }
      {productData.product_pages &&
      <ProductTabs productData={productData}/>
      }
    </Container>
  );
};

export default ProductPage;
