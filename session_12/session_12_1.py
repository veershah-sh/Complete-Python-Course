# list operations

my_list = []

print("1. Add Item")
print("2. Add Items")
print("3. Update Item")
print("4. Delete Item")
print("5. Clear List")
print("6. Show List")
print("7. Length Of List")
print("8. Exit")

while(True):
    opt = int(input("Select option: "))

    if opt == 1:
        item = input("Enter item to add: ")
        my_list.append(item)
        print(f"{item} added to list.")
    elif opt == 2:
        print("Type 'quit' to exit the loop")
        while(True):
            list_item = input("Enter item to add: ")
            # positive conditioning
            # if(list_item == "quit" or list_item == "Quit"):
            #     break
            # else:
            #     my_list.append(list_item)
                # print(f"{item} added to list.")

            # negative conditioning
            # if(list_item != "quit"):
            #     my_list.append(list_item)
                # print(f"{item} added to list.")
            # else:
            #     break

            if(list_item.lower() != "quit"):
                my_list.append(list_item)
                print(f"{list_item} added to list.")
            else:
                break
    elif opt == 3:
        item_to_update = input("Enter item to update: ")
        if item_to_update not in my_list:
            print("Item is not in list.")
        else:
            item_index = my_list.index(item_to_update)
            updated_item = input("Enter updated value: ")
            my_list[item_index] = updated_item
            print(f"{item_to_update} updated with {updated_item}.")
    elif opt == 4:
        item_to_delete = input("Enter item to delete: ")
        if item_to_delete not in my_list:
            print("Item is not in list.")
        else:
            # if you want to delete using index
            item_index = my_list.index(item_to_delete)
            my_list.pop(item_index)
            print(f"{item_to_delete} deleted from list.")

            # if you want to delete using value
            # my_list.remove(item_to_delete)
    elif opt == 5:
        approval = input("Are you sure to clear the list?(yes/no): ")
        if approval.lower() == "yes":
            my_list.clear()
            print(f"{my_list} is cleared.")
        else:
            print("Thank you for conforming.")
    elif opt == 6:
        print(my_list)
    elif opt == 7:
        print(f"Items available in list: {len(my_list)}")
    elif opt == 8:
        print("Good Bye :))")
        break
    else:
        print("select valid option.")