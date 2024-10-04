# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything,
# outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.


user_input = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip().lower()

possible_answers = ["42", "forty-two", "forty two"]

if user_input in possible_answers:
    answer = "Yes"
else:
    answer = "No"

print(answer)



