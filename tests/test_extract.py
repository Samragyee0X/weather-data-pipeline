import pytest
import requests
from unittest.mock import patch, Mock
from src.extract import extract_weather_data

args = (20.7172 , 85.3240 , "Asia/Kathmandu")

def test_success_retuns_data():
    fake = Mock()
    fake.json.return_value = {
        "daily": {"time": ["2023-11-01"]}
        }
    with patch("requests.Session.get", return_value=fake):
        result = extract_weather_data(*args)
        assert result == {"daily": {"time": ["2023-11-01"]}}

def test_timeout():
    with patch("requests.Session.get", side_effect=requests.exceptions.Timeout):
        with pytest.raises(RuntimeError, match="The API request timed out"):
            extract_weather_data(*args)

def test_http_error():
        fake = Mock()
        fake.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Client Error")
        with patch("requests.Session.get", return_value=fake):
            with pytest.raises(RuntimeError, match="HTTP error occurred: 404 Client Error"):
                extract_weather_data(*args)

def test_connection_error():
    with patch("requests.Session.get", side_effect=requests.exceptions.RequestException("Connection error")):
        with pytest.raises(RuntimeError, match="Error occurred during the API request: Connection error"):
            extract_weather_data(*args)

def test_invalid_json():
    fake = Mock()
    fake.json.side_effect = requests.exceptions.JSONDecodeError("bad", "", 0)
    with patch("requests.Session.get", return_value=fake):
        with pytest.raises(RuntimeError, match="Error occurred while parsing the JSON response"):
            extract_weather_data(*args)
    
    