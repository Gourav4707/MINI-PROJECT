from services import game_services

while True:
    print("\n--- GAME MENU ---")
    print("1. Stone Paper Scissors")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        game_services.play_game()
    elif choice == "0":
        break
    else:
        print("Invalid choice!")
