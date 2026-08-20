
#import module
import math
print(math.sqrt(25))


#from module import function
from math import pow
print(pow(4,2))

#Popular Libraries in Python:
import random
print(random.randint(1,10))


#Using External Libraries
import wikipedia
print(wikipedia.summary("virat kohli"))


#Use the random module to pick a winner from a list of names.
import random
names=["koushalya","navya","pooja","kavya"]
winner=random.choice(names)
print(f"winner is {winner}")

'''
Math Helper
Use the math module to:
Find square root of 81
Get factorial of 6
Get pi value and multiply by 2
'''
import math
print(math.sqrt(81))
print(math.factorial(6))
print(math.pi*2)

