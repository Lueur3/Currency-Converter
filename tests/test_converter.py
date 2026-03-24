import pytest
from src.converter import convert


@pytest.mark.parametrize("amount, target, expected", [(278.322, 4.051142, 1127.522)])
def test_conver_round(amount, target, expected):
    assert convert(amount, target) == expected


@pytest.mark.parametrize("amount, target, expected", [(278, 4, 1112)])
def test_conver_int(amount, target, expected):
    assert convert(amount, target) == expected
