# nested if

menu = """
    1. Burger
    2. Pizza
    3. Cold Drinks
"""


print(menu)
opt = int(input("select option: "))

if opt == 1:
    burgers = """
    1. Cheese Burger
    2. Paneer Burger
    """
    print("Burger")
    print(burgers)
    item = int(input("select item: "))
    if item == 1:
        print("Cheese Burger")
    elif item == 2:
        print("Paneer Burger")
    else:
        print("select valid item.")

elif opt == 2:
    pizza = """
    1. Paneer Pizza
    2. Veggie Pizza
    """
    print("Pizza")
    print(pizza)
elif opt == 3:
    cold_drinks = """
    1. Coke
    2. Sprite
    """
    print("Cold Drinks")
    print(cold_drinks)
else:
    print("select valid option.")