#Operators in Python
a=8
b=6
print(a==b)
print(a!=b)
print(a>b)
print(a<b)

#Logical operaters
x=5
y=9
print(x>0 and y>5)
print(x>4 or y<7)

#Membership operater
my_list=[1,2,3,4]
my_string="koushalya"
print(9 in my_list)
print("z" not in my_string)

#Logical operater practice
x=int(input("Enter the number:"))
y=int(input("Enter the second number:"))
print(x>10 and y>10)
print(x>10 or y<5)
print(not(x>y))

#Comparison operater
x=int(input("Enter your age:"))
if x >= 18:
    print("You are an adult")
else:
    print("You are a minor")
