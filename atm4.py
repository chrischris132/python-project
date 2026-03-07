import time
import os

# === FILE SETUP ===
filename = "atm_data.txt"

# Load data if file exists
if os.path.exists(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        pin_code = lines[0].strip()
        balance = float(lines[1].strip())
        transactions = [line.strip() for line in lines[2:]]
else:
    # Default values if file not found
    pin_code = "1234"
    balance = 0.0
    transactions = []

attempts = 3
withdrawal_limit = 3
withdrawals_done = 0

# === LOGIN SYSTEM ===
while attempts > 0:
    entered_pin = input("Enter your 4-digit PIN: ")
    if entered_pin == pin_code:
        print("PIN accepted. Welcome!")
        time.sleep(1)
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. {attempts} attempt(s) left.")
        time.sleep(1)

if attempts == 0:
    print("Too many wrong attempts. Account locked.")
else:
    # === ATM MENU ===
    while True:
        print("\n=== ATM MENU ===")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Change PIN")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            transactions.append(f"Deposited ${amount}")
            print(f"${amount} deposited successfully")
            time.sleep(1)

        elif choice == "2":
            if withdrawals_done >= withdrawal_limit:
                print("Withdrawal limit reached for this session.")
                time.sleep(1)
                continue
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient funds!")
            else:
                balance -= amount
                withdrawals_done += 1
                transactions.append(f"Withdrew ${amount}")
                print(f"${amount} withdrawn successfully")
            time.sleep(1)

        elif choice == "3":
            print(f"Your current balance is: ${balance}")
            time.sleep(1)

        elif choice == "4":
            print("\n=== TRANSACTION HISTORY ===")
            if len(transactions) == 0:
                print("No transactions yet.")
            else:
                for t in transactions:
                    print("-", t)
            time.sleep(2)

        elif choice == "5":
            old_pin = input("Enter your current PIN: ")
            if old_pin == pin_code:
                new_pin = input("Enter your new 4-digit PIN: ")
                confirm_pin = input("Confirm your new PIN: ")
                if new_pin == confirm_pin and len(new_pin) == 4 and new_pin.isdigit():
                    pin_code = new_pin
                    print("PIN changed successfully!")
                else:
                    print("PINs did not match or invalid format.")
            else:
                print("Incorrect current PIN.")
            time.sleep(1)

        elif choice == "6":
            # === SAVE DATA BEFORE EXIT ===
            with open(filename, "w") as file:
                file.write(pin_code + "\n")
                file.write(str(balance) + "\n")
                for t in transactions:
                    file.write(t + "\n")

            print("Data saved successfully.")
            print("Thank you for using our ATM. Goodbye!")
            time.sleep(1)
            break

        else:
            print("Invalid choice! Please select 1–6.")
            time.sleep(1)
