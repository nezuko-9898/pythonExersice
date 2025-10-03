class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder  # Public attribute
        self.__balance = initial_balance      # Private attribute (encapsulated)

    # Public method to check balance
    def get_balance(self):
        return f"Current balance: ₹{self.__balance}"

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"₹{amount} deposited successfully!"
        return "Invalid deposit amount!"

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"₹{amount} withdrawn successfully!"
        return "Insufficient balance or invalid amount!"

# Example usage
account = BankAccount("Rahul", 5000)
print(account.get_balance())  # Access balance via method
print(account.deposit(2000))  # Deposit money
print(account.withdraw(3000)) # Withdraw money
print(account.get_balance())  # Check updated balance
