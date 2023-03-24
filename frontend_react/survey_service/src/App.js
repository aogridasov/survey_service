
import './App.css';
import React, { useState } from 'react'
import { Route, Routes } from 'react-router-dom'
import HomePage from './pages/home'
import UserPage from './pages/user_profile'
import LeaderboardPage from './pages/leaderboard';
import Header from './components/header'
import LoginPage from './pages/login';
import SignUpPage from './pages/signup';


const survey_list = [
  {
      id: 1,
      title: 'test',
      description: 'test test'
  },
  {
      id: 2,
      title: 'test2',
      description: 'test test 2'
  }
]


const user_list = [
  {
    id: 1,
    username: 'toshley',
    coins: 110,
    completed_surveys: 10,
    upgrades: {
      bg_color: true,
      border: false
    }
  },
  {
    id: 2,
    username: 'test',
    coins: 999,
    completed_surveys: 43,
    upgrades: {
      bg_color: false,
      border: true
    }
  },
  {
    id: 3,
    username: 'testy',
    coins: 333,
    completed_surveys: 3,
    upgrades: {
      bg_color: true,
      border: true
    }
  }
]


const logged_in = false



export default function App() {
  const [ loggedIn, setLoggedIn ] = useState(logged_in)
  const [ currentUser, setCurrentUser ] = useState(user_list[0])
  const [ surveyList, setSurveyList] = useState(survey_list)
  const [ userList, setUserList] = useState(user_list)
  const [token, setToken] = useState();

  if(!token) {
    return <LoginPage setToken={setToken} />
  }

  return (
    <>
      <Header loggedIn={loggedIn} currentUser={currentUser}></Header>
      <main>
      <Routes>
          <Route exact path='/' element={<HomePage surveyList={surveyList}/>} />
          <Route path='user/:user_id' element={<UserPage currentUser={currentUser} surveyList={surveyList}/>} />
          <Route exac path='leaderboard' element={<LeaderboardPage userList={userList}/>} />
          <Route exac path='login' element={<LoginPage/>} />
          <Route exac path='signup' element={<SignUpPage/>} />
      </Routes>
      </main>
    </>
  )
}