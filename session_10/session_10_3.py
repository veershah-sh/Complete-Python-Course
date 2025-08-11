# match case

day = int(input("enter any day: "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    # default case
    case _:
        print("enter valid day")