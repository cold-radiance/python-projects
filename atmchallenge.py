total = 100
while total > 0:
    a = int(input("Enter the amount to withdraw (or 0 to exit): "))
    if a == 0:
        print("Exiting. Thank you!")
        break
    elif a <= total:
        total = total - a
        print("Amount withdrawn :", a)
        print("Remaining balance :", total)
    else:
        print("Insufficient balance. Please enter a smaller amount.")

if total == 0:
    print("You are broke")        