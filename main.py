class Transaction:
    """
    Represents a single financial transaction.
    """
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount


class FinanceManager:
    """
    Manages financial transactions and provides functionalities to add transactions,
    view transaction history, and calculate balance.
    """
    def __init__(self):
        self.transactions = []

    def add_transaction(self, date, description, amount):
        self.transactions.append(Transaction(date, description, amount))
        print("Transaction added successfully!")

    def view_transactions(self):
        if self.transactions:
            print("\nTransaction History:")
            for index, transaction in enumerate(self.transactions, start=1):
                print(f"{index}. Date: {transaction.date}, Description: {transaction.description}, Amount: {transaction.amount}")
        else:
            print("Your transaction history is empty!")

    def calculate_balance(self):
        total_income = sum(t.amount for t in self.transactions if t.amount > 0)
        total_expenses = sum(t.amount for t in self.transactions if t.amount < 0)
        balance = total_income + total_expenses
        print(f"\nTotal Income: {total_income}")
        print(f"Total Expenses: {total_expenses}")
        print(f"Current Balance: {balance}")


def main():
    finance_manager = FinanceManager()

    while True:
        print("\n===== Personal Finance Manager =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Calculate Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            amount = float(input("Enter income amount: "))
            finance_manager.add_transaction(date, description, amount)
        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            amount = float(input("Enter expense amount: "))
            finance_manager.add_transaction(date, description, -amount)
        elif choice == "3":
            finance_manager.view_transactions()
        elif choice == "4":
            finance_manager.calculate_balance()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
