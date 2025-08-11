# match case

month = int(input("enter any month: "))

match month:
    # combination of values
    case 1|3|5|7|8|12:
        print("31 Days")
    case 2:
        print("28/29 Days")
    case 4|9|11:
        print("30 Days")
    # default case
    case _:
        print("enter valid month")