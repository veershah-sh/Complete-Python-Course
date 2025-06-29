# List Datatype

# declare / define a list
values = [39, True, None, "name", 54.30]

# print a list
print(values)

# append - adds a value at the end of the list
values.append("apple")
values.append(30)
values.append(False)
values.append(["a", "b", "c"])


# copy - it creates and returns a shallow copy of your list
new_values = values.copy()

print(new_values)