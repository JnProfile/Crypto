from .APIExporter import APIExporter
from requests.exceptions import HTTPError

import requests


class OneInchExporter(APIExporter):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.base_url = "https://api.1inch.dev/swap/v6.0/1/quote"

    def make_request(self, exchange_token, target_token, amount):
        try:
            params = {
                "src": exchange_token,
                "dst": target_token,
                "amount": amount,
                "includeGas": "true",
            }

            headers = {"Authorization": f"Bearer {self.api_key}"}

            response = requests.get(
                self.base_url, headers=headers, params=params
            )
            response.raise_for_status()

            try:
                price = response.json().get("dstAmount")
                estimated_gas = response.json().get("gas")
                return price, estimated_gas
            except Exception as error:
                print(f"Failed to parse price and estimated_gas: {error}")
        except HTTPError as error:
            print(
                f"Error catched due making request to 1Inch API: {error}"
            )
