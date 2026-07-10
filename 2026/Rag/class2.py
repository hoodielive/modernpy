class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful. New balance: {self.balance}")


    def withdraw(self, amount):
        if amount > self.balance:
            print("You do not have any money to withdraw.")
        else:
            self.balance -= amount
            print(f"You have withdrawn {amount} and your new balance is {self.balance}")
        return amount

account = BankAccount("Sophia Christos", 2000.00)
print(f"New Account holder: {account.account_holder}.")
print(f"The balance on the account is: {account.balance}")
account.deposit(4444.00)
print(f"You have deposited $2,000.00 leaving you with a whopping {account.balance}")
account.withdraw(6000.00)
account.withdraw(995.00)
