import React, { Component } from "react";
import { useNavigate } from "react-router-dom";





const surveys = [
  {
    id: 1,
    title: "Cat or dog?",
    description: "Who is better: a cat or a dog?",
    questions: [1, 2, 3]
  },
  {
    id: 2,
    title: "Mouse or rat?",
    description: "Who is better: a mouse or a rat?",
    questions: [4, 5, 6]
  },
]

const solved_surveys = [
  {
    id: 1,
    title: "Cat or dog?",
    description: "Who is better: a cat or a dog?",
    questions: [1, 2, 3]
  },
]

const user = {
  id: 1,
  username: "testuser",
  coins: 999,
  upgrades: {
    backgound_color: 1,
    border: 1
  }

}

const isLoggedIn = true

const bg_color_price = 200
const border_price = 1000




class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      indexSurveyList: surveys,
      userSurveyList: solved_surveys,
      isLoggedIn: isLoggedIn,
      user: user,
      bg_color_price: bg_color_price,
      border_price: border_price
    };
  }

  // displayCompleted = (status) => {
  //   if (status) {
  //     return this.setState({ viewCompleted: true });
  //   }

  //   return this.setState({ viewCompleted: false });
  // };

  renderSurveys = (surveyList) => {

    return surveyList.map((item) => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span>
          <b>{item.title}</b>
          <br/>
          {item.description}
        </span>
      </li>
    ));
  };

  renderUserProfile = () => {
    const user = this.state.user
    const bg_color_price = this.state.bg_color_price
    const border_price = this.state.border_price

    return (
      <div>  
        <h1> {user.username}</h1>
        <b>Баланс: {user.coins}</b>
        <br/>
        <b>
            <a href="">Купить красивый фон ({{bg_color_price}})</a>
            <a href="">Купить красивую рамку вокруг ника ({{border_price}})</a>
        </b>
        <br/>
        <br/>
        <b>Пройденные опросы:</b>
        <br/>
        <br/>
        <ul className="list-group list-group-flush border-top-0">
                {this.renderSurveys(this.state.userSurveyList)}
        </ul>
      </div>
    )
  }

  renderUserInterface = () => {
    const navigate = useNavigate();
    const isLoggedIn = this.state.isLoggedIn
    const user = this.state.user
    if (isLoggedIn) {
      return (
        <div>
        <a href={navigate('/profile/:user_id')}>
          {user.username}
          &nbsp;
          //
          &nbsp;
          {user.coins} coins
			  </a>
			  <a href="">Logout</a>
      </div>
      )
    }
    return (
      <div>
        <a href="">Login</a>
        <a href="">Sign Up</a>
		  </div>
    )

  }

  renderHeader = () => {
    return (
      <header>
        <div>
          <a href="">
            Main
          </a>
          <a href="">
            Leaderboards
          </a>
        </div>
        <div>
          {this.renderUserInterface()}
        </div>
      </header>
    );
  };


  render() {
    return (
      <body>
        {this.renderHeader()}
        <main className="container">
          <h1 className="text-white text-uppercase text-center my-4">Surveys</h1>

                <div>
                <ul className="list-group list-group-flush border-top-0">
                  {this.renderSurveys(this.state.indexSurveyList)}
                </ul>
              </div>
        </main>
      </body>
    );
  }
}

export default App;