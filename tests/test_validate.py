import pytest
from src.validate import validate_weather_response

def make_valid():
    return {
        "daily": {
            "time": ["2023-11-01", "2023-11-02", "2023-11-03"],
            "temperature_2m_max": [25.0, 26.5, 24.8],
            "temperature_2m_min": [15.0, 16.2, 14.5]
        }
    }

def test_valid_data_passes():
    assert validate_weather_response(make_valid()) == True

def test_not_a_dict():
    with pytest.raises(ValueError, match="API response is not a dictionary as expected."):
        validate_weather_response("not a dict")

def test_missing_daily_key():
    with pytest.raises(ValueError, match="Missing 'daily' field in API response."):
        validate_weather_response({})

def test_missing_temperature_field():
    data = make_valid()
    del data["daily"]["temperature_2m_max"]
    with pytest.raises(ValueError, match="Missing required fields"):
        validate_weather_response(data)

def test_field_not_a_list():
    data = make_valid()
    data["daily"]["time"] = "2026-11-01"
    with pytest.raises(ValueError, match="not a list"):
        validate_weather_response(data)


def test_unequal_list_lengths():
    data = make_valid()
    data["daily"]["temperature_2m_min"].pop()
    with pytest.raises(ValueError, match="unequal lengths"):
        validate_weather_response(data)

def test_empty_lists():
    data = make_valid()
    for key in data["daily"]:
        data["daily"][key] = []
    with pytest.raises(ValueError, match="empty"):
        validate_weather_response(data)


def test_none_value():
    data = make_valid()
    data["daily"]["temperature_2m_max"][0] = None
    with pytest.raises(ValueError, match="non-numeric"):
        validate_weather_response(data)


def test_text_value():
    data = make_valid()
    data["daily"]["temperature_2m_max"][0] = "hot"
    with pytest.raises(ValueError, match="non-numeric"):
        validate_weather_response(data)

