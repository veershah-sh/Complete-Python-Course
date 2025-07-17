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


new_nums = [1,2,3,4,2,2]

nn = new_nums.copy()

new_nums.append(5)

nn_new = new_nums.copy()

print(nn)
print(nn_new)

# count() will return total num of instances of any value in a list
# it that value is not available than it will return "0"
count = new_nums.count(1000)
print(count)

new_nums.append([10,11,12])
print(new_nums)

new_nums.extend([13,14,15])
print(new_nums)

# new_nums = [1,2,3,4,2,2]

# index() returns the first index position of any value 
# but if the value is not available than it will raise an error
# list.index(*value, ?startPosition, ?endPosition)

pos = new_nums.index(2, 2, 7)
print(pos)

# [1, 2, 3, 4, 2, 2, 5, [10, 11, 12], 13, 14, 15]
# insert() adds a value to the list at given index 
# and if the index is not available than it will add value at the end of the list
new_nums.insert(9, 3)
print(new_nums)

# pop() removes the value from the list of given position
# if the index is not specified than it will remove last value
new_nums.pop(7)
print(new_nums)

# remove() removes value from the list
# if value is not available than it will raise an error
# if you have multiple vlaues of same type than it will remove only one value at a time
new_nums.remove(2)
print(new_nums)
new_nums.remove(2)
print(new_nums)


new_nums.reverse()
print(new_nums)

# sort() will sort the list in ascending / descending order 
# if there is any iterable(list, tuple, set, dict) in the list than it will throw an error

new_nums.sort(reverse=True)
print(new_nums)

# len() is used to find the length of any iterable
length = len(new_nums)
print("Length: ",length)

# it will only delete values from the list "not the list"
new_nums.clear()
print(new_nums)

new_nums.append(10)
print(new_nums)

# del will delete whole variable from the memory
del new_nums
# print(new_nums)

