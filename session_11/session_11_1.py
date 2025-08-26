"""
    Looping Statements:
        1. Number based loop
            - for loop

        2. Condition based loop
            - while loop
"""

# for num in range(1,10+1):
#     # print(num)
#     print(num, end=" ")

start = int(input("Enter starting value: "))
end = int(input("Enter ending value: "))
step = int(input("Enter steps: "))

for num in range(start,end+1,step):
    # print(num)
    print(num, end=" ")
else:
    print("\nLoop Executed.")