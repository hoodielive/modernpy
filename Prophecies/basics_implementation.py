# Write a program that allows a user to add/delete items from a
# todolist. Display user input as list

def main():
    added = []
    while True:
        user_response = input("Type 'add' to insert items or 'delete' to remove items.\n(If you wish to quit type 'q')\n")
        if user_response == 'q':
            print("Bye Felicia!")
            exit()
        elif user_response == "add":
            added = add_items(added)
            print("\nTODO list:")
            for item in added:
                i = added.index(item) + 1
                print(f"{i}: {item}")
        elif user_response == 'delete' and len(added) == 0:
            delete_item(added)
            print("\nTODO list:")
            for item in added:
                i = added.index(item) + 1
                print(f"{i}: {item}")
        elif user_response == 'delete' and len(added) == 0 or 'add' or 'q':
            print("Please enter a valid input.")
        else:
            print("ERROR: You can not remove from an empty list.\n")

def add_items(user_list):
    while True:
        item = input("Please enter an item to add and type 'done' when finished\n")
        if item == 'done':
            break
        user_list.append(item)
    return user_list


def delete_item(item_list):

    del_item = input("\ntype the item you would like to delete\n")
    if del_item in item_list:
        item_list.remove(del_item)


main()
