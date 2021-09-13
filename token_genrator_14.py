import random

# main routine goes here
tokens = ["unicorn", "horse", "horse", "horse",
          "donkey", "donkey", "donkey",
          "zebra", "zebra", "zebra"]
STARTING_BALANCE = 100

balance = STARTING_BALANCE
# Testing loop to generate tokens
for item in range(0, 500):
    chosen = random.choice(tokens)

    # adjust balance
    if chosen == "unicorn":
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5

print()
print("Starting balance: ${:.2f}".format(STARTING_BALANCE))
print("Final balance: ${:.2f}".format(balance))
