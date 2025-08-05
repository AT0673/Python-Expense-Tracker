# Python Expense Tracker 💰

A simple yet effective command-line expense tracking application built in Python. Track your daily expenses, categorize them, and get detailed summaries of your spending habits.

## Why I Built This 🎓

Im currently a University Student, and as we all know, budgeting at Univeristy is **HARD**. Between all my eating-out, partying, etc, I was quickly losing track of my finances, and often spent many days wondering where the hell it all went.
Thus, this expense tracker was born. I wanted something I could quickly use between classes, that would store my data locally, and give me clear insights into where, and how, my money was disappearing. The categorization feature made me realise that I was spending pretty much all my money on takeaway, and the summaries became essential to review to make sure I was keeping on track, and could continue to afford life.

I built this during my First-Year of Univeristy, using the fundementals I was learning in my Programming module, this just uses a different programming language to the one I was learning (Scala), this project served me well as both as a practical tool and a demonstration of the clean, functional programming principles I was learning throughout my First-year.

## Requirements & Architecture 📋

### Core Requirements
This application was designed to meet my rather loose needs for a personal finance managing tool:

- **User-Friendly Expense Entry**: Allow users to quickly input expenses with minimal friction
- **Data Storage**: Save all expenses to a CSV file for long-term tracking and data portability
- **Comprehensive Expense Summarization**: Provide clear breakdowns of spending by category and total amounts
- **Budget Awareness**: Show spending patterns to help me stop my outrageous takeaway addiction
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

- [x] Date tracking for expenses --> Completed 05/08/2025
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
