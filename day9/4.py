class BankAccount:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            print("Withdraw:", amount)

    def display_balance(self):
        print("Account Number:", self.account_number)
        print("Current Balance:", self.balance)
        print("----------------------")

account1 = BankAccount(12345, 1000)

account1.deposit(500)
account1.withdraw(300)
account1.display_balance()
