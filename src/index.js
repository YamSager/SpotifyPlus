import _ from 'lodash';
import React, { Component } from 'react';
import axios from 'axios';
import ReactDOM from 'react-dom';
import SpotifyContent from './components/spotify/spotify_content';

class App extends Component {

  constructor(props) {
    super(props);

    this.state = {
      authToken: ''
    };

    this.getInfo = this.getInfo.bind(this);
  }

  getInfo() {
    axios.get(`https://api.spotify.com/v1/search?q=$albums&type=$gossamer&limit=4`, { headers: { Authorization: 'Bearer ' + this.state.authToken } })
    .then(content => console.warn('spotify', content));
  }

  render() {
    return (
      <div>
        <SpotifyContent setAuthToken={(authToken) => this.setState({authToken})}/>
        <button onClick={this.getInfo}>Click and check console</button>
      </div>
    );
  }
}

ReactDOM.render(<App />, document.querySelector('.app'));

