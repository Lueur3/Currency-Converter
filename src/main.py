import sys
import os
import api
import converter
import validator


def check_exit(value: str):
    if value == "q":
        sys.exit()


data = {}
user_currency = ""
target_currency = ""
user_amount = ""

file_path = "data/cache.json"
folder_path = "data/"


print("Welcome to the currency converter!")

while True:
    print("\nEnter 'q' for exit.")
    user_currency = input("Enter the base currency code: ")
    check_exit(user_currency)

    target_currency = input("Enter the target currency code: ")
    check_exit(target_currency)

    user_amount = input("Enter the amount to convert: ")
    check_exit(user_amount)

    try:
        user_currency = validator.validate_currency_code(user_currency.rstrip()).upper()
        target_currency = validator.validate_currency_code(
            target_currency.rstrip()
        ).upper()
        user_amount = validator.validate_amount(user_amount)

        data = api.get_rates(user_currency)

        if target_currency not in data[user_currency]["rates"]:
            raise ValueError("Target currency not found in database.")

        result_convert = converter.convert(
            user_amount, data[user_currency]["rates"][target_currency]
        )

        print(f"Your result: {result_convert}")

    except ValueError as e:
        print(f"Error: {e}")
    except ConnectionError as e:
        print(f"Error: {e}")
    except TimeoutError as e:
        print(f"Error: {e}")
    except RuntimeError as e:
        print(f"Error: {e}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error has occurred: {e}")
