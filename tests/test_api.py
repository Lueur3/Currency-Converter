import pytest
import requests
from src.api import get_data


def test_get_data_success(mocker):
    mock_response_data = {"result": "success", "rates": {"USD": 1.0, "EUR": 0.92}}
    mock_get = mocker.patch("src.api.requests.get")

    mock_get.return_value.json.return_value = mock_response_data
    mock_get.return_value.status_code = 200

    result = get_data("USD")
    assert "USD" in result
    assert result["USD"]["rates"]["EUR"] == 0.92
    assert "get_time" in result["USD"]
    mock_get.assert_called_once()


def test_get_data_no_internet(mocker):
    mock_get = mocker.patch("src.api.requests.get")

    mock_get.side_effect = requests.exceptions.ConnectionError

    with pytest.raises(ConnectionError, match="No internet connection."):
        get_data("USD")


def test_get_data_invalid_format(mocker):
    mock_get = mocker.patch("src.api.requests.get")

    mock_get.return_value.json.return_value = {"result": "success"}
    mock_get.return_value.status_code = 200

    with pytest.raises(KeyError, match="The API returned data in an invalid format."):
        get_data("USD")


def test_get_data_api_error(mocker):
    mock_get = mocker.patch("src.api.requests.get")

    mock_get.return_value.json.return_value = {"result": "error", "rates": {}}

    with pytest.raises(ValueError, match="Data retrieval error."):
        get_data("USD")


def test_get_data_timeout(mocker):
    mock_get = mocker.patch("src.api.requests.get")
    mock_get.side_effect = requests.exceptions.Timeout

    with pytest.raises(
        TimeoutError, match="The timeout for the server's response has expired."
    ):
        get_data("USD")


def test_get_data_http_error(mocker):
    mock_response = mocker.Mock()

    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError

    mocker.patch("src.api.requests.get", return_value=mock_response)

    with pytest.raises(
        ValueError, match="The specified currency is not supported in the API."
    ):
        get_data("UNKNOWN")


def test_get_data_unexpected_error(mocker):
    mock_get = mocker.patch("src.api.requests.get")
    mock_get.side_effect = requests.exceptions.RequestException

    with pytest.raises(
        RuntimeError,
        match="An unexpected error occurred while making a request to the API.",
    ):
        get_data("USD")
