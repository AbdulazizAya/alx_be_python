def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            Name = input("Enter the Name of the Product: ")
            shopping_list.append(Name)
        elif choice == '2':
            # Prompt for and remove an item
            if len(shopping_list) != 0:
                Name = input("Enter the Name of the product to remove: ")
                shopping_list.remove(Name)
            else:
                print("Listing cart is empty!")
        elif choice == '3':
            # Display the shopping list
            if len(shopping_list) != 0:
                for item in shopping_list:
                    print(item)
            else:
                print("Empty List!")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()