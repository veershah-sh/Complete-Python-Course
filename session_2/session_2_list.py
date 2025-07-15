# list

cars = ["bmw", "mg", "ms", "honda"]

# print(cars)
# print(type(cars))

values_list = ["xyz", 2524, 3.14, True, None]
# print(values_list)
# print(type(values_list))

# Indexing
new_values_list = ["xyz", 2524, 3.14, True, None]
# print(new_values_list[0])
# print(new_values_list[-1])

# List methods

# Append method adds a value to the end of the list.

new_values_list.append("Computer")
new_values_list.append(23)

new_values_list.append([1,2,3])

nums = [4,5,6]
new_values_list.append(nums)


new_nums = [1,2,3,4]

nn = new_nums.copy()

new_nums.append(5)

nn_new = new_nums.copy()

print(nn)
print(nn_new)
