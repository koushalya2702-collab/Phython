students=[]
def menu():
    print("\n--- Educational System ---")
    print("1. Add Student Details")
    print("2. Display Student Details")
    print("3. Exit")
while True:
    menu()
    choice=int(input("Enter your choice:"))
    if choice == 1:
        name=input("Enter your name:")
        age=int(input("Enter your age:"))
        course=input("Enter your course:")

        student={
            "name": name,
            "age": age,
           "course":course
        }
        students.append(student)
        print("Student added successfully")
    elif choice == 2:
        if len(students)==0:
            print("No student details available.")
        else:
            print("\n--- Student Details ---")
            for student in students:
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])
                print("--------------------")

    elif choice == 3:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")