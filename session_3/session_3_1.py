# List Datatype

# declare / define a list
values = [39, True, None, "name", 54.30, 39]

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

count = values.count(39)
print(count)

values.extend(["a", "b", "c"])
print(values)

print(values.index(39))
print(values.index(39, 1))

# print(values.index(40))

values.insert(3, "python")
print(values)

# pop will remove the last value form the list by default
values.pop(5)
print(values)

values.remove('apple')
print(values)

values.reverse()
print(values)


nums = [10, 43, 65, 83, 1, 25]
# in acesnding order
nums.sort()
print(nums)
# in descending order
nums.sort(reverse=True)
print(nums)

# clear() delets all the values form the list
values.clear()
print(values)

#  del keyword delets whole list
del values
# print(values)
