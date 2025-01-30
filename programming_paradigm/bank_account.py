class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
        # self.initial_balance = initial_balance
        # initial_balance = 0

    def deposit(self, amount):
        # print(f"You have deposited ${amount}. Current balance is: ${amount + self.account_balance}")
        return amount + self.account_balance

    def withdraw(self, amount):
        if amount < self.account_balance:
            self.account_balance -= amount
            # print(f"You have withdrawn ${amount}. Current balance is: ${self.account_balance - amount}")
            return True

        else:
            # print("Insufficient funds or invalid amount.")
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")


