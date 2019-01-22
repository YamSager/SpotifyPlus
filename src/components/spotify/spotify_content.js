import React, { Component } from 'react';
import { Link } from './styledComponents';

let ACCESS_TOKEN = '';

class SpotifyContent extends Component {
  constructor(props) {
    super(props);

    ACCESS_TOKEN = this.checkForAccessToken();
  }

  checkForAccessToken() {
    if(!window.location.hash) return '';

    const firstValue = window.location.hash.substr(1).split("&")[0];

    if (firstValue.slice(0,12) == 'access_token') {
      const authToken = firstValue.slice(13);
      this.props.setAuthToken(authToken)
      return authToken;
    }
    return '';
  }

  render() {
    if (ACCESS_TOKEN === '') {
      return (
        <div>
          <Link href={`https://accounts.spotify.com/authorize?client_id=eba159118f0d4828a7428420d976089e&redirect_uri=http:%2F%2F${window.location.host}%2F&response_type=token`}>Click here to enable spotify</Link>
        </div>
      );
    }
    return null;
  }
};

export default SpotifyContent;
