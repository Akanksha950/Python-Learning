# Expense Tracker Project

expenseList=[]  # list to store multiple expenses

print("Welcome to Expense Tracker!")

while True:
    print("\n ====== MENU ======")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. Exit")
    print("===================")

    choice=int(input("\n Enter your choice(1-4):"))

    #1. ADD EXPENSE
    if(choice == 1):
        date=input("\n Enter date (DD-MM-YYYY): ")
        category=input("Enter category(Food, Travel, Shopping,etc): ")
        description=input("Enter short description: ")
        amount=float(input("Enter amount: "))

        expense={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }

        expenseList.append(expense)
        print("\n Expense added successfully")

    # 2.VIEW ALL EXPENSE

    elif(choice == 2):
        if(len(expenseList)==0):
            print("\n No expense recorded yet")
        else:
            print("\n All Expenses")
            count=1
            for e in expenseList:
                print(f"Expense {count} -> {e["date"]}, {e["category"]},{e["description"]},{e["amount"]}")
                count=count+1

            

    # 3. VIEW TOTAL SPENDING

    elif(choice == 3):
        total=0
        for e in expenseList:
            total=total+e["amount"]

        print("\n Total Spending = ", total)

    # 4. EXIT
    elif(choice == 4):
        print("\n Thanks for using Expense Tracker")
        break
    else:
        print("\n Invalid choice. Try Again")




