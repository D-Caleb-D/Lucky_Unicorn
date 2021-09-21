import random

# function goes here


def yes_no(question):

    valid = False
    while not valid:
        response = input(question).strip().lower()

        if response == "y" or response == "yes":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes or no")


def instructions():
    print()
    print("**** How To Play ****")
    print()
    print("Choose a starting amount (minimum $1, maximum $10)")
    print()
    print("Then press <ENTER> to play. You will be given a token. \n"
          "The 4 tokens are Horse, Zebra, Donkey and Unicorn")
    print()
    print("The game will cost $1 per round. \n"
          "Depending on the token you get given you will receive varying amounts of money back")
    print()
    print("The payout rates are as follows")
    print("Unicorn - Balance will increase by $4")
    print("Horse - Balance will decrease by $0.5")
    print("Zebra - Balance will decrease by $0.5")
    print("Donkey - Balance will decrease by $1")
    return""


def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))

            # If the amount is too low / high give
            if low < response <= high:
                return response

        # output an error
            else:
                print(error)

        except ValueError:
            print(error)


def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = ("{} {} {}".format(sides, statement, sides))
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

# main routine


statement_generator("Welcome to the Lucky Unicorn game!", "*")

played_before = yes_no("Have you played before? ")

if played_before == "no":
    instructions()

print()

# Ask user how much they want to play with
how_much = num_check("How much would you like to play with? ", 0, 10)
print()
print("You will be spending ${}".format(how_much))

balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play ").lower()
while play_again == "":

    # increase number of rounds played
    rounds_played += 1

    # print round number
    print()
    print("*** Round Number: {} ***".format(rounds_played))
    chosen_num = random.randint(1, 100)

    # adjust balance
    # if the random number is between 1 and 5,
    # user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        prize_decoration = "!"
        balance += 4
        # if the number is between 6 and 36
        # user gets a donkey (take away $1 from the balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        prize_decoration = "D"
        balance -= 1
    else:
         if chosen_num % 2 == 0:
            chosen = "horse"
            prize_decoration = "H"
         else:
             chosen = "zebra"
             prize_decoration = "Z"
         balance -= 0.5

    outcome = "You got a {}. Your balance is ${:.2f}".format(chosen, balance)

    statement_generator(outcome, prize_decoration)

    if balance < 1 or play_again == "xxx":
        play_again = "xxx"
        statement_generator("Sorry, you have run out of money", ".")
        print()

    else:
        play_again = input("Press Enter to play again or enter 'xxx' to quit")

statement_generator("Results", "-")
print()
print("Starting Balance ${}".format(how_much))
print("Final Balance ${}".format(balance))
print("Total Money Gained ${}".format(balance - how_much))
print("Thank you for playing the lucky unicorn game!")
