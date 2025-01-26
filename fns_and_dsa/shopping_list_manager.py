# shopping_list = []
#
# menu = input("Type 'add' to add an item, 'remove' to remove an item, 'view' to view the list, or 'exit' to exit: ")
# while menu != "exit":
#     if menu == "add":
#         add_item = input("Enter item's name: ")
#         shopping_list.append(add_item)
#         menu = input(
#             "Type 'add' to add an item, 'remove' to remove an item, 'view' to view the list, or 'exit' to exit: ")
#
#     elif menu == "remove":


#             menu = input(
#                 "Type 'add' to add an item, 'remove' to remove an item, 'view' to view the list, or 'exit' to exit: ")
#
#     elif menu == "view":

#         menu = input("Type 'add' to add an item, 'remove' to remove an item, 'view' to view the list, or 'exit' to exit: ")
#
#     else:
#         print("Invalid choice, please try again")

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
            add_item = input("Enter the item to add: ")
            shopping_list.append(add_item)
            pass

        elif choice == '2':
            item_name = input("What item do you want to remove?: ")
            if item_name in shopping_list:
                shopping_list.remove(item_name)
            else:
                print(f"{item_name} is not in your shopping list")
            pass

        elif choice == '3':
            print(shopping_list)
            pass

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



