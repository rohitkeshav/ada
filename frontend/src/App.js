import React, { Component } from 'react';
import LoginComponent from './components/login';
// import RegistrationComponent from './components/register';
import NavBarComponent from './components/navbar';
import { Route, Switch, HashRouter } from "react-router-dom";
import './App.css';
import HomeComponent from './components/home';


const Content = () => (
  <main>
    <Switch>
      <Route exact path='/' component={ HomeComponent } />
      <Route exact path='/login' component={ LoginComponent } />
      {/*<Route exact path='/register' component={ RegistrationComponent } />*/}
      {/*<Route exact path='/listings' component={ RegistrationComponent } />*/}
    </Switch>
  </main>
);


class App extends Component {
  render() {
    return (
        <HashRouter>
            <div className="App">
                <NavBarComponent />
                <Content />
            </div>
        </HashRouter>
    );
  }
}

export default App;
