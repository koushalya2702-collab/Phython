#function advanced
def display_info(name,age):
    print(f"Name:{name}, Age:{age}")
display_info(name="koushalya",age=99)

#variable length argument
def total_sum(*numbers):
    result=0
    for num in numbers:
        result+=num
    return result
print(total_sum(1,3,4,5,6,7))

#example
def student_info(**details):
    for key,value in details.items():
        print(f"{key}:{value}")
student_info(name="koushalya",age=89,course="phython")

#lambda function
double=lambda x:x*2
print(double(6))

#recursion
def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(8))

#nested function
def outer_function(name):
    def inner_function():
        print(f"hello {name}")
    inner_function()
outer_function("koushalya")