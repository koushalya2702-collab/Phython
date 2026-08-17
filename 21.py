# Python File Modes
file=open("notes.txt","r")
print(file.read())
file.close()

# readline() 
file=open("notes.txt","r")
print(file.readline())
file.close()


#readlines()
file = open("notes.txt", "r")
lines = file.readlines()
print(lines)
file.close()


#Writing to a File
file=open("notes.txt","w")
file.write("Namaskara bengaluru!\n")
file.write("phython is awesome")
file.close()


#Appending to a File
file=open("notes.txt","a")
file.write("\nThis line is added later.")
file.close()


#Using with Statement (Best Practice)
with open("notes.txt","r") as file:
    content=file.read()
    print(content)

#Writing List of Data to File
students = ["Ravi", "Meena", "Dinesh"]
with open("students.txt", "w") as file:
    for student in students:
        file.write(student + "\n")

#Reading File and Processing Each Line
with open("students.txt", "r") as file:
    for line in file:
        print("Student:", line.strip())