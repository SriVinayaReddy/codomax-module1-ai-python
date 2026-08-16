# CODOMAX Internship - Module 2
# Project 4: Expense Tracker

import json
import os
 
DATA_FILE = "expenses.json"
 
 
def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []
 
 
def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)
 
 
def add_expense(expenses):
    category = input("Category (e.g., Food, Travel, Bills): ")
    amount = float(input("Amount: "))
    note = input("Note (optional): ")
    expenses.append({"category": category, "amount": amount, "note": note})
    save_expenses(expenses)
    print("Expense added.")
 
 
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n=== All Expenses ===")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['category']} - {exp['amount']} ({exp['note']})")
 
 
def filter_by_category(expenses):
    category = input("Enter category to filter by: ")
    filtered = [e for e in expenses if e["category"].lower() == category.lower()]
    if not filtered:
        print("No expenses found in that category.")
        return
    print(f"\n=== Expenses in '{category}' ===")
    for exp in filtered:
        print(f"{exp['category']} - {exp['amount']} ({exp['note']})")
 
 
def delete_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return
    index = int(input("Enter the number of the expense to delete: ")) - 1
    if 0 <= index < len(expenses):
        removed = expenses.pop(index)
        save_expenses(expenses)
        print(f"Deleted: {removed['category']} - {removed['amount']}")
    else:
        print("Invalid entry number.")
 
 
def total_expenses(expenses):
    total = sum(e["amount"] for e in expenses)
    print(f"Total spent: {total}")
 
 
def expense_tracker():
    expenses = load_expenses()
 
    menu = """
=== Expense Tracker ===
1. Add Expense
2. View All Expenses
3. Filter by Category
4. Delete Expense
5. View Total Spend
6. Exit
"""
 
    while True:
        print(menu)
        choice = input("Choose an option (1-6): ")
 
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            filter_by_category(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            total_expenses(expenses)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
 
 
if __name__ == "__main__":
    expense_tracker()
 