import React from "react";

/* REACT-BOOTSTRAP */
import { Card } from "react-bootstrap";

/* REACT ROUTER */
import { Link } from "react-router-dom";

/* COMPONENTS */
import Rating from "./Rating";

function Product({ product }) {
  return (
    <Card className="my-3 p-3 rounded" >
      <Link to={`/product/${product._id}`}>
        <Card.Img src={product.image} width='300' height='350'/>
      </Link>

      <Card.Body>
        <Link to={`/product/${product._id}`}>
          <Card.Title as="div">
            <h4 style={{fontFamily:'Chalkboard'}}> {product.name}</h4>
          </Card.Title>
        </Link>

        <Card.Text as="div">
          <Rating
            value={product.rating}
            text={`${product.numReviews}  Reviews`}
            color={"#f8e825"}
          />
        </Card.Text>

        <Card.Text as="h3">${product.price}</Card.Text>
      </Card.Body>
    </Card>
  );
}

export default Product;
