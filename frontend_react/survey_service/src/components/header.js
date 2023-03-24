import React, { useState } from 'react';
import {  generatePath, Link, useParams } from 'react-router-dom';


function Header (props) {
    const user = props.currentUser
    const id = user.id
    let user_interface
    if (props.loggedIn) {
        user_interface = <div>
            <Link to={generatePath('/user/:id', {id})}>
                {user.username}
                &nbsp;
                //
                &nbsp;
                {user.coins} coins
            </Link>
            <a href="">Logout</a>
        </div>
        } else {
            user_interface = 
        <div>
            <Link to='/login'>Login</Link>
            <Link to='/signup'>Sign Up</Link>
        </div>
        }

    return (
        <header>
        <div>
            <Link to="/">
            Main
            </Link>
            <Link to="/leaderboard">
            Leaderboard
            </Link>
        </div>
        {user_interface}
        </header>
    );
}

export default Header;
