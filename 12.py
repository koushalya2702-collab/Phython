#functions
def greet():
    print("hello world")
greet()

#function parameters
def greet_user(name):
    print(f"hello {name} welcome.")
greet_user("koushalya")

#returning values from a function
def add_numbers(a,b):
    return a+b
result=add_numbers(10,90)
print("result is:",result)

#default parameter values
def greet(name="student"):
    print(f"hey {name} welcome to the college")
greet()
greet("kavya")

#local and global variable
name="koushalya"
def greet():
    name="kavya"
    print(name)
greet()
print(name)