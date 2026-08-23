#Homework
'''
Create a list of temperatures in Celsius: temps_c = [25, 30, 35, 40]
Use map() to convert them to Fahrenheit using the formula (°C×9/5)+32
Print the list of converted temperatures.

'''
temps_c = [25, 30, 35, 40]
temps_f=list(map(lambda c: (c * 9/5) + 32,temps_c))
print(temps_f)

'''
Create a list of city names: cities = ["Bengaluru", "Mysuru", "Mandya", "Hubballi", "Ballari", "Hassan"]
Use filter() to get all city names that start with the letter 'M'.
Print the resulting list
'''
cities = ["Bengaluru", "Mysuru", "Mandya", "Hubballi", "Ballari", "Hassan"]

result = list(filter(lambda city: city.startswith("M"), cities))

print(result)


'''
Given a list of student scores: scores = [45, 67, 89, 34, 76, 90]
Use reduce() to find the highest score in the list.
Print the highest score.

'''
from functools import reduce
scores = [45, 67, 89, 34, 76, 90]
result=reduce(lambda a,b: a if a > b else b,scores)
print(result)