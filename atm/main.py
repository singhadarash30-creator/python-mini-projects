from operations import *

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Statement")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Balance:", check_balance())

    elif choice == "2":
        amt = int(input("Enter amount: "))
        deposit(amt)

    elif choice == "3":
        amt = int(input("Enter amount: "))
        result = withdraw(amt)
        if result:
            print(result)

    elif choice == "4":
        print(get_statement())

    elif choice == "5":
        break