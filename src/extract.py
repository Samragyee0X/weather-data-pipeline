import requests

def extract_weather_data(latitude, longitude, timezone="auto"):

    url = "https://api.open-meteo.com/v1/forecast"
    
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": [
            "temperature_2m_max",
            "temperature_2m_min",
        ],
        "timezone": timezone,
        "past_days" : 7 ,
        "forecast_days" : 3
    }

    try:
        with requests.Session() as session:
            response = session.get(url, params=params, timeout=30)
            response.raise_for_status()
            return response.json()

    except requests.exceptions.Timeout as error:
        raise RuntimeError("The API request timed out") from error
    except requests.exceptions.HTTPError as error:
        raise RuntimeError(f"HTTP error occurred: {error}") from error
    except requests.exceptions.RequestException as error:
        raise RuntimeError(f"Error occurred during the API request: {error}") from error
    except ValueError as error:
        raise RuntimeError("Error occurred while parsing the JSON response") from error