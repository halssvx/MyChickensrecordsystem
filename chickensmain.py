chickens = ["George", "Fleur", "Devon", "Casey", "Marigold", "Apple Mint"]

def print_menu():
    print("Chicken Record System")
    print("0 - Exit App")
    print("1 - Print List of Chicken Records")
    print("2 - Create New Chicken Record")
    print("3 - Update Existing Chicken Record")
    print("4 - Delete a Chicken Record")

def print_chickens():
    print("\nChicken Records:")
    for i, name in enumerate(chickens, start=1):
        print(f"{i}. {name}")
    print()

def add_chicken():
    name = input("Enter new chicken name: ").strip()
    if name:
        chickens.append(name)
        print(f"'{name}' added successfully.")
    else:
        print("Invalid name. Please try again.")

def update_chicken():
    print_chickens()
    try:
        index = int(input("Enter the number of the chicken to update: ")) - 1
        if 0 <= index < len(chickens):
            new_name = input("Enter new name: ").strip()
            chickens[index] = new_name
            print(f"Chicken {index + 1} updated to '{new_name}'.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_chicken():
    print_chickens()
    try:
        index = int(input("Enter the number of the chicken to delete: ")) - 1
        if 0 <= index < len(chickens):
            removed = chickens.pop(index)
            print(f"'{removed}' has been deleted.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print_menu()
        choice = input("\nEnter choice: ").strip()

        if choice == '0':
            print("Exiting program...")
            break
        elif choice == '1':
            print_chickens()
        elif choice == '2':
            add_chicken()
        elif choice == '3':
            update_chicken()
        elif choice == '4':
            delete_chicken()
        else:
            print("Invalid option.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
