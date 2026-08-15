#menu driven program
def menu():
    print("Welcome to the menu-driven program!")
    print("1. option1")
    print("2.option2")
    print("3.option3")
    print("4.Exit")

while True:
    menu()
    choice=input("Enter your choice (1-4):")

    if choice=="1":
        print("you selected option 1")
    elif choice=="2":
        print("you selected option 2")
    elif choice=="3":
            print("you selected option 3")
    elif choice=="4":
            print("exiting the program.goodbye!")
            break
    else:
        print("Invalid choice.please try again")   


#simple calculator

def menu():
    print("\nSimple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
while True:
    menu()
    choice = input("Enter your choice (1-5): ")

    if choice in ['1', '2', '3', '4']:
        # Get two numbers from the user
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

    if choice == '1':
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
    elif choice == '5':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")