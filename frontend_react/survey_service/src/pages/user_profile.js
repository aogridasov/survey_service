import React from 'react';
import { useParams } from 'react-router-dom';
import surveyList from '../components/survey_list'


export default function UserPage(props) {
    const { id } = useParams();
    const user = props.currentUser
    return (
        <>  
        <h1> {user.username}</h1>
        <b>Баланс: {user.coins}</b>
        <br/>
        <b>
            <a href="">Купить красивый фон 200</a>
            <a href="">Купить красивую рамку вокруг ника 1000</a>
        </b>
        <br/>
        <br/>
        <b>Пройденные опросы:</b>
        <br/>
        <br/>
        <ul className="list-group list-group-flush border-top-0">
                {surveyList(props.surveyList)}
        </ul>
      </>
    );
}