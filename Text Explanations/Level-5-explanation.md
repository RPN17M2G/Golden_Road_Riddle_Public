
Level 5


Services:

React website:

The user interface of the program, its main purpose is to take the cargo mass input and show the results to the user.

Input: None – until the cargo mass input and the date is filled and sent to the server. Than the server returns the results - time for takeoff, distance for takeoff, amount of mass to burn in order to take off in under 60 seconds, hours available for takeoff.

Output: To the server: Cargo Mass.

`	`To the user: showing results.

Flask Server:

Responsible for transferring data between the React gui and the calculator.

Input: From React gui: cargo mass and date.

`            `From calculator: the results – time for takeoff, distance for takeoff, amount of mass to burn 	in order to take off in under 60 seconds, hours available for takeoff.

Output: For React gui: : the results – time for takeoff, distance for takeoff, amount of mass to burn 	in order to take off in under 60 seconds, hours available for takeoff.

`	`For calculator: cargo mass and date.

Database:

Saves previous results by the cargo mass inserted. Pull it for a faster answer.

Input: For insert: cargo mass, time for takeoff, distance for takeoff, amount of mass to burn in order	to take off in under 60 seconds.

`	`For get: cargo mass.

Output: For insert: none

For get: time for takeoff, distance for takeoff, amount of mass to burn in order to take off      in under 60 seconds.

Physics Calculator:

Calculates using physics equations the results.

Input: cargo mass

Output:  time for takeoff, distance for takeoff, amount of mass to burn in order to take off in under 60 seconds.

WeatherApi:

Using online weather api to check the temperatures in a specific date in the location of the mission and returns the hours when the temperatures are optimal for takeoff.

Input: the date

Output: A list with all the hours that the temperatures fit the requirements for takeoff.
