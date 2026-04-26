from system import *

while True:
    print("\n--- LIBRARY MENU ---")
    print("1. Show Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        print(show_books())

    elif ch == "2":
        b = input("Book name: ").lower()
        s = input("Student name: ")
        d = int(input("Days: "))
        print(issue_book(b, s, d))

    elif ch == "3":
        b = input("Book name: ").lower()
        late = int(input("Late days: "))
        print(return_book(b, late))

    elif ch == "4":
        break