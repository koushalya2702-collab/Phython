#looping through list
numbers=[1,2,3,4,5,90]
total=0
for num in numbers:
    total+=num
print("Total sum is:",total)

numbers=[2,3,4,5,6,9]
doubled=[]
for num in numbers:
    doubled.append(num*2)
print(doubled)

#looping through dictionaries
student_marks={
    "anand":89,
    "geeta":87,
    "kumar":90
}
for student in student_marks:
    print(student)

#looping through dictionaries
student_marks={
    "anand":89,
    "geeta":87,
    "kumar":90
}
for marks in student_marks.values():
    print(marks)



#looping through dictionaries
student_marks={
    "anand":89,
    "geeta":87,
    "kumar":90
}
for student,marks in student_marks.items():
    print(student,marks)

#for loop with range
student=["kavya","naveen","megha","pawan"]
marks=[45,66,88,99]
student_marks={}
for i in range(len(student)):
    student_marks[student[i]]=marks[i]
print(student_marks)

#list comprehension
numbers=[1,2,3,4,5]
squares=[num**2 for num in numbers]
print(squares)

#example
numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers=[num for num in numbers if num%2==0]
print(even_numbers)

#example
cities=["bengaluru","mysuru","mandya","madduru"]
uppercase=[city.upper() for city in cities]
print(uppercase)

#dictionary comprehension
numbers=[1,2,3,4,5,6]
squares_dict={num:num **2 for num in numbers}
print(squares_dict)

#example
names=["koushalya","koushik","kanaka","manasa"]
name_lengths={name:len(name) for name in names}
print(name_lengths)

#example
city_population={
    "bengaluru":99,
    "mandya":66,
    "mysuru":45,
    "kodagu":22
}
large_cities={city:population for city,population in city_population.items() if population > 50}
print(large_cities)

#splitting string to create lists
sentence="I love phython"
word=sentence.split()
print(word)

#example
data="apple,banana,mango"
fruits=data.split(",")
print(fruits)