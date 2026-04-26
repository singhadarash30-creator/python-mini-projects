from logic import *

while True:
    print("\n--- GAME MENU ---")
    print("1. Play")
    print("2. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        user = input("Enter stone/paper/scissors: ").lower()

        if user not in ["stone", "paper", "scissors"]:
            print("Invalid input")
            continue

        comp, result = play(user)
        print("Computer:", comp)
        print("Result:", result)

    elif ch == "2":
        break