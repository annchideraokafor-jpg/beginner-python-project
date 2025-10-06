expenses = []
def add_expense():
    name = input("Enter expense name: ")
    # validate amount input
    while True:
        amt_str = input("Enter amount: #")
        try:
            amount = float(amt_str)
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")
    date = input("Enter date (YYYY-MM-DD): ")
    expenses.append({"name": name, "amount": amount, "date": date})
    print("Expense added successfully.\n")
def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
    else:
        print("\n--- Expense List---:")
        total = 0
        for idx, expense in enumerate(expenses, 1):
            print(f"{idx}. {expense['name']} - #{expense['amount']} on {expense['date']}")
            total += expense['amount']
        print(f"\nTotal Expenses: #{total}\n")
def delete_expense():
    if not expenses:
        print("No expenses to delete.\n")
        return
    view_expenses()
    try:
        num = int(input("Enter the expense number to delete: "))
    except ValueError:
        print("Invalid input. Please enter a number.\n")
        return
    if 0 < num <= len(expenses):
        removed = expenses.pop(num - 1)
        print(f"Removed expense: {removed['name']} successfully.\n")
    else:
        print("Invalid number.\n")


def main_menu():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main_menu()