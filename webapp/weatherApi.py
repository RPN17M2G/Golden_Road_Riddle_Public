import requests
import datetime

LATITUDE = 30
LONGITUDE = 35

HTTP_OK = 200

START_INDEX_HOUR = -5
END_INDEX_HOUR = -3

MIN_TEMP = 15
MAX_TEMP = 30

NUMBER_OF_HOURS_A_DAY = 24

THREE_AFTER_THE_DECIMAL_POINT = 3


API_KEY = "1067ca546d8e48318b380656230202"

def get_take_off_hours(date):
    '''
    Checks in which hours of the selected date the tempratures are between MIN_TEMP and MAX_TEMP
    Input: date - the date to check
    Output: if unsuccessfull - str with the details of the error. If successfull - List including all the hours that the
    plane can take off in and the.
    '''
    hours_in_range = []
    sum_temp = 0

    #The Api url with the arguments.
    weather_url = f"http://api.weatherapi.com/v1/history.json?key={API_KEY}&q={LATITUDE},{LONGITUDE}&dt={date}&units=metric"
    response = requests.get(weather_url)

    if response.status_code == HTTP_OK:
        weather = response.json()

        for hour in weather['forecast']['forecastday'][0]['hour']: #Check each hour
            temperature = hour['temp_c']
            sum_temp += temperature #For calculating avarage
            if MIN_TEMP <= temperature and temperature <= MAX_TEMP: #Able to take off 
                hours_in_range.append(hour['time'][START_INDEX_HOUR:END_INDEX_HOUR]) #Append only the hour, without the date and the minutes
        
        if(len(hours_in_range) == 0):
            hours_in_range.append("No hours are avaliable for take off, temperature in destination is: " + str(round(sum_temp / NUMBER_OF_HOURS_A_DAY, THREE_AFTER_THE_DECIMAL_POINT) + " C")) #Add the unavailble to fly message
        
        return hours_in_range #List
        
    else:
        return "Could not retrieve weather information" #str

