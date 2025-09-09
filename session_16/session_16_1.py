class DemoClass:
    # default constructor
    def __init__(self):
        print("this is a constructor.")


class Auth:
    # parameterised constructor
    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password

    def printUserData(self):
        print(f"Username: {self.user_name}")
        print(f"Password: {self.user_password}")

    def __del__(self):
        print("destructor called")

dc = DemoClass()
a = Auth("Veer", "1234")
a1 = Auth("Shreyansh", "12345")
a.printUserData()
a1.printUserData()
