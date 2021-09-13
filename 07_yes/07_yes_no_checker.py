# ask user if they have played before...
show_instructions = input("Have you played this game before?")

# if they say yes, output 'program continues'
if show_instructions == "yes":
    print("Program continues")

elif show_instructions == "y":
      print("Program continues")

elif show_instructions == "no":
      print("Display instructions")

elif show_instructions == "n":
      print("Display instructions")

# if they say no, output 'display instructions'
else:
    print("Please enter yes / no")
