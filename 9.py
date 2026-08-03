#for loop
cities=['bengaluru','mysuru','udupi','kundapura']
for city in cities:
    print(city)

#using for loop with range
for i in range(1,10,2):
    print(i)

#looping over strings
name="koushalya"
for ch in name:
    print(ch)

#nested for loop
for i in range(1,11):
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")
    print()

#using break in for loop
cities=['bengaluru','mysuru','udupi','kundapura']
for city in cities:
    if city == "mysuru":
        break
    print(city)

#using continue in for loop
cities=['bengaluru','mysuru','udupi','kundapura']
for city in cities:
    if city == "mysuru":
        continue
    print(city)


#looping through a list with enumerate()

cities=['bengaluru','mysuru','udupi','kundapura']
for idx,city in enumerate(cities):
    print(idx,city)


#multiple of 3
for i in range(1,31):
    if i%3==0:
        print(i)

#sum of first 10 numbers
sum=0
for i in range(1,11):
    sum+=i
    print(sum)

