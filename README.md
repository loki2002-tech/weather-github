Overview
The Weather App is a GUI-based application that provides real-time weather updates for any city worldwide. It fetches weather data using the OpenWeatherMap API and displays key weather parameters like temperature, humidity, wind speed, and atmospheric pressure.

Features
✅ Real-Time Weather Updates – Fetches current weather conditions for any location.
✅ City-Based Search – Users can enter a city name to get instant weather details.
✅ Timezone Detection – Automatically detects and displays the local time of the city.
✅ Interactive GUI – Built with Tkinter for a user-friendly interface.
✅ Error Handling – Displays appropriate messages for invalid city names or network issues.

Technologies Used
Programming Language: Python
Libraries & Modules: Tkinter, Requests, OpenWeatherMap API, Geopy, TimezoneFinder, Pytz, Datetime
How It Works
User Input: The user enters a city name in the search field.
Geolocation Processing: The app retrieves the geographical coordinates of the city using Geopy.
Timezone Detection: The current local time of the city is determined using TimezoneFinder and pytz.
Weather Data Fetching: The app makes an API call to OpenWeatherMap to retrieve real-time weather details.
Weather Display: The fetched weather information (temperature, condition, humidity, wind speed, pressure) is displayed in the GUI.
