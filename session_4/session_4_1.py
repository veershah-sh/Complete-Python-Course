# set {}

"""
    1. It stores only unique values.
    2. It do not have a sequence. 
    (It do not support indexing.)
"""

a = {1,4,2,6,4}

print(type(a))
print(a)

fruits = {"apple", "kiwi", "banana", "orange"}
print(fruits)

# methods of set

# unary methods

# add() -> to add value to the set
a.add(40)
# print(a)

copy_a = a.copy()
print(copy_a)

# discard() -> to remove a value from the set
# if value is not available than it will not delete any value
a.discard(20)
print(a)

# remove() -> to remove a value from the set
# if value is not available than it will raise an error
a.remove(4)
print(a)

# pop() -> removes "first" value of the set
a.pop()
print(a)

fruits.pop()
print(fruits)

# update() -> used to add values to set
a.update([31,32,33])
print(a)

# [] -> empty list
# () -> empty tuple
# {} -> empty dictonary
# set() -> empty set

a.clear()
print(a)