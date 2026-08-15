#home-work Banking System

balance = 1000

while True:
    print("\n--- Banking System ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Money deposited successfully!")
        print("New balance:", balance)

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance -= amount
            print("Money withdrawn successfully!")
            print("New balance:", balance)
        else:
            print("Insufficient balance!")

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
