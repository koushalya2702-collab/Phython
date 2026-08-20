#map(), filter(), and reduce() in Python
numbers=[1,2,3,4,5]
def square(x):
    return x**2
result=map(square,numbers)
print(list(result))

# #Using lambda with map
numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x * 2, numbers)
print(list(result))  

# Multiple iterables
a=[1,2,3]
b=[4,5,6]
result=map(lambda x,y:x+y,a,b)
print(list(result))


filter()

numbers = [1, 2, 3, 4, 5]
def is_even(x):
    return x % 2==0
result=filter(is_even,numbers)
print(list(result))

#Using lambda
numbers = [10, 25, 30, 47, 50]
result=filter(lambda x: x > 25,numbers)
print(list(result))

#reduce
from functools import reduce
numbers = [1, 2, 3, 4, 5]
def add(x,y):
    return x+y
result=reduce(add,numbers)
print(result)

#Product of numbers
from functools import reduce
numbers = [1, 2, 3, 4, 5]
result=reduce(lambda x,y:x*y,numbers)
print(result)

#Maximum value
from functools import reduce

numbers = [10, 20, 5, 8, 100, 3]

result=reduce(lambda a,b:a if a>b else b,numbers)
print(result)


# Processing Student Scores
from functools import reduce
scores=[45,67,89,34,76,90]
updated=list(map(lambda x:x+5,scores))
passed=list(filter(lambda x:x >= 50, updated))
total=reduce(lambda x,y:x+y,passed)

print("Updated Scores:", updated)
print("Passed Students:", passed)
print("Total Marks:", total)