import React from 'react';

function userList(userList) {
    return (userList.map((item) => 
    <li
        key={item.id}
        style={{
            backgroundColor: `${
               item.upgrades.bg_color ? 'lightblue' : 'white'
            }`,
        }}
    >   
        <span
            style={{
                border: `${
                   item.upgrades.border ? 'dashed black 4px' : ''
                }`,
            }}
        >
            <b>{item.username}</b>
        </span>
        <br/>
        Опросов пройдено: {item.completed_surveys}
    </li>
        ));
};
export default userList;