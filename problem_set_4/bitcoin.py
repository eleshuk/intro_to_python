# Expects the user to specify as a command-line argument the number of Bitcoins, n, that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
# Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:

# Outputs the current cost of Bitcoins in USD to four decimal places, using , as a thousands separator.


import requests
import sys

# Need function to read the commandline input
# The list of command line arguments passed to a Python script. argv[0] is the script name (it is operating system dependent whether this is a full pathname or not)

def main():
    x=read_command_line_input()
    price=get_bitcoin_price()
    print(f"${x*price:,.4f}")

def read_command_line_input():
    cmd_line_arg = float(sys.argv[1])
    return cmd_line_arg


def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        # Get current pricedata from json file
        data = response.json()
        price_usd = data['bpi']['USD']['rate_float']

    except IndexError:
        sys.exit('Missing argument')
    except requests.RequestException:
        sys.exit('Request failed')

    return price_usd

main()