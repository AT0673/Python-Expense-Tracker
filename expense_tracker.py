from expense import Expense


def main():
    print("Welcome to the Expense Tracker!")
    expense_file_path = "expenses.csv"

    #Get user input for expenses
    expense = get_expense_details()

    #Write expenses to a file
    write_expense_to_file(expense, expense_file_path)

    #Read expenses from a file and summarize them
    summarize_expenses(expense_file_path)

def get_expense_details():
    print("Getting expense details...")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_date = input("Enter expense date (YYYY-MM-DD): ")
    # Validate date format
    try:
        from datetime import datetime
        datetime.strptime(expense_date, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None
    # Print the entered details
    print(f"You've entered: {expense_name}, {expense_amount}, {expense_date}")

    expense_categories = [
        "Food",
        "Transport",
        "Utilities",
        "Entertainment",
        "Other",
    ]
    
    while True:
        print("Select a category for the expense:")
        for i, category_name in enumerate(expense_categories):
            print(f" {i+1}. {category_name}")
        try:
            category_choice = int(input("Enter the number of the category: "))
            if 1 <= category_choice <= len(expense_categories):
                selected_category = expense_categories[category_choice - 1]
                print(f"You selected: {selected_category}")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

   # Creating an Expense object and saving it
    expense = {
        "name": expense_name,
        "amount": expense_amount,
        "category": selected_category,
        "date": expense_date
    }   

    print("Expense recorded:")
    print(f"  Name    : {expense['name']}")
    print(f"  Amount  : ${expense['amount']:.2f}")
    print(f"  Category: {expense['category']}")
    print(f"  Date    : {expense['date']}")
    return expense


def write_expense_to_file(expense, expense_file_path):
    print(f"Saving user expense: {expense} to {expense_file_path}")
    with open(expense_file_path, 'a') as file:
        file.write(f"{expense['name']},{expense['amount']},{expense['category']},{expense['date']}\n")


# This function will read expenses from a file and summarize them
def summarize_expenses(expense_file_path):
    print("\n=== 💰 Expense Summary 💰 ===\n")
    with open(expense_file_path, 'r') as file:
        expenses = file.readlines()
    
    # Dictionary for category emojis
    category_emojis = {
        "Food": "🍔",
        "Transport": "🚗",
        "Utilities": "🏠",
        "Entertainment": "🎮",
        "Other": "📦"
    }

    
    
    for expense in expenses:
        name, amount, category, date = expense.strip().split(',')
        emoji = category_emojis.get(category, "📝")
        print(f"{emoji} {category} - {name}: ${float(amount):.2f} on {date}")

    amount_by_category = {}
    for expense in expenses:
        _, amount, category, _ = expense.strip().split(',')
        amount = float(amount)
        if category in amount_by_category:
            amount_by_category[category] += amount
        else:
            amount_by_category[category] = amount


    # User input for summary options
    print("\n=== 📊 Summary Options 📊 ===")
    print("1. View daily totals")
    print("2. View monthly totals")
    print("3. View yearly totals")
    print("4. View category totals")
    print("5. View all expenses")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    if choice == '6':
        print("Exiting the Expense Tracker. Goodbye!")
        return
    elif choice == '5':
        print("\n=== 📋 All Expenses 📋 ===")
        for expense in expenses:
            name, amount, category, date = expense.strip().split(',')
            emoji = category_emojis.get(category, "📝")
            print(f"{emoji} {category} - {name}: ${float(amount):.2f} on {date}")
        return
    elif choice == '1':
        # Daily totals
        print("\n=== 📅 Daily Totals 📅 ===")
        from datetime import datetime
        daily_totals = {}
        for expense in expenses:
            _, amount, category, date = expense.strip().split(',')
            amount = float(amount)
            day = datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m-%d')
            if day in daily_totals:
                daily_totals[day] += amount
            else:
                daily_totals[day] = amount
        for day, total in daily_totals.items():
            print(f"{day}: ${total:.2f}")
        return
    elif choice == '2':
        print("\n=== 📅 Monthly Totals 📅 ===")
        from datetime import datetime
        monthly_totals = {}
        for expense in expenses:
            _, amount, category, date = expense.strip().split(',')
            amount = float(amount)
            month = datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m')
            if month in monthly_totals:
                monthly_totals[month] += amount
            else:
                monthly_totals[month] = amount
        for month, total in monthly_totals.items():
            print(f"{month}: ${total:.2f}")
        return
    elif choice == '3':
        print("\n=== 📆 Yearly Totals 📆 ===")
        from datetime import datetime
        yearly_totals = {}
        for expense in expenses:
            _, amount, category, date = expense.strip().split(',')
            amount = float(amount)
            year = datetime.strptime(date, '%Y-%m-%d').strftime('%Y')
            if year in yearly_totals:
                yearly_totals[year] += amount
            else:
                yearly_totals[year] = amount
        for year, total in yearly_totals.items():
            print(f"{year}: ${total:.2f}")
        return
    elif choice == '4':
        print("\n=== 📊 Category Totals 📊 ===")
        if not amount_by_category:
            print("No expenses recorded.")
            return
        for category, total in amount_by_category.items():
            emoji = category_emojis.get(category, "📝")
            print(f"{emoji} {category}: ${total:.2f}")
    elif choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please try again.")
        return
    print("\nThank you for using the Expense Tracker! Have a great day! 😊")

if __name__ == "__main__":
    main()
