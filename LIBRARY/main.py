from services import library_service

while True:
    print("\n====== 📚 LIBRARY SYSTEM ======")
    print("1. Show Books")
    print("2. Add Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        library_service.show_books()
    elif choice == "2":
        library_service.add_book()
    elif choice == "3":
        library_service.issue_book()
    elif choice == "4":
        library_service.return_book()
    elif choice == "0":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")