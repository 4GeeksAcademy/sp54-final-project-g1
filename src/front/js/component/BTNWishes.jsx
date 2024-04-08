import React, { useContext } from "react";
import { Context } from "../store/appContext.js";
import { Link } from "react-router-dom";
export const BTNWishes = () => {
    const { store, actions } = useContext(Context);
    let myWishes = store.wishes;

    // If not logged in, try to read from localStorage
    /* if (!store.isLogin) {
        const wishesFromStorage = JSON.parse(localStorage.getItem("wishes")) || [];
        myWishes = wishesFromStorage;
    } */

    return (
        <Link to={"/wishes"}>
            <button className="btn btn-success position-relative ms-2">
                Wishes
                <span className="position-absolute top-0 end-0 translate-middle badge rounded-pill bg-warning text-dark">
                    {myWishes.length}
                </span>
            </button>
        </Link>
    );
};