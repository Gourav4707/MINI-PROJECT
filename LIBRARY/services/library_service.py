books = {
    "Python": {"available": True},
    "DSA": {"available": True},
    "Physics": {"available": True},
    "Maths": {"available": False},
    "Chemistry": {"available": False}
}

issued_books = {}

def show_books():
    print("\nAvailable Books:")
    for book, data in books.items():
        status = "Available" if data["available"] else "Issued"
        print(f"{book} - {status}")

def add_book():
    name = input("Enter book name: ")
    books[name] = {"available": True}
    print("Book added successfully!")

def issue_book():
    name = input("Enter book name: ")
    if name in books and books[name]["available"]:
        student = input("Enter student name: ")
        days = int(input("Enter days to issue: "))
        
        books[name]["available"] = False
        issued_books[name] = {
            "student": student,
            "days": days
        }
        print("Book issued successfully!")
    else:
        print("Book not available!")

def calculate_fine(days_late):
    fine = 0
    for i in range(1, days_late + 1):
        fine += 10 * i
    return fine

def return_book():
    name = input("Enter book name: ")
    if name in issued_books:
        extra_days = int(input("Enter extra days (0 if on time): "))
        
        if extra_days > 0:
            fine = calculate_fine(extra_days)
            print(f"Late return! Fine = ₹{fine}")
        else:
            print("Returned on time!")

        books[name]["available"] = True
        del issued_books[name]
    else:
        print("Invalid book name!")
