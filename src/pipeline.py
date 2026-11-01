from src.extract import extract_weather_data
from src.validate import validate_weather_response


def run_weather_pipeline(latitude, longitude, timezone):

    # Step 1: Extract weather data
    weather_data = extract_weather_data(
        latitude,
        longitude,
        timezone
    )

    # Step 2: Validate extracted data
    validate_weather_response(weather_data)

    # Step 3: Return validated data
    return weather_data