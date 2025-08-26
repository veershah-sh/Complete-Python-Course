my_list = ["apple", "mango", "orange"]
item_to_update = input("Enter item to update: ")
if item_to_update not in my_list:
    print("Item is not in list.")
else:
    item_index = my_list.index(item_to_update)
    updated_item = input("Enter updated value: ")
    my_list[item_index] = updated_item
    print(my_list)