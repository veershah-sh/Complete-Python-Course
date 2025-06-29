# implicit type cast
num = int(input("Enter any number: "))

print(type(num))
print(f"The cube of {num} is {num*num*num}")

num1 = input("Enter another number: ")

# explicit type cast
print(float(num1) * 2)