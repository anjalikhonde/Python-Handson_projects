menu = {
    "Pizza": 40,
    "Pasta": 50,
    "Burger": 60,
    "Salad": 70,
    "Coffee": 80
}

print("=" * 60)
print("🍽️ Welcome to XYZ Restaurant")
print("=" * 60)

print("Menu")
print("-" * 60)

for item, price in menu.items():
    print(f"{item:<10} : Rs {price}")

print("=" * 60)

order_total = 0

# First Order
item = input("Enter the first item you want to order: ").title()

if item in menu:
    order_total += menu[item]
    print(f"✅ {item} has been added to your order.")
else:
    print(f"❌ Sorry! {item} is not available.")

# Additional Orders
while True:
    choice = input("\nDo you want to order anything else? (Y/N): ").lower()

    if choice == "y":
        item = input("Enter the next item: ").title()

        if item in menu:
            order_total += menu[item]
            print(f"✅ {item} has been added to your order.")
        else:
            print(f"❌ Sorry! {item} is not available.")

    elif choice == "n":
        break

    else:
        print("⚠️ Please enter only Y or N.")

# Final Bill
print("\n" + "=" * 60)
print("🧾 Final Bill")
print("=" * 60)
print(f"Total Amount: Rs {order_total}")
print("🙏 Thank you for visiting XYZ Restaurant!")
print("Have a great day!")