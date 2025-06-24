# Golden Road Riddle

This project is a full-stack web application designed as part of a riddle challenge to identify candidates for the **Golden Road Team**.

## Overview

The application allows users to input the **mass of an aircraft's cargo** and receive the following outputs:

- **Time required for takeoff**
- **Minimum runway length needed for takeoff**
- If takeoff time exceeds **60 seconds**, it calculates:
  - The **amount of mass to reduce** to achieve takeoff in under 60 seconds
- **Recommended hours for takeoff** based on temperature data at specific coordinates

The physics behind the calculations is based on simplified motion formulas.

## Technologies

- **Frontend**: React (JavaScript)
- **Backend**: Flask (Python)
- **Database**: SQLite3
- **External API**: Used to fetch real-time weather data

## Purpose

This public repository was created as a cleaned version of the original, which contained private data. It omits the original issues and commit history.

## Note

The coordinates used for temperature calculations are example values and can be adjusted.
