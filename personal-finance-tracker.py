#  Build a tool that allows users to track their income, expenses, 
# and provide a summary of their financial health.
import datetime



# Define the Transaction class to represent financial transactions
class Transaction:
    # Initialize a new Transaction object with necessary attributes
    def __init__(self, amount, date, type, description):
        self.amount = amount  # The monetary value of the transaction
        self.date = date if isinstance(date, datetime.date) else datetime.datetime.strptime(date, "%Y-%m-%d")   # ensure The date of the transaction is a datetime.date object
        self.type = type  # The type of transaction ('income' or 'expense')
        self.description = description  # A brief description of the transaction

# Define the FinanceTracker class to manage and track transactions
class FinanceTracker:
    # Initialize the FinanceTracker with an empty list to store transactions
    def __init__(self):
        self.transactions = []

    # Method to add a transaction directly to the tracker
    def add_transaction(self, transaction):
        self.transactions.append(transaction)  # Append the transaction to the list

    # Method to add an income transaction
    def add_income(self, amount, date, description):
        income = Transaction(amount, "income", date, description)  # Create a new Transaction as income
        self.transactions.append(income)  # Add it to the list of transactions

    # Method to add an expense transaction
    def add_expense(self, amount, date, description):
        expense = Transaction(amount, "expense", date, description)  # Create a new Transaction as expense
        self.transactions.append(expense)  # Add it to the list of transactions

    # Method to calculate and return the current balance based on transactions
    def get_balance(self):
        balance = 0  # Start with a balance of zero
        for transaction in self.transactions:  # Loop through each transaction
            if transaction.type == 'income':
                balance += transaction.amount  # Increase balance for income
            elif transaction.type == 'expense':
                balance -= transaction.amount  # Decrease balance for expenses
        return balance  # Return the calculated balance

    # Method to print a summary of all transactions
    def show_transaction(self):
        running_balance = 0  # Keep track of the balance as we list transactions
        print("Date\t\tType\tAmount\tBalance\tDescription")  # Print table headers
        for transaction in self.transactions:  # Loop through each transaction
            # Adjust the running balance based on the transaction type
            if transaction.type == "income":
                running_balance += transaction.amount
            else:
                running_balance -= transaction.amount
            # Print details of the transaction including the running balance
            print(f"{transaction.date}\t{transaction.type}\t{transaction.amount}\t{running_balance}\t{transaction.description}")


    def add_transaction_ui(self):
    # Example of user input for a transaction
        amount = float(input("Amount: "))
        date_str = input("Date (YYYY-MM-DD): ")
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        type = input("Type (income/expense): ")
        description = input("Description: ")
        self.add_transaction(Transaction(amount, date, type, description))


finance_tracker = FinanceTracker()  # Create an instance of the FinanceTracker class
finance_tracker.add_transaction_ui()  # Call the add_transaction_ui() method on the instance
