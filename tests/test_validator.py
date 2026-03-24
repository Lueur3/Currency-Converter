import pytest
from src.validator import validate_amount, validate_currency_code


def test_valid_type_except():
    with pytest.raises(ValueError):
        validate_amount("uuu")


@pytest.mark.parametrize("amount, expected_type", [("123", float)])
def test_valid_type(amount, expected_type):
    assert isinstance(validate_amount(amount), expected_type)


def test_valid_negative_num():
    with pytest.raises(ValueError):
        validate_amount("-123")


@pytest.mark.parametrize("code", ["uu", "uuuu"])
def test_valid_code_len(code):
    with pytest.raises(ValueError, match="The code entered is the wrong length."):
        validate_currency_code(code)


@pytest.mark.parametrize("code", ["u13", "1us", "#$S"])
def test_valid_code_cont(code):
    with pytest.raises(
        ValueError,
        match="The code must consist only of letters from the Latin alphabet",
    ):
        validate_currency_code(code)
