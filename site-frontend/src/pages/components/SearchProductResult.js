import React from 'react';
import { useState } from 'react';
import { useNavigate } from "react-router-dom";
import { Link } from "react-router-dom";

function SearchProductResult({ product }) {
  return (
    <div>
        <Link to={`/products/${product.id}`}>{ product.name }</Link>
    </div>
  );
}

export default SearchProductResult;
