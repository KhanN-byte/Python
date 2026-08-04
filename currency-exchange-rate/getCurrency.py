"""Fetch the latest exchange rates for a user-supplied currency code."""

from __future__ import annotations

import json
import os
import sys
from pprint import pprint
from urllib import error, request

API_BASE_URL = "https://v6.exchangerate-api.com/v6"
API_KEY_ENVIRONMENT_VARIABLE = "EXCHANGE_RATE_API_KEY"


def fetch_rates(currency_code: str) -> dict:
    """Return the provider response for a three-letter currency code."""
    api_key = os.getenv(API_KEY_ENVIRONMENT_VARIABLE)
    if not api_key:
        raise RuntimeError(
            f"Set {API_KEY_ENVIRONMENT_VARIABLE} before running this script."
        )

    normalized_code = currency_code.strip().upper()
    if len(normalized_code) != 3 or not normalized_code.isalpha():
        raise ValueError("Currency code must contain exactly three letters.")

    url = f"{API_BASE_URL}/{api_key}/latest/{normalized_code}"
    try:
        with request.urlopen(url, timeout=15) as response:
            return json.load(response)
    except error.HTTPError as exception:
        if exception.code == 401:
            raise RuntimeError("The exchange-rate provider rejected the API key.") from exception
        if exception.code == 404:
            raise RuntimeError(
                f"No exchange-rate data was found for {normalized_code}."
            ) from exception
        raise RuntimeError(
            f"The exchange-rate request failed with status {exception.code}."
        ) from exception
    except error.URLError as exception:
        raise RuntimeError("The exchange-rate service could not be reached.") from exception


def main() -> int:
    currency_code = input("Base currency code (for example, USD): ")
    try:
        pprint(fetch_rates(currency_code))
    except (RuntimeError, ValueError) as exception:
        print(f"Error: {exception}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
