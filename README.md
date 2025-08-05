# Python Expense Tracker 💰

A simple yet effective command-line expense tracking application built in Python. Track your daily expenses, categorize them, and get detailed summaries of your spending habits.

## Features ✨

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

3. No additional dependencies required - uses only Python standard library!

## Usage

Run the expense tracker:

```bash
python expense_tracker.py
```

### Adding an Expense

1. Enter the expense name when prompted
2. Enter the expense amount (numbers only)
3. Select a category from the numbered list
4. Your expense will be saved automatically

### Example Session

```
Welcome to the Expense Tracker!
Getting expense details...
Enter expense name: Coffee
Enter expense amount: 4.50
You've entered: Coffee, 4.50
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
```

## File Structure

```
Python-Expense-Tracker/
├── expense.py              # Expense class definition
├── expense_tracker.py      # Main application logic
├── expenses.csv           # Data storage (auto-generated)
├── README.md             # This file
└── .codebuddy/
    └── .gitignore        # Git ignore rules
```

## Data Storage

Expenses are stored in `expenses.csv` with the following format:
```csv
name,amount,category
Sushi,10.0,Food
Train,1.45,Transport
```

## Sample Output

```
=== 💰 Expense Summary 💰 ===

🍔 Food - Sushi: $10.00
🍔 Food - Burger: $20.00
🚗 Transport - Train: $1.45
🚗 Transport - Gas: $30.00
🏠 Utilities - Sofa: $400.00
🏠 Utilities - Internet: $45.95

=== 📊 Category Totals 📊 ===
🍔 Food: $30.00
🚗 Transport: $31.45
🏠 Utilities: $445.95

=== 💵 Grand Total 💵 ===
Total Expenses: $507.40
```

## Code Structure

### Classes

- **`Expense`**: Simple data class to represent an expense with name, amount, and category

### Main Functions

- **`get_expense_details()`**: Interactive function to collect expense information from user
- **`write_expense_to_file()`**: Saves expense data to CSV file
- **`summarize_expenses()`**: Reads and displays expense summaries with category breakdowns

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## Future Enhancements

- [ ] Date tracking for expenses
- [ ] Monthly/yearly expense reports
- [ ] Budget setting and tracking
- [ ] Data visualization with charts
- [ ] Export to different formats (JSON, Excel)
- [ ] Search and filter functionality
- [ ] Expense editing and deletion
- [ ] Multiple user support

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Happy expense tracking! 📊💰**
