from flask import Flask, request
from flask_cors import CORS
import json


import Database
import Physics_Calculator
import weatherApi

app = Flask(__name__)
CORS(app)

options = True

NOT_FOUND = -1

class HTTP_CODES():
    BAD_REQUEST = 400
    HTTP_OK = 200
    NO_CONTENT_SUCCESS = 204

class RESULTS_POSITIONS():
    DISTANCE = 0
    TIME = 1
    MASS_TO_BURN = 2

@app.before_request
def deal_with_options_request():
    if request.method == 'OPTIONS': #comes before POST
        headers = { #S
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'content-type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', HTTP_CODES.NO_CONTENT_SUCCESS, headers) 


@app.route('/calculate', methods=['POST'])
def calculate():

    if request.method == 'POST':
        # Perform calculations using the mass and return results
        mass = int(json.loads(request.data.decode())["mass"]) #Get the response, translate it into json and than get the mass, if fails the server will return 400 so its ok
        date = json.loads(request.data.decode())["date"] 
        weatherDetails = weatherApi.get_take_off_hours(date)
        db_instance = Database.database_instance() #Singleton pattern, the database should have only one connection


        results = db_instance.get_data_of_a_specific_cargo_mass(mass)

        if(mass < 0):
            return "Negative number", HTTP_CODES.BAD_REQUEST

        if(type(weatherDetails) == str):
            return weatherDetails, HTTP_CODES.BAD_REQUEST #Failed to retrive weather information

        if(results.count(NOT_FOUND) != 0): #If the database didnt find the results, calculate them and then insert them into the db
            results = Physics_Calculator.calc_results(mass)
            db_instance.insert_data(mass ,results[RESULTS_POSITIONS.DISTANCE] + 1, results[RESULTS_POSITIONS.TIME], results[RESULTS_POSITIONS.MASS_TO_BURN])            

        results_json = {'time_for_take_off' : results[RESULTS_POSITIONS.TIME], 'distance' : results[RESULTS_POSITIONS.DISTANCE], 'mass_to_burn_in_order_to_take_off' : results[RESULTS_POSITIONS.MASS_TO_BURN], 'hours_for_take_off' : json.dumps(weatherDetails)}
        return results_json, HTTP_CODES.HTTP_OK


if __name__ == '__main__':
    calculate()
    app.run(debug=True, host='0.0.0.0') #Self host














