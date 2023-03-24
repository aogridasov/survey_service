import React, { useContext } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import surveyList from '../components/survey_list'


export default function HomePage(props) {
    return (
        <main>
            <div className='container'>
            <h1>Surveys </h1>
            <ul>
                {surveyList(props.surveyList)}
            </ul>
            </div>
        </main>
    )
}