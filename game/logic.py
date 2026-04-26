import random

def play(user):
    options = ["stone", "paper", "scissors"]
    comp = random.choice(options)

    if user == comp:
        return comp, "Draw"
    elif (user == "stone" and comp == "scissors") or \
         (user == "paper" and comp == "stone") or \
         (user == "scissors" and comp == "paper"):
        return comp, "You Win"
    else:
        return comp, "Computer Wins"