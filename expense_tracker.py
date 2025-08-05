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
    print("You've entered: {expense_name}, {expense_amount}")
    
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
        "category": selected_category
    }   

    print("Expense recorded:")
    print(f"  Name    : {expense['name']}")
    print(f"  Amount  : ${expense['amount']:.2f}")
    print(f"  Category: {expense['category']}")
    return expense


def write_expense_to_file(expense, expense_file_path):
    print(f"Saving user expense: {expense} to {expense_file_path}")
    with open(expense_file_path, 'a') as file:
        file.write(f"{expense['name']},{expense['amount']},{expense['category']}\n")


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
        name, amount, category = expense.strip().split(',')
        emoji = category_emojis.get(category, "📝")
        print(f"{emoji} {category} - {name}: ${float(amount):.2f}")

    amount_by_category = {}
    for expense in expenses:
        _, amount, category = expense.strip().split(',')
        amount = float(amount)
        if category in amount_by_category:
            amount_by_category[category] += amount
        else:
            amount_by_category[category] = amount
    
    print("\n=== 📊 Category Totals 📊 ===")
    for category, total in amount_by_category.items():
        emoji = category_emojis.get(category, "📝")
        print(f"{emoji} {category}: ${total:.2f}")
    
    grand_total = sum(amount_by_category.values())
    print("\n=== 💵 Grand Total 💵 ===")
    print(f"Total Expenses: ${grand_total:.2f}")
    print("\n" + "=" * 30 + "\n")


if __name__ == "__main__":
    main()
