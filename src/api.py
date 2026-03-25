import requests
from datetime import datetime
import json
import os

FILE_PATH = "data/cache.json"
FOLDER_PATH = "data/"


def get_data(currency: str):
    try:
        response = requests.get(
            f"https://open.er-api.com/v6/latest/{currency}", timeout=5
        )
        response.raise_for_status()
        response_data = response.json()

        if "rates" not in response_data or not isinstance(response_data["rates"], dict):
            raise KeyError("The API returned data in an invalid format.")

        if response_data["result"] == "error":
            raise ValueError("Data retrieval error.")

        get_time = datetime.now().strftime("%c")
        data = {}
        data[currency] = {"get_time": get_time, "rates": response_data["rates"]}

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


def load_cache():
    if os.path.exists(FILE_PATH) and os.path.getsize(FILE_PATH) > 0:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                return data
            except json.JSONDecodeError:
                raise ValueError("Error receiving data.")
    return {}


def get_rates(currency: str):
    data_currs = load_cache()

    if currency in data_currs:
        now_time = datetime.now()
        last_time = datetime.strptime(data_currs[currency]["get_time"], "%c")
        diff_time = now_time - last_time
        hours_passed = int(diff_time.total_seconds() // 3600)

        if hours_passed < 24:
            return data_currs

    new_data = get_data(currency)
    save(new_data)
    return new_data


def save(data_currs: dict):

    os.makedirs(FOLDER_PATH, exist_ok=True)

    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
    else:
        data = {}

    data.update(data_currs)
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
