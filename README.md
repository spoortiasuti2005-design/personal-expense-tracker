# Personal Expense Tracker with CSV

## Project Description
A simple Python application to record daily expenses by category and store them permanently in a CSV file.

## Features
- Add new expenses
- View all expenses
- Filter expenses by category
- Calculate category-wise totals
- Validate dates and amounts
- Store data using CSV files

## Technologies Used
- Python
- CSV module
- VS Code

## How to Run
1. Install Python.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run:

```bash
python expense_tracker.py
```

## Learning Outcomes
- File handling
- CSV read and write operations
- Python dictionaries
- Loops and conditional statements
- Input validation
- Functions

## Problem Fixed
During testing, the CSV file was empty, so Python could not find the Date column. I fixed this by checking whether the file exists or is empty and writing the correct header row when needed.

## Sample Program Output

### 1. Main Menu

```text
===== PERSONAL EXPENSE TRACKER =====
1. Add Expense
2. View All Expenses
3. Filter Expenses by Category
4. Category-wise Summary
5. Exit

Enter your choice:
```

### 2. View All Expenses

```text
--- All Expenses ---
Date: 2026-11-01 | Category: Food | Description: Breakfast | Amount: ₹ 80
Date: 2026-11-02 | Category: Travel | Description: Bus fare | Amount: ₹ 40
Date: 2026-11-03 | Category: Shopping | Description: Notebook | Amount: ₹ 150
Date: 2026-11-04 | Category: Food | Description: Lunch | Amount: ₹ 120
Date: 2026-11-05 | Category: Education | Description: Python book | Amount: ₹ 500
```

### 3. Category-wise Summary

```text
--- Category-wise Summary ---
Food: ₹ 380
Travel: ₹ 390
Shopping: ₹ 500
Education: ₹ 700

Total Expenses: ₹ 1970
```

### 4. Exit

```text
Thank you for using Personal Expense Tracker!
```

*Note: Sample output is based on the 10 sample expense records in expenses.csv.*