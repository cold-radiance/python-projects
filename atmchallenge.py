balance = 1000
is_running = True

print("=== WELCOME TO THE COLD-RADIANCE ATM ===")

# This loop will keep running forever until is_running becomes False
while is_running:
    print("\n1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        print(f"Your current balance is: ${balance}")
        
    elif choice == "2":
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance:
            print("❌ Insufficient funds! You can't withdraw that much.")
        else:
            balance -= amount
            print(f"✅ Successfully withdrew ${amount}. New balance: ${balance}")
            
    elif choice == "3":
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print(f"✅ Successfully deposited ${amount}. New balance: ${balance}")
        
    elif choice == "4":
        print("Thank you for using Cold-Radiance ATM. Goodbye! 👋")
        is_running = False  # This breaks the loop and stops the program
        
    else:
        print("❌ Invalid option. Please choose between 1 and 4.")