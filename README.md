# Crypto Exchange Rate Fetcher

This project fetches the best crypto exchange rates from Changelly and 1inch APIs.

## Getting Started

These instructions will guide you on how to set up and run the project.

### Prerequisites

- Python 3.x
- `requests` library
- `argparse` library (usually comes with Python by default)

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/crypto-exchange-rate-fetcher.git
    cd crypto-exchange-rate-fetcher
    ```

2. Install the required libraries:

    ```sh
    pip install requests
    ```

### Usage

To run the script, use the following command:

```sh
python main.py --changelly_key XXXXXX --one_inch_key XXXXXX
```

### Results
The fetched results will be stored in the results folder. Each time the script is run, the results in this folder will be overwritten with the latest data.
