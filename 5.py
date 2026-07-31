#Tuples(accessing tuple element)
fruits=("apple","banana","grapes","kivi")
print(fruits[1])
print(fruits[-2])

#tuples operations
tuple1=(1,2,3)
tuple2=(4,5,6)
combine_tuple=tuple1+tuple2
print(combine_tuple)

repeated_tuple=(1,2)*5
print(repeated_tuple)

#tuple methods
tuple1=(1,23,4,5,6,1)
print(tuple1.count(1))
print(tuple1.index(6))


#sets
set1={1,2,3}
set2={4,5,6}
union_set=set1 | set2
print(union_set)

set1={1,2,3}
set2={2,3,6}
intersection_set=set1 & set2
print(intersection_set)

set1={1,2,3}
set2={3,5,6}
difference_set=set1-set2
print(difference_set)

set1={1,2,3}
set2={3,5,6}
sym_diff_set=set1 ^ set2
print(sym_diff_set)

#set methods
fruits={"apple","banana","grapes","kivi"}
fruits.add("guva")
print(fruits)

fruits={"apple","banana","grapes","kivi"}
fruits.remove("kivi")
print(fruits)

fruits={"apple","banana","grapes","kivi"}
fruits.pop()
print(fruits)

fruits={"apple","banana","grapes","kivi"}
fruits.discard("lemon")
print(fruits)



