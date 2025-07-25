student = {
    "name": "abc",
    "qualification": "masters",
    "age": 25,
    "experience": 4.5,
    "isWorking": True
}

print(student)

# student = student.fromkeys(["a","b","c"], 0)
# print(student)

# student["name"] = 10
# print(student) 

# print(student.get("Name"))

value = student.get("name")

print(value)
# if value:
#     print(value)
# else:
#     print("Key not found!")

deleted_item = student.popitem()
print(deleted_item)
print(student)

student.pop("name")
print(student)

default_student = student.setdefault("fee", 3000)
print(student)

student["fee"] = 4000
print(student)

student.update({"age": 30, "fee": 5000})
print(student)

# keys
keys = student.keys()
print(keys)

# values
values = student.values()
print(values)

# items
items = student.items()
print(items)