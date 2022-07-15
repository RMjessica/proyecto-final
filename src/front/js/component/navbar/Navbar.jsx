import React, { useContext, useEffect } from "react";
import { Link } from "react-router-dom";
import { SearchBar } from "./SearchBar.jsx";
import {
  AiOutlineShoppingCart,
  AiOutlineUser,
  AiOutlineLogout,
} from "react-icons/ai";
import { Context } from "../../store/appContext";

//import { IoLogOutOutline } from "react-icons/io";

import logo from "../../../img/logo.png";

export const Navbar = () => {
  const { store, actions } = useContext(Context);

  /*   const handleLogout = useEffect(() => {
    actions.logout();
  }, []); */

  return (
    <>
      <nav className="navbar sticky-top navbar-expand-sm navbar-light bg-light">
        <div className="container d-flex justify-content-around position-relative">
          <div className="navbar-brand m-0">
            <Link to="/inicio">
              <img
                src={logo}
                style={{ width: "55%", height: "30%" }}
                alt="Liberte"
              />
            </Link>
          </div>

          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item active d-inline position-absolute top-50 start-50 translate-middle">
                <SearchBar />
              </li>

              <div className="d-flex d-inline position-absolute top-50 start-100 translate-middle">
                {store.auth ? (
                  <li className="nav-item dropdown">
                    <Link to="/inicio">
                      <button
                        onClick={actions.logout}
                        type="button"
                        className="btn btn-sm mx-2 border-0"
                      >
                        <AiOutlineLogout size={28} />
                      </button>
                    </Link>
                  </li>
                ) : null}
                <li className="nav-item dropdown">
                  <Link to="/login">
                    <button type="button" className="btn btn-sm mx-2 border-0">
                      <AiOutlineUser size={28} />
                    </button>
                  </Link>
                </li>

                <li className="nav-item active">
                  <Link to="/cart">
                    <button type="button" className="btn btn-sm me-2 border-0">
                      <AiOutlineShoppingCart size={28} />
                    </button>
                  </Link>
                </li>
              </div>
            </ul>
          </div>
        </div>
      </nav>
    </>
  );
};
