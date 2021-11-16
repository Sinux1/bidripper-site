import React from 'react';

import forecastImage from './assets/images/bidripperlogo.png' 

const iHeight='192px'
const iWidth='487px'


const Branding = () => {
    return (
        <div className="branding">
            <img className='forecast-image' src={forecastImage} alt='Current 4 week Forecast ' />
        </div>
    );
}
 
export default Branding;