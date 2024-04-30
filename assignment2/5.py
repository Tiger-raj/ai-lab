#   Create a class to represent a bank account with attributes like account number, balance, and owner name.
#   Implement methods to deposit, withdraw, and display account information.

# class definition
class bankAccount:
    # initializing the bankAccount class
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    # method to deposit money
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    # method to withdraw money
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            return self.balance

    # method to display account information
    def display(self):
        return f"\tAccount Number: {self.account_number}\tOwner Name: {self.owner_name}\tBalance: {self.balance}"

# create an instance of BankAccount
account = bankAccount("4567463989", "Rishikesh kumar", 5000)

# display initial account information
print("Account created , Account status is :\n",account.display())

# deposit money
account.deposit(3400)
print("After deposit,Account status :\n", account.display())

# withdraw money
account.withdraw(3000)
print("After withdrawal,Account status :\n ", account.display())

