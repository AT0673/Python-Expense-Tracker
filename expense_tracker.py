def main():
    print("Welcome to the Expense Tracker!")
    expense_file_path = "expenses.csv"

    #Get user input for expenses
    get_expense_details()

    #Write expenses to a file
    write_expense_to_file()

    #Read expenses from a file and summarize them
    summarize_expenses()

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



def write_expense_to_file(expense, expense_file_path):
    print(f"Saving user expense: {expense}")


# This function will read expenses from a file and summarize them
def summarize_expenses():
    print("Summarizing expenses...")


if __name__ == "__main__":
    main()