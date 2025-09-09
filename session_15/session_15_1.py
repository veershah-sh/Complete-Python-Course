class FirstClass:
    # method
    def sayMyName(self, name):
        print(f"1. My name is {name}.")

class SecondClass:
    def sayMyName(self, name):
        print(f"2. My name is {name}.")

# object of class
object_1 = FirstClass()
object_2 = SecondClass()

object_1.sayMyName("Veer")
object_2.sayMyName("ABC")
