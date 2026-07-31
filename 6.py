#Dictionaries(accessing dictionary element)
karnataka_food={
    "Mysuru":"Mysore Pak",
    "Bengaluru":"Bisi Bele Bath",
    "Mangaluru":"Neer Dosa"
}
print(karnataka_food.get("Mysuru"))
print(karnataka_food.get("shivamogga","Not Found"))


#Adding and updating dictionary element
karnataka_food={
    "Mysuru":"Mysore Pak",
    "Bengaluru":"Bisi Bele Bath",
    "Mangaluru":"Neer Dosa"
}
karnataka_food["kundapura"]="kunda"
print(karnataka_food)

karnataka_food={
    "Mysuru":"Mysore Pak",
    "Bengaluru":"Bisi Bele Bath",
    "Mangaluru":"Neer Dosa"
}
karnataka_food["Mysuru"]="Ragi Mudde"
print(karnataka_food)


karnataka_food={
    "Mysuru":"Mysore Pak",
    "Bengaluru":"Bisi Bele Bath",
    "Mangaluru":"Neer Dosa"
}
print(karnataka_food.pop("Mysuru"))


karnataka_food={
    "Mysuru":"Mysore Pak",
    "Bengaluru":"Bisi Bele Bath",
    "Mangaluru":"Neer Dosa"
}
del karnataka_food["Mangaluru"]
print(karnataka_food)

#Dictionary Methods
karnataka_food={
    "Mysuru":"Mysore Pak",
    "Bengaluru":"Bisi Bele Bath",
    "Mangaluru":"Neer Dosa"
}
print(karnataka_food.keys())


karnataka_food={
    "Mysuru":"Mysore Pak",
    "Bengaluru":"Bisi Bele Bath",
    "Mangaluru":"Neer Dosa"
}
print(karnataka_food.values())

karnataka_food={
    "Mysuru":"Mysore Pak",
    "Bengaluru":"Bisi Bele Bath",
    "Mangaluru":"Neer Dosa"
}
print(karnataka_food.items())

karnataka_food={
    "Mysuru":"Mysore Pak",
    "Bengaluru":"Bisi Bele Bath",
    "Mangaluru":"Neer Dosa"
}
new_dishes={"Hubballi":"Girmit"}
karnataka_food.update(new_dishes)
print(karnataka_food)


#Basic dictionary operation
cities={
    "sagara":"benne dose",
    "mysuru":"mysuru pak",
    "karnataka":"kunda",
    "shimogga":"vade",
    "kerala":"kadubu"
}
cities["mandya"]="kabbu"
print(cities)
cities["sagara"]="vada pav"
print(cities)
del cities["mysuru"]
print(cities)


#Nested dictionary
friends={
    "kavita":{
       " sub":"maths",
       "food":"biriyani",
    },
    "mahesh":{
        "sub":"science",
        "food":"kabab",
    }
}
print(friends["kavita"]["food"])