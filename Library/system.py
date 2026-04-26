books = {
    "python": {"available": True},
    "java": {"available": True},
    "c++": {"available": True}
}

issued = {}

def issue_book(book, student, days):
    if book in books and books[book]["available"]:
        books[book]["available"] = False
        issued[book] = {"student": student, "days": days}
        return "Book Issued"
    return "Book Not Available"

def return_book(book, late_days):
    if book in issued:
        fine = late_days * 10   # ₹10 per day
        books[book]["available"] = True
        del issued[book]
        return f"Returned successfully. Fine: {fine}"
    return "Invalid Book"

def show_books():
    return books