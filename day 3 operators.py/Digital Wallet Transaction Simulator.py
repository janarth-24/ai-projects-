"""
Question 3 — Digital Wallet Transaction Simulator
Problem statement
Create a Python program that simulates a digital wallet using assignment and comparison operators.
Requirements
Accept the user's name and initial wallet balance.
Accept a deposit amount.
Update the balance using +=.
Accept a withdrawal amount.
Check whether sufficient balance is available.
Update the balance using -= if the withdrawal is valid.
Reject negative amounts.
Display the final balance using f-strings.
"""
name = input("Enter your name: ")
#initialize the wallet balance
while True:
    try:
        initial_balance = float(input("Enter your initial wallet balance: "))
        if initial_balance < 0:
            print("Initial balance cannot be negative. Please try again.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

wallet_balance = initial_balance
while True:
    choice = int(input("Enter a number to choose an option:\n1. Deposit\n2. Withdraw\n3. Check balance\n4. Exit\n"))

    if choice == 1:
            #Accept a deposit amount
        while True:
            try:
                deposit_amount = float(input("Enter the deposit amount: "))
                if deposit_amount < 0:
                    print("Deposit amount cannot be negative. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        # Update the balance using +=
        wallet_balance += deposit_amount

    
    elif choice == 2:
        #Accept a withdrawal amount
        while True:
            try:
                withdrawal_amount = float(input("Enter the withdrawal amount: "))
                if withdrawal_amount < 0:
                    print("Withdrawal amount cannot be negative. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        # Check whether sufficient balance is available
        if withdrawal_amount > wallet_balance:
            print("Insufficient balance for this withdrawal.")
        else:
            # Update the balance using -= if the withdrawal is valid
            wallet_balance -= withdrawal_amount

    elif choice == 3:
        # Display the current balance
        print(f"{name}, your current wallet balance is: ${wallet_balance:.2f}")
    else:
        print("Exiting the program.")
        break


    # Display the final balance using f-strings
    print(f"{name}, your final wallet balance is: ${wallet_balance:.2f}")
