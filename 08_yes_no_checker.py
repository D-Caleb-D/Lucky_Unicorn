
show_instructions = ""
while show_instructions.lower() != "xxx":
    # ask the user if they have played the game before
    show_instructions = input("have you played the game before?").lower()

    # If they say yes, output 'program continues'
    # If they say no, output 'display instructions'
    # If answer is invalid, print an error

    if show_instructions =="yes" or show_instructions == "y":
        show_instructions = "yes"
        print("program contiues")

    elif show_instructions == "no" or show_instructions == "n":
        show_instructions = "no"
        print("display instructions")

    else:
        print("please answer yes / no")
