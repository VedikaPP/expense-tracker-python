# Expense Tracker Project

expenses = [] #list  of expenses in form of dictionary
print("Welcome  to Expense Tracker !!!")

while True:
    print("=======Menu======")
    print("1. Add Expense ")
    print("2. View All Expenses ")
    print("3. View Total ")
    print("4. Exit ")

    choice = int(input("Please Enter Your Choice : "))
# Add Expense
    if (choice == 1):
        date = input("Enter the date (DD-MM-YY) : ")
        category = input("Enter category(Food,Travel,shopping ,etc) : ")
        description = input ("Enter short Description : ")
        amount =float( input ("Enter the total amount :"))

        expense = {
            "date" : date,
            "category": category,
            "description":description,
            "amount": amount
        }        

        expenses.append(expense)
        print("\n Expenses added succsefully")

#2. Veiw all expenses
    elif(choice == 2):
        if(len(expenses)==0):
            print("No Expense Added")
        else:
            print("====This is your all expense ====")
            count =1
        for eachexpense in expenses:
                print(f"Expense Number {count} -> {eachexpense['date']}, {eachexpense['category']}, {eachexpense['description']}, {eachexpense['amount']}")
                count = count+1
#3. View total Spending
    elif(choice == 3):
        total=0
        for eachexpense in expenses:
            total = total + eachexpense["amount"]

        print("\n Total Expense = ", total)
#4.Exit
    elif(choice== 4):
        print("Thank You for using our system 😊")
        break

    else:
        print("Invalid choice Try again")