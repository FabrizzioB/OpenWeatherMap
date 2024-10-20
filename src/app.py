import uvicorn
import requests
from datetime import datetime

from fastapi import FastAPI, HTTPException
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from config import API_KEY, DEFAULT_LANGUAGE, UNITS
from cities import cities_portugal

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "cities": cities_portugal})

@app.get("/weather/{city}")
def read_weather(city: str):
    """
    Retrieves the current weather for a given city.

    - **city**: Name of the city to get weather information for.
    - Returns a JSON object with the city name, current temperature (in Celsius), and a brief description of the weather condition.
    - Raises a 404 error if the city is not found.

    Example response:
    ```json
    {
        "city": "Porto",
        "temperature": 22.5,
        "description": "clear sky"
    }
    ```
    """
    weather_data = get_current_weather(city)

    return {
        "city": weather_data['name'],
        "temperature": weather_data['main']['temp'],
        "description": weather_data['weather'][0]['description']
    }

@app.get("/current/{city}")
def get_current_weather(city: str):
    """
    This endpoint retrieves the weather information for a given city.

    - **city**: The name of the city to get weather information for.
    - Returns the weather data in JSON format.
    - If the city is not found in the predefined list or in the API, it raises a 404 error.
    """
    # Find the city in the predefined list
    city_info = next((item for item in cities_portugal if item["city"].lower() == city.lower()), None)

    if city_info is None:
        raise HTTPException(status_code=404, detail="City not found within the list.")

    # Extract latitude and longitude
    lat = city_info['lat']
    lon = city_info['lon']

    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}lat={lat}&lon={lon}&lang={DEFAULT_LANGUAGE}&units={UNITS}&appid={API_KEY}"

    response = requests.get(complete_url)

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=404, detail="City, latitude or longitude doesn't correspond with any results in OpenWeatherMap API.")


@app.get("/forecast/{city}",
         summary="Get 8-day weather forecast for a city",
         description="This endpoint retrieves the 8-day weather forecast for a specified city, including daily temperatures and weather conditions.",
         responses={
             200: {
                 "description": "8-day weather forecast returned successfully",
                 "content": {
                     "application/json": {
                         "example": {
                             "city": "Porto",
                             "forecast": [
                                 {
                                     "date": "2023-10-18",
                                     "temperature": {"day": 21.5, "night": 15.2},
                                     "description": "clear sky"
                                 },
                                 {
                                     "date": "2023-10-19",
                                     "temperature": {"day": 20.3, "night": 14.1},
                                     "description": "few clouds"
                                 }
                             ]
                         }
                     }
                 }
             },
             404: {"description": "City not found in OpenWeatherMap"}
         })
def get_forecast(city: str):
    """
    Retrieves an 8-day weather forecast for a given city.

    - **city**: Name of the city to get the weather forecast for.
    - Returns a JSON object with the city name and a list of forecasted days, including date, day and night temperatures, and weather description.
    - Raises a 404 error if the city is not found.
    """
    # Find the city in the predefined list
    city_info = next((item for item in cities_portugal if item["city"].lower() == city.lower()), None)

    if city_info is None:
        raise HTTPException(status_code=404, detail="City not found in the list")

    lat = city_info['lat']
    lon = city_info['lon']

    # Construct the API URL
    base_url = "https://api.openweathermap.org/data/3.0/onecall"
    complete_url = f"{base_url}?lat={lat}&lon={lon}&exclude=current,minutely,hourly,alerts&units={UNITS}&lang={DEFAULT_LANGUAGE}&appid={API_KEY}"

    # Make the API request
    response = requests.get(complete_url)

    if response.status_code == 200:
        forecast_data = response.json()

        # Extract the daily forecast for 8 days
        daily_forecast = []
        for day in forecast_data['daily']:
            day_forecast = {
                "date": datetime.fromtimestamp(day['dt']).strftime('%Y-%m-%d'),
                "temperature": {
                    "day": round(day['temp']['day'], 2),
                    "night": round(day['temp']['night'], 2)
                },
                "description": day['weather'][0]['description']
            }
            daily_forecast.append(day_forecast)

        return {
            "city": city_info['city'],
            "forecast": daily_forecast
        }
    else:
        raise HTTPException(status_code=404, detail="City not found in OpenWeatherMap")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
