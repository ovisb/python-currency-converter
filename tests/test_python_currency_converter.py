from unittest.mock import patch

import pytest

from python_currency_converter.python_currency_converter import (
    exchange_money,
    get_currency_code,
    get_currency_data_from_url,
    get_money_to_exchange,
    init_cache,
)


@pytest.mark.parametrize(
    "user_input, expected",
    [
        ((20, 2), 40),
        ((128, 3.21), 410.88),
    ],
)
def test_exchange_money(user_input, expected):
    money, rate = user_input

    assert exchange_money(money, rate) == expected


@pytest.mark.parametrize(
    "user_input, expected",
    [
        ("42", 42.0),
        ("13", 13.0),
    ],
)
def test_get_money_input_valid(user_input, expected):
    with patch("builtins.input", side_effect=[user_input], return_value=expected):
        assert get_money_to_exchange() == expected


def test_get_money_input_invalid():
    expected_valid = 42.0
    with patch(
        "builtins.input",
        side_effect=["asd", "TEST", "XyZ", "42"],
        return_value=expected_valid,
    ):
        assert get_money_to_exchange() == expected_valid


@pytest.mark.parametrize(
    "user_input, expected",
    [
        ("USD", "USD"),
        ("EUR", "EUR"),
        ("", ""),
    ],
)
def test_get_currency_input_valid(user_input, expected):
    with patch("builtins.input", side_effect=[user_input], return_value=expected):
        assert get_currency_code() == expected


def test_get_currency_input_invalid():
    expected_valid = "USD"
    with patch(
        "builtins.input",
        side_effect=["123", "123A", "5", "USD"],
        return_value=expected_valid,
    ):
        assert get_currency_code() == expected_valid


# Test function using pytest
def test_get_currency_data_from_url(mock_requests_get):
    mock_response = {"key": "value"}
    mock_requests_get.return_value.json.return_value = mock_response

    result = get_currency_data_from_url("usd")

    assert result == mock_response

    expected_url = "http://www.floatrates.com/daily/usd.json"
    mock_requests_get.assert_called_once_with(expected_url)


def test_init_cache(mock_requests_get):
    mock_response = {"key": "value"}

    mock_requests_get.return_value.json.return_value = mock_response

    cache = init_cache()

    assert cache == {"eur": mock_response, "usd": mock_response}


@pytest.fixture
def mock_requests_get(monkeypatch):
    with patch("requests.get") as mock_get:
        yield mock_get
