import React, { Component } from 'react';
import './login.css'


export default class RegistrationComponent extends Component {
    render() {
        return(
            <div className="login-page">
                <div className="form">
                    <form className="login-form">
                        <input type="text" placeholder="Email address"/>
                        <input type="text" placeholder="First name"/>
                        <input type="text" placeholder="Middle name"/>
                        <input type="text" placeholder="Last name"/>
                        <input type="text" placeholder="Owner or Tenant"/>
                        <input type="text" placeholder="Phone number - "/>
                        <input type="text" placeholder="Date of birth - mm/dd/yyyy"/>
                        <input type="password" placeholder="Password"/>
                        <button>Sign Up</button>
                    </form>
                </div>
            </div>
        )
    };
}
