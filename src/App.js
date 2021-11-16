import Branding from './Branding';
import SpotBid from './SpotBid';
import { withAuthenticator } from '@aws-amplify/ui-react';
import React from 'react';
import { AmplifySignOut } from '@aws-amplify/ui-react';

function App() {
  return (
    
    <div className="App">
      <div className="mForecast">
        <Branding />
      </div>
      <div className="spotBid">
        <SpotBid />
      </div>
      <div className="signout"><AmplifySignOut /></div>
    </div>
  );
}


export default withAuthenticator(App);
