import React from 'react';
import { API } from 'aws-amplify'
import { useState } from "react";


const Spot_Bids = () => {
    function NewlineText(props) {
        const text = props.text;
        return text.split('\n').map(str => <p>{str}</p>);
      }
    const [budget, setBudget] = useState('0')
    const [projectedBid, setProjectBid] = useState('')

    const getBid = async (e) => {
        e.preventDefault();
        if (isNaN(budget)) {
            setProjectBid("Budget must be a number")
            console.log("ERROR: Budget must be a number value")
        } else {
            var msg = ""
            const data = await API.get('bidripperapi', '/bid/' + budget)

            var Data = JSON.parse(data.data);
            if (parseFloat(Data.Bid, 10)  === -2){
                msg = "Bidripper is currently experiencing internal problems.\nPlease check back later."
            } else{
                msg = `For the week beginning ${Data.WeekOf}\n`
                msg += `BID: $${Data.Bid}\n`
                msg += `RUNTIME: ${Data.Runtime} hours\n`
                msg += `APPROX COST: $${Data.Cost}\n`
                msg += `The forecast suggests the spot price will remain less than/equal to $${Data.max} this week`  
            }

            setProjectBid(msg)

        }
        
      }
    
    return (
        <div className="spot-bids">
            <div className="spot-bid-header">
                <h2>Get A Spot Bid</h2>
                <h2>c4.8xlarge : us-west-2a</h2> 
            </div>
            <form onSubmit={getBid}>
                <label>Budget: </label>
                <input type="text"
                required
                value={budget}
                onChange={(e) => setBudget(e.target.value) }/>
                <NewlineText text={projectedBid} />
                <button>Get Bid</button>
            </form>
        </div>
    );
}

export default Spot_Bids;
