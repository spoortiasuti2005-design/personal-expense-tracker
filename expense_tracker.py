
import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


# 1. Create CSV file
def create_file():
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])


# 2. Add a new expense
def add_expense():
    print("\n--- Add Expense ---")

    while True:
        date = input("Enter date (YYYY-MM-DD): ")

        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date! Please try again.")

    category = input("Enter category: ").strip()

    while not category:
        print("Category cannot be empty.")
        category = input("Enter category: ").strip()

    description = input("Enter description: ").strip()

    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("Expense added successfully!")


# 3. View all expenses
def view_expenses():
    print("\n--- All Expenses ---")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        found = False

        for expense in reader:
            found = True

            print(
                "Date:", expense["Date"],
                "| Category:", expense["Category"],
                "| Description:", expense["Description"],
                "| Amount: ₹", expense["Amount"]
            )

        if not found:
            print("No expenses found.")


# 4. Filter expenses by category
def filter_expenses():
    category = input("\nEnter category to search: ").strip()

    print("\n--- Filtered Expenses ---")

    found = False

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for expense in reader:
            if expense["Category"].lower() == category.lower():
                found = True

                print(
                    "Date:", expense["Date"],
                    "| Category:", expense["Category"],
                    "| Description:", expense["Description"],
                    "| Amount: ₹", expense["Amount"]
                )

    if not found:
        print("No expenses found in this category.")


# 5. Category-wise summary
def category_summary():
    print("\n--- Category Summary ---")

    totals = {}

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for expense in reader:
            category = expense["Category"]
            amount = float(expense["Amount"])

            if category in totals:
                totals[category] += amount
            else:
                totals[category] = amount

    if not totals:
        print("No expenses available.")
        return

    grand_total = 0

    for category, amount in totals.items():
        print(category, ": ₹", round(amount, 2))
        grand_total += amount

    print("-------------------------")
    print("Total Expenses: ₹", round(grand_total, 2))


# 6. Main menu
def main():
    create_file()

    while True:
        print("\n===== PERSONAL EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter Expenses by Category")
        print("4. Category-wise Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            filter_expenses()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice! Please try again.")


# 7. Start the program
if __name__ == "__main__":
    main()
