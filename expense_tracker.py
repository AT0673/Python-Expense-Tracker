def main():
    print("Welcome to the Expense Tracker!")
    pass

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

def write_expense_to_file():
    print("Writing expense to file...")

# This function will read expenses from a file and summarize them
def summarize_expenses():
    print("Summarizing expenses...")


if __name__ == "__main__":
    main()