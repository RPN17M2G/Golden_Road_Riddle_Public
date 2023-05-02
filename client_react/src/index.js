import React, {useState} from 'react';
import ReactDOM from 'react-dom';
import './index.css';

const NUMBER_OF_DIGITS_AFTER_THE_DECIMAL_POINT = 3
const M_TO_KM = 1000

const ResultBox = ({ value, title }) => ( //Results are shown in 4 identical boxs so I created a template for the box instead of copy and paste the div
    /*
    the result box template
    Input: value, title - the parts of the results
    Output: a div which includes the title and the value but formated and designed
    */
  <div className="result-box">
    <h3>{title}</h3>
    <p className='value'>{value}</p>
  </div>
);

const HoursBox = ({ hours }) => (
  <div className="hours-result-box">
    <h3>Hours available for Take Off</h3>
    <p className='hours'>{hours.join(', ')}</p>
  </div>
);



const InputForm = ({ onSubmit }) => (
    /*
    the form component
    Input: onSubmit - the function to handle the submit button in order to calculate the results and switch to the results component
    Output: the react component which includes the form and a submit button
    */
  <form onSubmit={onSubmit}> 
    <label className="input-label">Cargo Mass:</label>
    <input type="number" className="input-field" id="input_mass"/>
    <br />
    <label className="input-label">Date to check:</label>
    <input type="date" className="input-field" id="input_date"/>
    <input type="submit" className="submit-button" />
  </form>
);

const Results = ({ time_for_take_off, distance, distanceKM, mass_to_burn_in_order_to_take_off, hours, handleReturnClick }) => (
    /*
    the results component
    Input: handleReturnClick - the function to handle a switch back to the form. time_for_take_off, distance, distanceKM(distance in km instead of m), weight_to_burn_in_order_to_take_off, hours - the results to show
    Output: the react component which includes the results and the return button
    */
  <div className="results-container">
    <div className='results-content'>
      <ResultBox value={time_for_take_off} title="Time required for take off - Seconds" />
      <ResultBox value={distanceKM} title="Road distance in order to take off - KM" />
      <ResultBox value={distance} title="Road distance in order to take off - M" />
      <ResultBox value={mass_to_burn_in_order_to_take_off} title="weight to burn in order to take off in under 60 seconds - KG" />
      <HoursBox hours={hours} />
    </div>

    
    <button onClick={handleReturnClick}  className="return-button">Return</button>
  </div>
);

const WelcomeScreen = () => {
  /*
  Shows the main page and handles the events
  Input: none
  Output: A page with a welcome message, a description about the calculator, the aircraft specifation and a form for cargo mass 
  which than shows the results of the calculation
  */

  const [showResults, setShowResults] = useState(false);
  const [timeResult, setTimeResult] = useState("");
  const [distanceResultKM, setDistanceResultKM] = useState("");
  const [distanceResult, setDistanceResult] = useState("");
  const [massResult, setMassResult] = useState("");
  const [hoursResult, setHoursResult] = useState([]);


  const handleSubmit = async (event) => {
    event.preventDefault();
    var mass = event.target.querySelector('input[id="input_mass"]').value;
    var date = event.target.querySelector('input[id="input_date"]').value;

    fetch("http://localhost:5000/calculate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ 'mass' : mass, 'date' : date }),
        })
        .then((response) => response.json())
        .then((data) => {
            //Update the results - format the numbers with ',' and round the results to 3 digits after the decimal point for easier viewing
            setTimeResult(data['time_for_take_off'].toLocaleString(undefined, {maximumFractionDigits:NUMBER_OF_DIGITS_AFTER_THE_DECIMAL_POINT}))
            setDistanceResult((data['distance']).toLocaleString(undefined, {maximumFractionDigits:NUMBER_OF_DIGITS_AFTER_THE_DECIMAL_POINT}))
            setDistanceResultKM((data['distance']  / M_TO_KM ).toLocaleString(undefined, {maximumFractionDigits:NUMBER_OF_DIGITS_AFTER_THE_DECIMAL_POINT}))
            setMassResult(data['mass_to_burn_in_order_to_take_off'].toLocaleString(undefined, {maximumFractionDigits:NUMBER_OF_DIGITS_AFTER_THE_DECIMAL_POINT}))
            
            setHoursResult([].concat(...JSON.parse(data['hours_for_take_off']))) //Add the array to the results

            setShowResults(true); //Change the screen
        })
        .catch((err) => {

            console.log(err.message)
            if(err.message.includes("Negative")){
                alert("Please enter a positive value.")
            } else if(err.message.includes("Failed to fetch"))
            {
                alert("The server is not active.")
            } else if(err.message.includes("Could not")){
              alert("Failed to retrive weather, maybe the date is to far in the future or the past.")
            }
        });

    
    
};

  const handleReturnClick = () => {
    //Reset the results
    setDistanceResult(0)
    setTimeResult(0)
    setMassResult(0)

    setShowResults(false); //Change the screen
  };

  //The full page
  return (
    <div className='main-container'>
      <h1 className="welcome-message">Welcome!</h1>
      <h2 className="description-message">To the Physics Calculator<br />This calculator lets you enter <br />the mass of the Cargo for an aircraft<br />
      and shows you the time takes to take off,<br />the distance the road must be for take off<br />and if the time for take off is greater than<br /> 60 seconds - it shows the amount of mass<br />
      to burn in order to take off in under 60 seconds.
      </h2>

      {showResults ? ( //All the messages are static so I implimented a switch so that only this div will get changed
        <Results time_for_take_off={timeResult} distance={distanceResult} distanceKM={distanceResultKM} mass_to_burn_in_order_to_take_off={massResult} hours={hoursResult} handleReturnClick={handleReturnClick} />
      ) : (
        <InputForm onSubmit={handleSubmit} />
      )}

      <h3 className='aircraft-specifation'>The results shown are for an aircraft which<br /> weights 350,000 N(including the passengers),<br />
      which takes off in a speed of 140 M/S<br />and its engines produce 100,000 N/S of force
      </h3>
    </div>
  );
};

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<WelcomeScreen />)
