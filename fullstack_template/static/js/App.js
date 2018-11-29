import React from "react";
import { Route, NavLink, HashRouter} from "react-router-dom";
import Profile from "./Profile";
import Dashboard from "./Dashboard";

export default class App extends React.Component {
  render () {
    return (
    <HashRouter>
            <div>
                      <h1>RJEMS Enterprise</h1>
                      <ul className="header">
                        <li><span className="glyphicon glyphicon-user"></span><NavLink to="/Profile">Profile</NavLink></li>
                        <li><span className="glyphicon glyphicon-dashboard"></span><NavLink to="/Dashboard">Dashboard</NavLink></li>
                        <li><span className="glyphicon glyphicon-search"></span><a href="/Search">Search</a></li>
                        <li><span className="glyphicon glyphicon-upload"></span><a href="/Upload">Upload</a></li>
                      </ul>
            <div className="content">
            <Route path="/Profile" component={Profile}/>
            <Route path="/Dashboard" component={Dashboard}/>
            </div>
            </div>
    </HashRouter>
    )
  }
}


