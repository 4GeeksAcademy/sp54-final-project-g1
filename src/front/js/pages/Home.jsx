import React, { useContext } from "react";
import { Context } from "../store/appContext.js";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";
import { ProductsList } from "./ProductsList.jsx";
import { Slider } from "./Slider.jsx";
import { Newsletter } from "../component/Newsletter.jsx";



export const Home = () => {
  const { store, actions } = useContext(Context);

  return (
    <div className="text-center mt-5">
      <h1>Hello Rigo!!</h1>
      <p>
        <img src={rigoImageUrl} />
      </p>
      <div className="alert alert-info">
        {store.message || "Loading message from the backend (make sure your python backend is running)..."}
      </div>
      <Slider />
      <ProductsList />
      <p>
        This boilerplate comes with lots of documentation:{" "}
        <a href="https://start.4geeksacademy.com/starters/react-flask">
          Read documentation
        </a>
      </p>
      <Newsletter />
    </div>
  );
};
