# Even so, in a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.

# Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.

import sys
def count_lines():
    try:
        # if len(sys.argv) > 1 and len(sys.argv) < 2 and sys.argv[1].endswith(".py"):
        if len(sys.argv) == 2 and sys.argv[1].endswith(".py"):
            with open(sys.argv[1], 'r') as fp:
                lines = [line for line in fp if line.strip() and not line.strip().startswith('#')]
                total_lines = len(lines)
                print(total_lines)
        elif len(sys.argv) < 2:
            # print("Too few command-line arguments")
            sys.exit("Too few command-line arguments")
        elif not sys.argv[1].endswith(".py"):
            sys.exit("Not a Python file")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")

    except FileNotFoundError:
        sys.exit("File does not exist")

count_lines()