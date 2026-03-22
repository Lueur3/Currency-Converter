import requests
import time


def get_data(currency: str):
    try:
        response = requests.get(
            f"https://open.er-api.com/v6/latest/{currency.upper()}", timeout=5
        )
        response.raise_for_status()
        response_data = response.json()

        if "rates" not in response_data or not isinstance(response_data["rates"], dict):
            raise KeyError("The API returned data in an invalid format.")

        if response_data["result"] == "error":
            raise ValueError("Data retrieval error.")

        get_time = time.ctime()
        data = {}
        data["get_time"] = get_time
        data["rates"] = response_data["rates"]

        return data

    except requests.exceptions.ConnectionError:
        raise ConnectionError("No internet connection.")
    except requests.exceptions.Timeout:
        raise TimeoutError("The timeout for the server's response has expired.")
    except requests.exceptions.HTTPError:
        raise ValueError("The specified currency is not supported in the API.")
    except requests.exceptions.RequestException:
        raise RuntimeError(
            "An unexpected error occurred while making a request to the API."
        )
