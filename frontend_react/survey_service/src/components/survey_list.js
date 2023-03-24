import React from 'react';

function surveyList(surveyList) {
    return surveyList.map((item) => (
    <li
        key={item.id}
    >
        <span>
        <b>{item.title}</b>
        <br/>
        {item.description}
        </span>
    </li>
        ));
};
export default surveyList;