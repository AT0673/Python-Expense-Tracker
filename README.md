# Python Expense Tracker 💰

A simple yet effective command-line expense tracking application built in Python. Track your daily expenses, categorize them, and get detailed summaries of your spending habits.

## Why I Built This 🎓

As a university student living away from home for the first time, I quickly realized that managing my finances was more challenging than I expected. Between groceries, transport, utilities, and the occasional entertainment, my money seemed to disappear faster than I could track it. I needed a simple, no-frills solution that could help me understand where my money was going without the complexity of expensive budgeting apps.

This expense tracker was born out of necessity during my studies. I wanted something I could quickly use between classes, that would store my data locally, and give me clear insights into my spending patterns. The categorization feature helped me identify that I was spending way too much on takeout (classic student mistake!), and the summary reports became essential for my monthly budget reviews.

Built using the Python skills I was learning in my computer science courses, this project serves both as a practical tool for daily use and a demonstration of clean, functional programming principles.

## Requirements & Architecture 📋

### Core Requirements
This application was designed to meet specific needs for effective personal finance management:

- **User-Friendly Expense Entry**: Allow users to quickly input expenses with minimal friction
- **Persistent Data Storage**: Save all expenses to a CSV file for long-term tracking and data portability
- **Comprehensive Expense Summarization**: Provide clear breakdowns of spending by category and total amounts
- **Budget Awareness**: Show spending patterns to help users make informed financial decisions
- **Offline Functionality**: Work completely offline without requiring internet connectivity or external services

## Features ✨
The application follows a clean, modular design using two main components:

1. **`expense.py`** - Data Model
   - Contains the `Expense` class that encapsulates three essential attributes:
     - `name`: Description of the expense
     - `category`: Spending category for organization
     - `amount`: Monetary value of the expense

2. **`expense_tracker.py`** - Application Logic
   - Handles the complete expense tracking workflow:
     - Interactive user input collection
     - Data validation and processing
     - CSV file writing and reading operations
     - Summary generation and display formatting

This simple yet effective architecture ensures the application is easy to understand, maintain, and extend while providing all necessary functionality for expense tracking.

- **Interactive Expense Entry**: Easy-to-use command-line interface for adding expenses
- **Category Organization**: Organize expenses into predefined categories:
  - 🍔 Food
  - 🚗 Transport
  - 🏠 Utilities
  - 🎮 Entertainment
  - 📦 Other
- **Persistent Storage**: Expenses are saved to a CSV file for long-term tracking
- **Visual Summaries**: Get colorful, emoji-enhanced summaries of your expenses
- **Category Totals**: See spending breakdown by category
- **Grand Total**: Track your overall spending

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/Python-Expense-Tracker.git
cd Python-Expense-Tracker
```

2. Ensure you have Python 3.6+ installed:
```bash
python --version
```

3. Install required dependencies:
```bash
pip install pandas plotly
```

Note: The application uses pandas for data export functionality and plotly for interactive visualizations.

## Usage

Run the expense tracker:

```bash
python expense_tracker.py
```

### Main Menu Options

The application now features an interactive menu system:

1. **Set Budget** - Define monthly budgets for spending targets
2. **Add Expense** - Record new expenses with date and category
3. **View Expense Summary** - Access detailed spending analysis
4. **Export Expenses to Different Format** - Export data to CSV, JSON, or XML
5. **Exit** - Close the application

### Setting a Budget

1. Select option 1 from the main menu
2. Enter your budget amount
3. Specify the month in YYYY-MM format (e.g., 2025-08)
4. Your budget will be saved for comparison with actual spending

### Adding an Expense

1. Select option 2 from the main menu
2. Enter the expense name when prompted
3. Enter the expense amount (numbers only)
4. Enter the expense date in YYYY-MM-DD format
5. Select a category from the numbered list:
   - 🍔 Food
   - 🚗 Transport
   - 🏠 Utilities
   - 🎮 Entertainment
   - 📦 Other
6. Your expense will be saved automatically and a summary will be displayed

### Viewing Summaries

Select option 4 to access the comprehensive summary menu with options for:
- Daily totals (with year/month filtering)
- Monthly totals
- Yearly totals
- Category totals
- All expenses list
- Monthly budget comparison
- Interactive data visualization

### Exporting Data

Select option 5 to export your expenses in different formats:
- **CSV**: For spreadsheet applications like Excel
- **JSON**: For web applications and data processing
- **XML**: For structured data exchange

### Example Session

```
Welcome to the Expense Tracker!
Please select an option:
1. Set Budget
2. Add Expense
4. View Expense Summary
5. Export Expenses to Different Format
6. Exit
Enter your choice (1-6): 2

Getting expense details...
Enter expense name: Coffee
Enter expense amount: 4.50
Enter expense date (2025-08-06): 2025-08-06
You've entered: Coffee, 4.50, 2025-08-06
Select a category for the expense:
 1. Food
 2. Transport
 3. Utilities
 4. Entertainment
 5. Other
Enter the number of the category: 1
You selected: Food

Expense recorded:
  Name    : Coffee
  Amount  : $4.50
  Category: Food
  Date    : 2025-08-06
```

## File Structure

```
Python-Expense-Tracker/
├── expense.py              # Expense class definition
├── expense_tracker.py      # Main application logic
├── expenses.csv           # Expense data storage (auto-generated)
├── budget.csv             # Budget data storage (auto-generated)
├── exported_expenses.csv   # Exported CSV data (when exported)
├── exported_expenses.json  # Exported JSON data (when exported)
├── exported_expenses.xml   # Exported XML data (when exported)
├── README.md             # This file
└── .codebuddy/
    └── .gitignore        # Git ignore rules
```

## Data Storage

### Expenses
Expenses are stored in `expenses.csv` with the following format:
```csv
name,amount,category,date
Sushi,10.65,Food,2025-08-05
Train,1.45,Transport,2025-07-31
```

### Budgets
Monthly budgets are stored in `budget.csv` with the following format:
```csv
budget_amount,month
2000.0,2025-08
1500.0,2025-09
```

## Sample Output

### Expense Summary
```
=== 💰 Expense Summary 💰 ===

🍔 Food - Sushi: $10.65 on 2025-08-05
🍔 Food - Hamburger: $12.54 on 2025-08-07
🚗 Transport - Gas: $20.65 on 2025-08-05
🏠 Utilities - Electric: $70.50 on 2024-07-31
🎮 Entertainment - Netflix: $7.99 on 2025-08-31

=== 📊 Summary Options 📊 ===
1. View daily totals
2. View monthly totals  
3. View yearly totals
4. View category totals
5. View all expenses
6. View monthly budget comparison
7. Visualize expenses
8. Exit
```

### Budget Comparison
```
=== 📊 Budget Comparison 📊 ===
2025-08: Under budget by $1456.15
```

### Category Totals
```
=== 📊 Category Totals 📊 ===
🍔 Food: $1103.73
🚗 Transport: $3060.65
🏠 Utilities: $352.50
🎮 Entertainment: $14.54
📦 Other: $20.75
```

## Code Structure

### Classes

- **`Expense`**: Simple data class to represent an expense with name, amount, and category

### Main Functions

- **`main()`**: Interactive menu system for navigating application features
- **`get_budget()`**: Collects and validates monthly budget information
- **`get_expense_details()`**: Interactive function to collect expense information with date validation
- **`write_expense_to_file()`**: Saves expense data to CSV file with date tracking
- **`summarize_expenses()`**: Comprehensive expense analysis with multiple viewing options
- **`export_expenses()`**: Exports expense data to CSV, JSON, or XML formats

### Key Features

- **Date Validation**: Ensures proper date formats (YYYY-MM-DD for expenses, YYYY-MM for budgets)
- **Interactive Visualization**: Uses Plotly to create interactive charts including:
  - Monthly expense bar charts
  - Category distribution pie charts  
  - Daily expense line graphs
  - Cumulative expense trend analysis
- **Budget Tracking**: Compares monthly spending against set budgets
- **Data Export**: Multiple export formats for external analysis
- **Flexible Summaries**: Daily, monthly, yearly, and category-based expense views

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request
## Future Enhancements

- [x] Date tracking for expenses --> Completed 05/08/2025
- [x] Monthly/yearly expense reports --> Completed 05/08/2025
- [x] Budget setting and tracking --> Completed 05/08/2025
- [x] Data visualization with charts --> Completed 06/08/2025
- [x] Export to different formats (JSON, Excel) --> Completed 06/08/2025
- [ ] Search and filter functionality
- [ ] Expense editing and deletion
- [ ] Multiple user support

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Happy expense tracking! 📊💰**
