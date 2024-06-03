from .APIExporter import APIExporter
from requests.exceptions import HTTPError

import requests


class ChangellyExporter(APIExporter):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.base_url = "https://dex-api.changelly.com/v1/1/price"

    def make_request(self, exchange_token, target_token, amount):
        try:
            params = {
                "fromTokenAddress": exchange_token,
                "toTokenAddress": target_token,
                "amount": amount,
                "slippage": "1",
            }

            headers = {"Authorization": f"Bearer {self.api_key}"}

            response = requests.get(
                self.base_url, headers=headers, params=params
            )
            response.raise_for_status()

            try:
                price = response.json().get("amount_out_total")
                estimated_gas = response.json().get("estimate_gas_total")
                return price, estimated_gas
            except Exception as error:
                print(f"Failed to parse price and estimated_gas: {error}")
        except HTTPError as error:
            print(
                f"Error catched due making request to Changelly API: {error}"
            )
