# implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0.
# If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting,
# and treat the user’s greeting case-insensitively.implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0.
# If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and
# treat the user’s greeting case-insensitively.


user_input = str(input("Please enter a greeting: ")).strip().lower()

if user_input.startswith("hello"):
    print("$0")
elif user_input.startswith("h"):
    print("$20")
else:
    print("$100")

# def starts_with(x, substring):
#     x=x.strip().lower()
#     prefix, _ , _ = x.partition(substring)
#     return prefix ==''
