from enum import Enum


class CryptoTypes(Enum):
    ETHEREUM = "0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
    TETHER = "0xdac17f958d2ee523a2206206994597c13d831ec7"
    BITCOIN = "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599"


if __name__ == "__main__":
    print(CryptoTypes.ETHEREUM.value)
    print(CryptoTypes.TETHER.value)
    print(CryptoTypes.BITCOIN.value)
