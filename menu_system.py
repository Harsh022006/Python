def show_menu():
    print("\n------ Welcome to Harsh's Food Corner ------")
    print("1. Pizza - ₹120")
    print("2. Burger - ₹80")
    print("3. Sandwich - ₹60")
    print("4. Coffee - ₹50")
    print("5. Exit")

def take_order():
    total = 0
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            print("You selected Pizza 🍕")
            qty = int(input("Enter quantity: "))
            total += 120 * qty
        elif choice == '2':
            print("You selected Burger 🍔")
            qty = int(input("Enter quantity: "))
            total += 80 * qty
        elif choice == '3':
            print("You selected Sandwich 🥪")
            qty = int(input("Enter quantity: "))
            total += 60 * qty
        elif choice == '4':
            print("You selected Coffee ☕")
            qty = int(input("Enter quantity: "))
            total += 50 * qty
        elif choice == '5':
            print("\nExiting the menu...")
            break
        else:
            print("Invalid choice! Please select again.")
            continue

        another = input("Do you want to order more? (yes/no): ").lower()
        if another != 'yes':
            break

    return total

def main():
    total_bill = take_order()
    print("\n------ BILL SUMMARY ------")
    print(f"Total Amount to Pay: ₹{total_bill}")
    print("Thank you for visiting Harsh's Food Corner! 😊")

# Run the program
main()
