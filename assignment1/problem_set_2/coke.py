# only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.
# implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

def main():
    calculate_change()

def calculate_change():
    # user_input = 0
    # Limit accepted denominations to 25, 10, 5
    accepted_denomination = [25,10,5]
    # Starting amount
    starting_amount = 50

    # Loop through while the value of the starting amount
    while starting_amount > 0:
        print(f"Amount Due: {starting_amount}")

        user_input = int(input("Insert Coin: "))

        # Check if the user input is an accepted denomination
        if user_input in accepted_denomination:
            # remaining = starting_amount - user_input

            # Return the remaining value based on the starting amount, the updated starting amount, and the user input
            starting_amount -= user_input

            # print(remaining)
            # print(f"Amount due: {starting_amount}")

            # if starting_amount >= 0:
            #     print(f"Amount due: {starting_amount}")
            if starting_amount <= 0:
                # Value of changed owed should be positive
                print(f"Change Owed: {-(starting_amount)}")


main()





