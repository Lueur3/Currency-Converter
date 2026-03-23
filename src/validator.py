def validate_amount(amount: str):
    try:
        amnt = float(amount)
        if amnt <= 0:
            raise ValueError("The value entered must be greater than zero.")

        return amnt

    except ValueError:
        raise ValueError("Invalid value. Please enter a number.")


def validate_currency_code(code: str):
    if len(code) != 3:
        raise ValueError("The code entered is the wrong length.")

    if not code.isalpha() or not code.isascii():
        raise ValueError(
            "The code must consist only of letters from the Latin alphabet"
        )

    return code
