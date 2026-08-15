#exception handling
try:
    a=int(input("Enter a number:"))
    print(10/a)
except ZeroDivisionError:
    print("You can't devide by zero")

#handling multiple exception
try:
    num=int(input("Enter a number:"))
    result=10/num
    print("result:",result)
except ZeroDivisionError:
    print("you con't devide by zero")
except ValueError:
    print("please enter the valid number")


#using finally
try:
    num=int(input("Enter a number:"))
    result=10/num
    print("result:",result)
except ZeroDivisionError:
    print("you con't devide by zero")
except ValueError:
    print("please enter the valid number")
finally:
    print("thank you")


#age varifier
try:
    age=int(input("ENter your age:"))
    years=100 - age
    print(f" he has another {years} years to complete his 100 years")
except ValueError:
    print("Enter the currect age")


#safe devider
try:
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number"))
    result=a/b
    print("result:",result)
except ZeroDivisionError:
    print("you con't devide by zero")
except ValueError:
    print("please enter the valid number")
finally:
    print("this is your answer")


#file reader
try:
    file=open("myfile.txt","r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("closing file")