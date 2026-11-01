import pytest
from unittest.mock import Mock, patch
from src.extract import extract_weather_data
from src.validate import validate_weather_response


def test_bad_api_payload_is_caught_by_validation():
    fake = Mock()
    fake.json.return_value = {"daily": {"time": ["2026-11-01"]}}  # temperatures missing
    with patch("requests.Session.get", return_value=fake):
        data = extract_weather_data(27.7172, 85.3240, "Asia/Kathmandu")
    with pytest.raises(ValueError, match="Missing required fields"):
        validate_weather_response(data)