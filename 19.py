#Grocery Store Menu
cart = {}

while True:
    print("\n--- Grocery Store ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Total Price")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item name: ")
        price = float(input("Enter item price: "))

        cart[item] = price
        print(item, "added to cart.")

    elif choice == 2:
        item = input("Enter item to remove: ")

        if item in cart:
            del cart[item]
            print(item, "removed from cart.")
        else:
            print("Item not found!")

    elif choice == 3:
        total = sum(cart.values())
        print("Total price:", total)

    elif choice == 4:
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice!")