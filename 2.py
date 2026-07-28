#  Input and Output in Python
name=input("Enter your name:")
age=int(input("Enter your age:"))
print("hello, "+ name +" you are " +str(age) +" years old ")
print(f"hello {name} you are {age} years old")


# String Manipulation(Concatenation,Repetition)
first_name="koushalya" 
second_name="narayana"
full_name=first_name + " "+ second_name
print(full_name)

#Repetition
greetings = "Hello! " * 5
print(greetings)


#String Methods:

message =" Hello, World!  "
print(message.upper())
print(message.lower())
print(message.strip())
print(message.replace("Hello","Hi"))

#Accessing String Characters:
text="koushalya"
print(text[5])
print(text[-2])
print(text[-3])
print(text[2])  

#Slicing Strings
text="Phython Programming"
print(text[0:5])
print(text[0:6])
print(text[:9])
print(text[0:])

#Escape Sequences
print("Hello\n\tWorld")
print("Hello\tWorld")

#Character Counter:
input="hello World"
print(len(input.replace(" ","")))