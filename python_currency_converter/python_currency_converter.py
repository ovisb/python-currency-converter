"""Currency converter module"""
import requests


def init_cache() -> dict:
    """
    Initialize the cache with USD/EUR currencies
    """
    cache = {}
    cache.update({"eur": get_currency_data_from_url("EUR")})
    cache.update({"usd": get_currency_data_from_url("USD")})
    return cache


def get_money_to_exchange() -> float:
    """
    Get amount of money we want to exchange
    """
    while True:
        money = input()
        if is_money_input_valid(money):
            return float(money)
        print("Please enter only numbers.")


def is_money_input_valid(money: str) -> bool:
    """
    Validate input
    """
    return money.isnumeric()


def get_currency_code() -> str:
    """
    Get currency code from the user
    """
    while True:
        currency_input = input()
        if is_valid_currency_input(currency_input):
            return currency_input


def is_valid_currency_input(currency_input: str) -> bool:
    """
    Validate input
    """
    if currency_input == "":
        return True

    if not currency_input.isalpha():
        print("Please enter only letters.")
        return False

    return True


def exchange_money(money: float, exchange_rate: float) -> int | float:
    """
    Convert using exchange rate
    """
    conversion = money * exchange_rate

    return int(conversion) if conversion % 1 == 0 else conversion


def get_currency_data_from_url(currency_code: str) -> dict:
    """
    Get exchange info from specific currency_code
    get from http://www.floatrates.com/
    """
    currency_code = currency_code.lower()
    url = f"http://www.floatrates.com/daily/{currency_code}.json"
    response: requests.Response = requests.get(url)
    return response.json()
