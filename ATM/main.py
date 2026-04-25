from service import atm_service

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Statement")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        atm_service.check_balance()
    elif choice == "2":
        atm_service.deposit()
    elif choice == "3":
        atm_service.withdraw()
    elif choice == "4":
        atm_service.show_statement()
    elif choice == "0":
        break
    else:
        print("Invalid choice!")
      
