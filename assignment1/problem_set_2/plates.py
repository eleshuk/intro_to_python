# PLATE REQUIREMENTS
    # “All vanity plates must start with at least two letters.”
    # “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    # “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    # “No periods, spaces, or punctuation marks are allowed.
# Implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

# Suggestion from class - use regex
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    import re
    # Uppercase letters - convert input to uppercase. Input will be a string, remove whitespace
    str(s.strip().upper())

    # Conditions:
        # First two characters are letters
        # Max 6 characters, min 2 characters
        # First number cannot be 0
        # No numbers in the middle of a plate, they must come at the end - AAA222 is good, AA22A is not
        # No periods, no punctuation, no spaces
        # One string can be all letters or a combination of letters and numbers

    # if re.match(r'^[a-zA-Z]{2}', s) and len(s) <=6 and len(s) >=2 and not s.startswith("0") and re.match(r'[a-zA-Z0-9\s]+$', s) and re.match(r'^[A-Za-z]+\d*$'):
    if re.match(r'^[A-Za-z]{2}[A-Za-z]*([1-9]\d*)?$', s) and len(s) <=6 and len(s) >=2:
        x = True
    else:
        x = False

    return x

main()
