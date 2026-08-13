#list(accessing list elements)
fruits=["banana","apple","Cherry"]
print(fruits[0])
print(fruits[-1])

#Modify the list
animals=["Cat","Dog","Horse","Rat"]
animals.append("Ox")
print(animals)

animals=["Cat","Dog","Horse","Rat"]
animals.insert(1,"Donkey")
print(animals)

animals=["Cat","Dog","Horse","Rat"]
animals.remove("Cat")
print(animals)

animals=["cat","Dog","Horse","Rat"]
animals.pop(2)
print(animals)

animals=["cat","Dog","Horse","Rat"]
animals.pop()
print(animals)

animals=["cat","Dog","Horse","Rat"]
animals.clear()
print(animals)


#Slicing the list
animals=["Cat","Dog","Horse","Rat"]
print(animals[1:4])
print(animals[2:])
print(animals[0:4:2])

#List functions
animals=["Cat","Dog","Horse","Rat"]
print(len(animals))


numbers=[2,4,6,5,3]
print(sorted(numbers))
print(sum(numbers))


#Common method
animals=["Cat","Dog","Horse","Rat"]
print(animals.index("Dog"))
print(animals.count("Cat"))

numbers=[2,4,6,5,2,2,3]
print(numbers.count(2))
numbers.reverse()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
numbers.sort()
print(numbers)

#Nested list
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[1][2])
