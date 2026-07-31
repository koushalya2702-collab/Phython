#if,else,elif condition
age=int(input("enter your age:"))
if age <= 5:
    print("the bus pass is free")
elif age >= 60:
    print("get a senior citizen discount")
else:
    print("you may pay the full charge")


#meal time checker
time=input("Enter the time:")
if time == 8:
    print("its time for breakfast")
elif time == 13:
    print("its time for lunch")
elif time == 20:
    print("its time for dinner")
else:
    print("its not a meal time")

#Simple eligible check
age=int(input("enter your age:"))
if age <= 18:
    print("you may get a student membership")
elif age >= 60:
    print("you get a senior citizen membership")
else:
    print("they get a regular membership")


#nested if
day="sunday"
is_raining=False

if day == "sunday" or day == "saturday":
    if not is_raining:
        print("visit mysuru")
    else:
        print("its raining")
else:
    print("its another week day")