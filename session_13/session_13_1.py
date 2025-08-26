# functions

"""
    Type Cases:
        1. Camel Case - userMarks, studentRollNumber
        (function name, object name)

        2. Pascel Case - EmployeeSalary, StudentName
        (Class name)

        3. Snake Case - maths_marks, python_code
        (variables)

        4. Kabab Case - build-in, python-leacture
        (variables)
"""

"""
    Types of Functions:
        1. System Default Functions(build-in functions)

        2. User Defined Functions
            - fn without argument & without return value
            - fn with argument & without return value
            - fn without argument & with return value
            - fn with argument & with return value

"""
# - fn without argument & without return value
def sayMyName():
    print("My name is veer.")

sayMyName()

# - fn with argument & without return value
def findTotal(n1,n2):
    print(f"Total is: {n1+n2}")

findTotal(10, 17)