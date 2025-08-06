from expense import Expense


def main():
    print("Welcome to the Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget_file_path = "budget.csv"

    #Get user input for expenses and budget
    while True:
        print("Please select an option:")
        print("1. Set Budget")
        print("2. Add Expense")
        print("4. View Expense Summary")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            budget = get_budget()
        elif choice == "2":
            expense = get_expense_details()
            #Write expenses to a file
            write_expense_to_file(expense, expense_file_path)
            summarize_expenses(expense_file_path, budget_file_path)
        elif choice == "4":
            summarize_expenses(expense_file_path, budget_file_path)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


def get_budget():
    # Get user input for budget and month/year of budget and save it
    print("\n=== 💰 Set Your Budget 💰 ===")
    budget_file_path = "budget.csv"
    budget_amount = float(input("Enter your budget amount: "))
    budget_month = input("Enter the month for the budget (YYYY-MM): ")
    # Validate month format
    try:
        from datetime import datetime
        datetime.strptime(budget_month, '%Y-%m')
    except ValueError:
        print("Invalid month format. Please use YYYY-MM.")
        return None
    # write the budget to a file
    with open(budget_file_path, 'a') as budget_file:
        budget_file.write(f"{budget_amount},{budget_month}\n")
    print(f"Budget of ${budget_amount:.2f} set for {budget_month}.")
    return budget_amount

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
def summarize_expenses(expense_file_path, budget_file_path):
    print("\n=== 💰 Expense Summary 💰 ===\n")
    with open(expense_file_path, 'r') as file:
        expenses = file.readlines()
    
    # Ensure monthly_totals is always defined
    monthly_totals = {}

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
    budget_dict = {}
    try:
        with open(budget_file_path, 'r') as budget_file:
            for line in budget_file:
                if line.strip():
                    budget_amount, budget_month = line.strip().split(',')
                    budget_dict[budget_month] = float(budget_amount)
    except FileNotFoundError:
        pass  # No budgets set yet

    monthly_totals = {}
    for expense in expenses:
        try:
            _, amount, _, date = expense.strip().split(',')
            amount = float(amount)
            month = date[:7]  # YYYY-MM
            if month in monthly_totals:
                monthly_totals[month] += amount
            else:
                monthly_totals[month] = amount
        except ValueError:
            continue

    while True:
        print("\n=== 📊 Summary Options 📊 ===")
        print("1. View daily totals")
        print("2. View monthly totals")
        print("3. View yearly totals")
        print("4. View category totals")
        print("5. View all expenses")
        print("6. View monthly budget comparison")
        print("7. Visualize expenses")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")
        if choice == '8':
            print("Exiting the Expense Tracker. Goodbye!")
            break
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

            # Calculate all years and months present in the expenses
            years = set()
            months_by_year = {}
            for expense in expenses:
                try:
                    _, _, _, date = expense.strip().split(',')
                    dt = datetime.strptime(date, '%Y-%m-%d')
                    year = dt.strftime('%Y')
                    month = dt.strftime('%m')
                    years.add(year)
                    months_by_year.setdefault(year, set()).add(month)
                except ValueError:
                    print(f"Skipping invalid date in expense: {expense.strip()}")
                    continue

            years = sorted(years)
            print("Available years:", ", ".join(years))
            year_choice = input("Enter a year to view daily totals (or press Enter for all years): ").strip()
            if year_choice != 'all' and year_choice not in years:
                print("Invalid year selected.")
                return
            
            # Default to 'all' months unless specified
            month_choice = 'all'
            # If not 'all', show available months for the selected year
            if year_choice != 'all':
                months = sorted(months_by_year.get(year_choice, []))
                print("Available months:", ", ".join(months))
                month_input = input("Enter a month to view daily totals (or type 'all' for all months): ").strip()
                if month_input and month_input != 'all':
                    if month_input not in months:
                        print("Invalid month selected.")
                        return
                    else:
                        month_choice = month_input

            # Calculate daily totals based on the user's choices
            daily_totals = {}
            for expense in expenses:
                try:
                    _, amount, category, date = expense.strip().split(',')
                    amount = float(amount)
                    dt = datetime.strptime(date, '%Y-%m-%d')
                    year = dt.strftime('%Y')
                    month = dt.strftime('%m')
                    day = dt.strftime('%d')
                    if (year_choice == 'all' or year == year_choice) and (month_choice == 'all' or month == month_choice):
                        if day in daily_totals:
                            daily_totals[day] += amount
                        else:
                            daily_totals[day] = amount
                except ValueError:
                    print(f"Skipping invalid date in expense: {expense.strip()}")
                    continue
            if not daily_totals:
                print("No expenses found for the selected period.")
                return
            else:
                print(f"Daily totals for {year_choice} {month_choice if month_choice != 'all' else ''}:")
                for day, total in sorted(daily_totals.items()):
                    print(f"{day}: ${total:.2f}")
            pass
        elif choice == '2':
            print("\n=== 📅 Monthly Totals 📅 ===")
            for month, total in sorted(monthly_totals.items()):
                print(f"{month}: ${total:.2f}")
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
            pass
        elif choice == '4':
            print("\n=== 📊 Category Totals 📊 ===")
            if not amount_by_category:
                print("No expenses recorded.")
                return
            for category, total in amount_by_category.items():
                emoji = category_emojis.get(category, "📝")
                print(f"{emoji} {category}: ${total:.2f}")
            pass

            # Budget comparison via the budget file after the user picks a month to compare
        elif choice == '6':
            print("\n=== 📊 Budget Comparison 📊 ===")
            month_to_compare = input("Enter the month to compare (YYYY-MM): ")
        # Validate month format
            try:
                from datetime import datetime
                datetime.strptime(month_to_compare, '%Y-%m')
            except ValueError:
                print("Invalid month format. Please use YYYY-MM.")
                continue
            if month_to_compare not in budget_dict:
                print(f"No budget set for {month_to_compare}.")
                continue
            if month_to_compare not in monthly_totals:
                print("No expenses recorded to compare against the budget.")
                continue
            budget_amount = budget_dict[month_to_compare]
            total = monthly_totals[month_to_compare]
            if total > budget_amount:
                print(f"{month_to_compare}: Over budget by ${total - budget_amount:.2f}")
            else:
                print(f"{month_to_compare}: Under budget by ${budget_amount - total:.2f}")
        elif choice == '7':
            print("\n=== 📊 Visualize Expenses 📊 ===")
            import plotly.graph_objects as go
            from plotly.subplots import make_subplots

            # Create a subplot with 2 rows and 2 columns
            fig = make_subplots(
                rows=2, cols=2,
                subplot_titles=("Monthly Expenses", "Category Distribution", 
                                "Daily Expenses", "Cumulative Expense Trend"),
                specs=[[{"type": "xy"}, {"type": "pie"}], # First row: Monthly Expenses and Category Distribution
                       [{"type": "xy"}, {"type": "xy"}]]  # Second row: Daily Expenses and Cumulative Expense Trend
            )
            
            # Monthly Expenses
            months = list(monthly_totals.keys())
            monthly_expenses = list(monthly_totals.values())
            fig.add_trace(
                go.Bar(x=months, y=monthly_expenses, name="Monthly Expenses"),
                row=1, col=1
            )

            # Category Distribution Pie Chart
            categories = list(amount_by_category.keys())
            category_totals = list(amount_by_category.values())
            fig.add_trace(
                go.Pie(labels=categories, values=category_totals, name="Category Distribution"),
                row=1, col=2
            )

            # Daily Expenses
            # Sort dates for better visualization
            expense_data = [(date, float(amount)) for _, amount, _, date in 
                           (expense.strip().split(',') for expense in expenses)]
            expense_data.sort(key=lambda x: x[0])  # Sort by date
            dates, daily_expenses = zip(*expense_data)

            fig.add_trace(
                go.Scatter(x=dates, y=daily_expenses, mode='lines+markers', name="Daily Expenses"),
                row=2, col=1
            )

            # Cumulative Expense Trend
            cumulative_expenses = []
            cumulative_total = 0
            for amount in daily_expenses:
                cumulative_total += amount
                cumulative_expenses.append(cumulative_total)
            fig.add_trace(
                go.Scatter(x=dates, y=cumulative_expenses, mode='lines', name="Cumulative Expenses"),
                row=2, col=2
            )

            # Update layout
            fig.update_layout(
                title_text="Expense Tracker Visualization",
                height=800,
                width=1200,
                showlegend=True
            )

            # Show the figure
            fig.show()

if __name__ == "__main__":
    main()
