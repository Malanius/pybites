VALID_COLORS = ["blue", "yellow", "red"]


def print_colors():
    """In the while loop ask the user to enter a color,
    lowercase it and store it in a variable. Next check:
    - if 'quit' was entered for color, print 'bye' and break.
    - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
    - otherwise print the color in lower case."""
    while True:
        color_input = input("Enter color: ")
        if color_input.lower() == "quit":
            print("bye")
            break
        if color_input.lower() not in VALID_COLORS:
            print("Not a valid color")
        else:
            print(color_input.lower())
