"""
Day 3 — Mini Project
Smart Shopping Bill and Discount Calculator
Problem statement
Build a Python program that generates a shopping bill by calculating the total purchase amount, applying discounts, calculating tax, and determining the final payable amount.
Input requirements
Collect the customer's name, product name, unit price, quantity, and membership status (True or False).
Business rules
Purchase amount     -> Discount
₹5,000 and above    -> 20%
₹2,000–4,999.99    -> 10%
₹1,000–1,999.99    -> 5%
Below ₹1,000        -> 0%


Additional rules:
Members receive an additional five percentage points of discount.
Apply an illustrative tax of 18% after deducting the total discount.
Reject negative prices and quantities less than or equal to zero.
Validate the customer's name and membership status.
Display all monetary values to two decimal places.

"""


import math

# Collect and validate customer name
while True:
    name = input("Enter your name: ").strip()

    if name.replace(" ", "").isalpha():
        break

    print("Invalid name. Please try again.")

# Validate mobile number
while True:
    mobile_number = input("Enter your mobile number: ").strip()

    if len(mobile_number) == 10 and mobile_number.isdigit():
        break

    print("Please enter a valid 10-digit mobile number.")

# Validate membership status
while True:
    membership = input("Are you a member? (True/False): ").strip().lower()

    if membership in ["true", "false"]:
        membership_status = membership == "true"
        break

    print("Invalid input. Enter True or False.")

# Initialize shopping cart outside the loop
products = {}

# Main menu
while True:
    print("\n========== SHOPPING MENU ==========")
    print("1. Add Product")
    print("2. View Cart")
    print("3. Remove Product")
    print("4. Calculate Bill")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add product
    if choice == "1":

        product_name = input("Enter product name: ").strip().title()

        if not product_name:
            print("Product name cannot be empty.")
            continue

        try:
            unit_price = float(input("Enter unit price: "))
            quantity = int(input("Enter quantity: "))

            # Validate price and quantity
            if not math.isfinite(unit_price) or unit_price < 0:
                print("Invalid unit price.")
                continue

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue

        except ValueError:
            print("Invalid input. Enter valid numeric values.")
            continue

        # Handle duplicate products
        if product_name in products:
            old_price, old_quantity = products[product_name]

            if old_price != unit_price:
                print("This product already exists with a different price.")
                continue

            quantity += old_quantity

        # Store product details
        products[product_name] = (unit_price, quantity)

        print(f"{product_name} added successfully!")

    # View shopping cart
    elif choice == "2":

        if not products:
            print("Your shopping cart is empty.")
            continue

        print("\n=============== SHOPPING CART ===============")

        print(f"{'Product':<20}{'Price':>10}{'Qty':>6}{'Total':>12}")

        for product_name, (unit_price, quantity) in products.items():
            price = unit_price * quantity

            print(f"{product_name:<20}{unit_price:>10.2f}"
                  f"{quantity:>6}{price:>12.2f}")

        subtotal = sum(
            price * qty for price, qty in products.values()
        )

        print("----------------------------------------------")
        print(f"Cart Total: ₹{subtotal:.2f}")

    # Remove product
    elif choice == "3":

        if not products:
            print("Your shopping cart is empty.")
            continue

        product_name = input("Enter product to remove: ").strip().title()

        if product_name in products:
            del products[product_name]
            print(f"{product_name} removed successfully.")
        else:
            print("Product not found in the cart.")

    # Calculate final bill
    elif choice == "4":

        if not products:
            print("Add at least one product before billing.")
            continue

        # Calculate total purchase amount
        total_purchase_amount = sum(
            unit_price * quantity
            for unit_price, quantity in products.values()
        )

        # Calculate purchase discount
        if total_purchase_amount >= 5000:
            purchase_discount = 0.20
        elif total_purchase_amount >= 2000:
            purchase_discount = 0.10
        elif total_purchase_amount >= 1000:
            purchase_discount = 0.05
        else:
            purchase_discount = 0.00

        # Calculate membership discount
        membership_discount = 0.05 if membership_status else 0.00

        # Calculate total discount
        total_discount = purchase_discount + membership_discount

        discount_amount = total_purchase_amount * total_discount

        # Amount after discount
        discounted_amount = total_purchase_amount - discount_amount

        # Calculate tax
        tax_rate = 0.18
        tax_amount = discounted_amount * tax_rate

        # Calculate final payable amount
        final_purchase_amount = discounted_amount + tax_amount

        # Display customer details
        print("\n================ SMART SHOPPING BILL ================")

        print(f"Customer Name     : {name}")
        print(f"Mobile Number     : {mobile_number}")
        print(f"Membership Status : {'Member' if membership_status else 'Non-Member'}")

        # Display product details
        print("\n---------------- PRODUCT DETAILS -------------------")

        print(f"{'Product':<20}{'Price':>10}{'Qty':>6}{'Total':>12}")

        for product_name, (unit_price, quantity) in products.items():
            price = unit_price * quantity

            print(f"{product_name:<20}{unit_price:>10.2f}"
                  f"{quantity:>6}{price:>12.2f}")

        # Display bill summary
        print("\n---------------- BILL SUMMARY ----------------------")

        print(f"Total Purchase Amount : ₹{total_purchase_amount:.2f}")
        print(f"Purchase Discount     : {purchase_discount * 100:.0f}%")
        print(f"Membership Discount   : {membership_discount * 100:.0f}%")
        print(f"Total Discount        : {total_discount * 100:.0f}%")
        print(f"Discount Amount       : ₹{discount_amount:.2f}")
        print(f"Discounted Amount     : ₹{discounted_amount:.2f}")
        print(f"Tax Rate              : {tax_rate * 100:.0f}%")
        print(f"Tax Amount            : ₹{tax_amount:.2f}")

        print("----------------------------------------------------")
        print(f"Final Payable Amount  : ₹{final_purchase_amount:.2f}")
        print("----------------------------------------------------")

        print(f"You saved ₹{discount_amount:.2f} through discounts!")
        print("Thank you for shopping with us!")

        break

    # Exit application
    elif choice == "5":
        print("Thank you for visiting!")
        break

    # Handle invalid menu choices
    else:
        print("Invalid choice. Please select between 1 and 5.")
