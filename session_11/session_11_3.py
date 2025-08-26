import math

print("1. Find Square")
print("2. Find Cube")
print("3. Find Area of Circle")
print("4. Exit")

while(True):
    opt = int(input("Select option: "))
    if opt == 1:
        print("Find Square")
        num = int(input("Enter number: "))
        print(f"Square of {num} is {num*num}")
    elif opt == 2:
        print("Find cube")
        num = int(input("Enter number: "))
        print(f"Square of {num} is {num*num*num}")
    elif opt == 3:
        print("Find Area of Circle")
        radius = float(input("Enter radius: "))
        print(f"Area of Circle for radius {radius} is {math.pi * radius * radius}")
    elif opt == 4:
        print("Good Bye :)")
        break
    else:
        print("Select valid option")