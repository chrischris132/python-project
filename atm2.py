
balance = 0 # starting balance
while True:
    print("\n== ATM MENU ===")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("choose an option(1-4): ")
    if choice == "1":
        amount = float(input("enter amount to deposit: "))
        balance= balance+amount
        print(f"${amount} deposited successfully. new balance is${balance}")
        
    if choice == "2":
        amount1 = float(input("Enter amount to withdraw: "))         
        if amount > balance:
            print("insufficient funds")
        else:
            balance=balance-amount
            print(f"${amount1} Withdrawn successfully.")     
    if choice == "3":
        print(f"Your current balance is:${balance}")
    if choice == "4":
        print("Thank you for using our ATM. Goodbye")
        break
    else:
        print("invalid choice please select 1-4.")
   
