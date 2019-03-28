import { Navbar, Nav, NavDropdown, NavItem } from 'react-bootstrap'
import React, { Component } from 'react';
import { Link } from "react-router-dom";


export default class NavBarComponent extends Component {
    render (){
        return (
            <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">

                <Navbar.Brand href="/">ADA</Navbar.Brand>
                <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="mr-auto">
                        <Link className="nav-link" to="/login">Login</Link>
                        <Link className="nav-link" to="/register">Register</Link>
                      {/*<NavDropdown title="Dropdown" id="basic-nav-dropdown">*/}
                        {/*<NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>*/}
                        {/*<NavDropdown.Item href="#action/3.2">Another action</NavDropdown.Item>*/}
                        {/*<NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>*/}
                        {/*<NavDropdown.Divider />*/}
                        {/*<NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item>*/}
                      {/*</NavDropdown>*/}
                    </Nav>
                </Navbar.Collapse>

            </Navbar>
        )
    }
}
