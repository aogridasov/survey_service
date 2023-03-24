import React, { useContext } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import userList from '../components/user_list'


export default function LeaderboardPage(props) {
    return (
        <main>
            <div className='container'>
            <h1>Leaderboard</h1>
            <ul>
                {userList(props.userList)}
            </ul>
            </div>
        </main>
    )
}