import React from 'react';

import forecastImage from './assets/images/bidripperlogo.png' 

const Branding = () => {
    return (
        <div className="branding">
            <img className='forecast-image' src={forecastImage} alt='Current 4 week Forecast ' />
        </div>
    );
}
 
export default Branding;
