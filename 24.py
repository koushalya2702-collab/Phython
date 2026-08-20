#match case statement

day = input("Enter the day:")
match day:
    case "monday":
        print("start of the work week")
    case "friday":
        print("almost weekend")
    case "saturday|sunday":
        print("it's weekend")
    case _:
        print("its just another day")
