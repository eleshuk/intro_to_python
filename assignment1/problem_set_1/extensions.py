# In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if
# the file’s name ends, case-insensitively, in any of these suffixes:
def main():
    user_input = str(input("Input file name ").strip().lower())
    # extensions(user_input)
    extensions_concise(user_input)

def extensions(x):
    # Create conditions that return the appropriate category based on the user input
    if x.endswith("jpeg"):
        print("image/jpeg")
    elif x.endswith(".jpg"):
        print("image/jpeg")
    elif x.endswith(".png"):
        print("image/png")
    elif x.endswith(".pdf"):
        print("application/pdf")
    elif x.endswith(".gif"):
        print("image/gif")
    elif x.endswith(".txt"):
        print("text/plain")
    elif x.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")


def extensions_concise(x):
    # Use split to split out the components of the file name by the .
    # Then elect the last item from the list returned by split
    extension = x.split('.')[-1]

    # .png, .gif, .jpg, .jpeg, are all in the same category
    images = ["png", "gif", "jpg", "jpeg"]
    # .pdf and .zip are all in the same category
    applications = ["pdf", "zip"]

    # Check if the user input is in the "images" list
    if extension in images:
        # If it is, then print a string that combines "image/" with the extension
        # Need to add a conditional here that converts the .jpeg to .jpg when the extension is returned
        if extension == "jpg":
            extension = "jpeg"
        else:
            extension == extension
        print(f"image/{extension}")
    # Check if extension is in "applications" list
    elif extension in applications:
        print(f"application/{extension}")
    # Check if extension is "txt"
    elif extension == "txt":
        print("text/plain")
    # Otherwise return "application/octet-stream"
    else:
        print("application/octet-stream")

main()
