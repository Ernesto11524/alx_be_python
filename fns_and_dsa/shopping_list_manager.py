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
            item = input("What item do you want to add: ")
            shopping_list.append(item)
            pass
        elif choice == '2':
            item = input("What item do you want to eliminate: ")
            shopping_list.remove(item)
            pass
        elif choice == '3':
            lenth = len(shopping_list)
            for i in range(lenth):
                print(shopping_list[i])
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()