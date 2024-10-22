# In a file called taqueria.py, implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.

def main():
    prices = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    calculate_prices(prices)


def calculate_prices(prices):
    price = 0
    # User while true
    while True:
        try:
            # Prompt user for items, one per line, until the user inputs control-d
            # Treat user input case sensitively
            # Enable user to place an order
            # Assume every item on the menu will be titlecased
            user_input = input("Item: ").title()
            # After each inputted item, display the total cost of all items inputted thus far, with a $ in front, formatted to 2 decimal places
            price += prices[user_input]
            # print("$",'{0:.2f}'.format(price))
            print(f"${price:.2f}")
        # Ignore any input that isn't an item - from the menu?
        except KeyError:
            pass
        except EOFError: # CTRL-D
            print("Order Complete")
            break

main()