# # Homework
# name1=input("Enter friend 1 name:")
# name2=input("Enter friend 2 name:")
# name3=input("Enter friend 3 name:")
# with open("friends.txt","w") as file:
#     file.write(name1 + "\n")
#     file.write(name2+ "\n")
#     file.write(name3 + "\n")


# #append marks
# name = input("Enter student name: ")
# marks = input("Enter marks: ")

# with open("marks.txt", "a") as file:
#     file.write(name + " - " + marks + "\n")

# print("Student marks added successfully!")



# #Read and Count Lines
# filename=input("Enter the filename:")
# with open(filename,"r") as file:
#     line=file.readlines()
#     print("Number of lines:",len(line))


#search from file
name=input("Enter name to search:")
with open("friends.txt","r") as file:
    friends=file.readlines()
found=False
for friend in friends:
    if friend.strip()==name:
        found=True
        break
if found:
    print("found")
else:
    print("not found")

