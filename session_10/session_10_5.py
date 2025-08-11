# match case

month = int(input("enter month: "))
day = int(input("enter any day: "))

match day:
    case 1|2|3|4|5:
        print("Week Day")
        
    case 1|2|3|4|5 if month == 1:
        print("Week Day of January")

    case 6|7:
        print("weekend")
    # default case
    case _:
        print("enter valid day")