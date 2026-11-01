def validate_weather_response(data):

    #check for response structure
    if not isinstance(data, dict):
        raise ValueError("API response is not a dictionary as expected.")

    #check if the daily field exists
    if "daily" not in data:
        raise ValueError("Missing 'daily' field in API response.")

    daily_data = data["daily"]

    #check: are the 3 required fields are present

    required_fields = ["time" , "temperature_2m_max", "temperature_2m_min"]
    for field in required_fields:
        if field not in daily_data:
            raise ValueError(f"Missing required fields: {field}")

    #check for all three required fields containing python lists
    
    for field in required_fields:
            if not isinstance(daily_data[field] , list):
                raise ValueError(f"Field '{field}' is not a list as expected.")
    #check for length consistency of the lists

    lengths = [len(daily_data[field]) for field in required_fields]

    if len(set(lengths)) != 1:
        raise ValueError("Weather data arrays have unequal lengths.")

    if lengths[0] == 0:
        raise ValueError("Weather data arrays are empty.")

    for field in ["temperature_2m_max", "temperature_2m_min"]:
        for value in daily_data[field]:
            if not isinstance(value, (int, float)):
                raise ValueError(f"Field '{field}' contains a non-numeric value: {value!r}")
    return True
     