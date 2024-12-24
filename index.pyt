
categories = {
    "Food": 0,
    "Transport": 0,
    "Entertainment": 0,
    "Utilities": 0,
    "Others": 0
}

def add_expense():
    print("\nAvailable categories:")
    for category in categories:
        print(f"- {category}")

    
    category = input("\nEnter the category for your expense: ").capitalize()

    if category in categories:
        
        try:
            amount = float(input(f"Enter the amount for {category}: "))
            categories[category] += amount
            print(f"\n{amount} added to {category}!")
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
    else:
        print("Invalid category. Please try again.")

def show_summary():
    total_expenses = sum(categories.values())
    
   
    print("\n=== Daily Expense Summary ===")
    print(f"Total Expenses: ₹{total_expenses:.2f}")
    
    if total_expenses == 0:
        print("No expenses recorded yet.")
        return
    
    
    for category, amount in categories.items():
        percentage = (amount / total_expenses) * 100
        print(f"{category}: ₹{amount:.2f} ({percentage:.2f}%)")

def main():
    print("Welcome to the Daily Expense Tracker!")
    
    while True:
        print("\nOptions:")
        print("1. Add an expense")
        print("2. Show expense summary")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            show_summary()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
