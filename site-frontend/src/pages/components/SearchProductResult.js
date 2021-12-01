import React from 'react';
import { Link } from "react-router-dom";

function SearchProductResult({ product }) {
  return (
    <div>
        <Link to={`/products/${product.id}`}>{ product.name }</Link>
    </div>
  );
}

export default SearchProductResult;
