import React, { useState } from "react";
import { Redirect } from "react-router-dom";
import Container from "react-bootstrap/Container";
import Navbar from "react-bootstrap/Navbar";
import Button from "react-bootstrap/Button";
import ButtonGroup from "react-bootstrap/ButtonGroup";
import ApiRoute, { ApiLogout } from "../config/ApiSettings";

function PageNavbar(props) {
  // const [redirect, setRedirect] = useState(false);

  //...logout Handler
  const logout = async (e) => {
    await ApiLogout();
    props?.setProfile(null);
    // setRedirect(true);
  };

  //...login Handler
  const login = (e) => {
    window.location.assign(`${ApiRoute.FRONTEND_DOMAIN}/login`);
  };

  //...register Handler
  const register = (e) => {
    window.location.assign(`${ApiRoute.FRONTEND_DOMAIN}/register`);
  };

  //...Profile Handler
  const profile = (e) => {
    window.location.assign(`${ApiRoute.FRONTEND_DOMAIN}/profile`);
  };

  //...Admin Handler
  const gotoAdmin = (e) => {
    window.location.assign(`${ApiRoute.API_ADMIN}`);
  };

  //...Access-board Handler
  const accessBoard = (e) => {
    window.location.assign(`${ApiRoute.FRONTEND_DOMAIN}/access-gate`);
  };

  // if (redirect) {
  //   window.location.assign(ApiRoute.FRONTEND_DOMAIN);
  // }
  return (
    <Navbar className="navbar-container">
      <Container>
        <Navbar.Brand href="#home">Meal Manager</Navbar.Brand>
        <Navbar.Toggle />
        <Navbar.Collapse className="justify-content-end" >
          <Navbar.Text className="ml-auto" >
              <Button variant="outline-secondary" style={{color:'black', margin: '5px'}} onClick={accessBoard} >
                Access Board
              </Button>
              <Button variant="outline-secondary" style={{color:'black', margin: '5px'}} onClick={gotoAdmin}>
                Admin
              </Button>
              <Button variant="outline-secondary" style={{color:'black', margin: '5px'}} onClick={profile}>
                Profile
              </Button>
              <Button variant="outline-secondary" style={{color:'black', margin: '5px'}}  onClick={register}>
                Register
              </Button>
              <Button variant="outline-secondary" style={{color:'black', margin: '5px'}} onClick={login}>
                Login
              </Button>
              <Button variant="outline-secondary"  style={{color:'black', margin: '5px'}} onClick={logout}>
                Logout
              </Button>
          </Navbar.Text>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default PageNavbar;
