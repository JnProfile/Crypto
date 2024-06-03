from enums.CryptoTypes import CryptoTypes
from exporters.ChangellyExporter import ChangellyExporter
from exporters.OneInchExporter import OneInchExporter

import csv
import argparse

parser = argparse.ArgumentParser(description='Process some API keys.')
parser.add_argument('--changelly_key',
                    required=True, help='API key for the changelly')
parser.add_argument('--one_inch_key',
                    required=True, help='API key for the 1inch')

args = parser.parse_args()

changelly_api_key = args.changelly_key
one_inch_api_key = args.one_inch_key

changelly = ChangellyExporter(api_key=changelly_api_key)
one_inch = OneInchExporter(api_key=one_inch_api_key)

tests = [
    {
        "exchange_token": CryptoTypes.ETHEREUM,
        "target_token": CryptoTypes.TETHER,
        "amount": 2570000000,
    },
    {
        "exchange_token": CryptoTypes.BITCOIN,
        "target_token": CryptoTypes.TETHER,
        "amount": 1450000000,
    },
    {
        "exchange_token": CryptoTypes.TETHER,
        "target_token": CryptoTypes.BITCOIN,
        "amount": 1234000000,
    }
]

for test in tests:
    file_name = f"results/{test['exchange_token'].name}_{test['target_token'].name}.csv"
    one_inch_price, one_inch_gas = one_inch.make_request(
        test["exchange_token"].value,
        test["target_token"].value,
        test["amount"]
    )
    changelly_price, changelly_gas = changelly.make_request(
        test["exchange_token"].value, test["target_token"].value, test["amount"]
    )
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "Exchange token -> Target token",
                "Amount",
                "Price 1inch",
                "Gas 1inch",
                "Price Changelly",
                "Gas Changelly",
            ]
        )
        writer.writerow(
            [
                f"{test['exchange_token'].name} -> {test['target_token'].name}",
                test["amount"],
                one_inch_price,
                one_inch_gas,
                changelly_price,
                changelly_gas,
            ]
        )
