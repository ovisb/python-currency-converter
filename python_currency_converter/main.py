"""Main module"""
from python_currency_converter import (  # type: ignore
    exchange_money,
    get_currency_code,
    get_currency_data_from_url,
    get_money_to_exchange,
    init_cache,
)


def main() -> None:
    """Main function"""

    cache = init_cache()

    current_currency = get_currency_code().lower()

    while True:
        exchanged_currency = get_currency_code().lower()

        if not exchanged_currency:
            return

        money = get_money_to_exchange()

        print("Checking the cache...")
        if cache.get(exchanged_currency):
            print("Oh! It is in the cache!")
            exchage_rate = cache[exchanged_currency][current_currency]["inverseRate"]

            amount = round(exchange_money(money, exchage_rate), 2)
        else:
            print("Sorry, but it is not in the cache!")
            exchanged_currency_info = get_currency_data_from_url(exchanged_currency)
            cache.update({exchanged_currency: exchanged_currency_info})
            exchange_rate = exchanged_currency_info[current_currency]["inverseRate"]
            amount = round(exchange_money(money, exchange_rate), 2)

        print(f"You received {amount} {exchanged_currency}.")


if __name__ == "__main__":
    main()
